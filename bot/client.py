from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException

class BinanceTestnetClient:
    """
    A wrapper around the official binance-python client.
    Configured strictly for the Binance Futures Testnet.
    """
    def __init__(self, api_key: str, api_secret: str, logger):
        self.logger = logger
        try:
            # testnet=True automatically routes to https://testnet.binancefuture.com for futures calls
            self.client = Client(api_key, api_secret, testnet=True)
            self.logger.info("Successfully initialized Binance Client for Testnet.")
        except Exception as e:
            self.logger.error(f"Failed to initialize Binance Client: {str(e)}")
            raise e

    def get_client(self):
        return self.client