Here is the clean, professional version of your README without emojis and without casual tone:

# Binance Futures Testnet Trading Bot

A structured Python CLI application designed to execute MARKET and LIMIT orders on the Binance Futures Testnet (USDT-M).

## Overview

This project provides a command-line interface for placing futures orders on Binance Testnet. The application is built with a modular architecture to ensure clean separation of concerns, maintainability, and scalability.
It supports both MARKET and LIMIT order types and includes proper validation, error handling, and logging mechanisms.

## Features

### Order Placement

- Supports MARKET and LIMIT orders
- Supports both BUY and SELL sides
- Executes orders on Binance Futures Testnet (USDT-M)

### Input Validation

- Validates CLI arguments before making API requests
- Prevents invalid or incomplete orders from being sent to Binance
- Ensures required parameters (e.g., price for LIMIT orders) are provided

### Error Handling

- Handles Binance API exceptions such as:
  - Insufficient margin
  - Invalid symbols
  - Precision errors
- Handles network-related failures gracefully
- Prevents application crashes due to unhandled exceptions

### Logging

- Logs request summaries and API responses
- Outputs logs to:
  - Console
  - `trading_bot.log` file

- Enables easier debugging and traceability

### Modular Architecture

The application is structured into separate components:

- API interaction layer
- Business logic
- CLI parsing
- Input validation

This separation improves readability, maintainability, and extensibility.

## Setup Instructions

### 1. Clone or Download the Repository

Download the repository and navigate to the project directory.

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate the environment:

**Mac/Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Keys

1. Create an account on Binance Futures Testnet.
2. Generate an API Key and Secret.
3. Rename `.env.example` to `.env`.
4. Add your credentials:

```
BINANCE_TESTNET_API_KEY=your_key_here
BINANCE_TESTNET_API_SECRET=your_secret_here
```

## Usage Examples

All interactions are performed using `cli.py`.

### 1. Place a MARKET BUY Order

Buy 0.01 BTC at the current market price:

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### 2. Place a LIMIT SELL Order

Sell 0.01 BTC if the price reaches 70,000 USDT:

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 70000
```

### 3. Validation Failure Example

Attempting to place a LIMIT order without specifying a price:

```bash
python cli.py --symbol ETHUSDT --side BUY --type LIMIT --quantity 0.5
```

The application prevents execution and displays a validation error before making an API request.

## Assumptions and Design Decisions

### Time in Force

All LIMIT orders are configured as GTC (Good Till Canceled), which is standard for basic limit orders.

### Testnet Configuration

The application relies on the `python-binance` library’s `testnet=True` flag to route requests automatically to the Binance Futures Testnet endpoint.

### Quantity Precision

Binance enforces symbol-specific step sizes and precision rules.
The application assumes users provide valid quantity precision. If invalid precision is entered, the resulting Binance API error is caught and displayed appropriately.
