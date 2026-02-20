from binance.exceptions import BinanceAPIException

class OrderManager:
    """
    Handles the actual buying and selling logic.
    """
    def __init__(self, client, logger):
        self.client = client
        self.logger = logger

    def place_order(self, symbol: str, side: str, order_type: str, quantity: float, price: float = None):
        self.logger.info(f"Preparing to place {side} {order_type} order for {quantity} {symbol}...")
        
        # Prepare base parameters required for all orders
        params = {
            'symbol': symbol,
            'side': side,
            'type': order_type,
            'quantity': quantity
        }

        # Add specific parameters for LIMIT orders
        if order_type == 'LIMIT':
            params['price'] = price
            params['timeInForce'] = 'GTC' # Good Till Canceled

        try:
            # Sending request to Binance Futures (USDT-M)
            response = self.client.futures_create_order(**params)
            
            # Extracting the important details to show the user
            order_id = response.get('orderId')
            status = response.get('status')
            executed_qty = response.get('executedQty')
            avg_price = response.get('avgPrice', 'N/A (Limit Order Unfilled)')
            
            self.logger.info("ORDER SUCCESSFUL!")
            self.logger.info(f"Order ID: {order_id}")
            self.logger.info(f"Status: {status}")
            self.logger.info(f"Executed Qty: {executed_qty}")
            self.logger.info(f"Average Price: {avg_price}")
            
            return response

        except BinanceAPIException as e:
            # Catch API errors (e.g., Insufficient funds, invalid symbol)
            self.logger.error(f"API ERROR: Status {e.status_code} - {e.message}")
        except Exception as e:
            # Catch network errors or other unexpected issues
            self.logger.error(f"UNEXPECTED ERROR: {str(e)}")
            
        return None