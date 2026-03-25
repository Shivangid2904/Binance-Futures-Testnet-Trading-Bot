def validate_side(side):
    if side.upper() not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")
    return side.upper()


def validate_order_type(order_type):
    if order_type.upper() not in ["MARKET", "LIMIT", "STOP_LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")
    return order_type.upper()


def validate_quantity(quantity):
    q = float(quantity)
    if q <= 0:
        raise ValueError("Quantity must be positive")
    return q


def validate_price(price, order_type):
    if order_type in ["LIMIT", "STOP_LIMIT"]:
        if price is None:
            raise ValueError("Price required for LIMIT or STOP_LIMIT order")
        p = float(price)
        if p <= 0:
            raise ValueError("Price must be positive")
        return p
    return None
def validate_stop_price(stop_price, order_type):
    if order_type == "STOP_LIMIT":
        if stop_price is None:
            raise ValueError("Stop price required for STOP_LIMIT")
        sp = float(stop_price)
        if sp <= 0:
            raise ValueError("Stop price must be positive")
        return sp
    return None