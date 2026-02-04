from binance.enums import *
from .logger import logger

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        symbol = symbol.upper()
        side = side.upper()
        order_type = order_type.upper()

        logger.info(f"Sending {order_type} {side} request for {symbol} | Qty: {quantity}")

        if order_type == "MARKET":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
        elif order_type == "LIMIT":
            if not price:
                raise ValueError("Price is required for LIMIT orders.")
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=price
            )
        
        logger.info(f"SUCCESS: OrderID {response['orderId']} | Status: {response['status']}")
        return response

    except Exception as e:
        logger.error(f"FAILED to place order: {e}")
        return None
