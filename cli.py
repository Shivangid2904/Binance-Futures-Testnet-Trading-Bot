import argparse
import logging
from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
    validate_stop_price
)
from bot.logging_config import setup_logger

setup_logger()

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price", required=False)
    parser.add_argument("--stop_price", required=False)
    args = parser.parse_args()

    try:
        symbol = args.symbol.upper()
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)
        stop_price = validate_stop_price(args.stop_price, order_type)

        print("\n📌 Order Summary")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")
        print(f"Price: {price if price else '-'}")
        print(f"Stop Price: {stop_price if stop_price else '-'}")

        # ✅ Confirm BEFORE placing order
        confirm = input("Proceed with order? (y/n): ")
        if confirm.lower() != 'y':
            print("Cancelled")
            return

    # ✅ Now place order
        order = place_order(symbol, side, order_type, quantity, price, stop_price)

        print("\n✅ Order Successful!")

        if order:
            print("Response received from Binance:\n")

            for key, value in order.items():
             print(f"{key}: {value}")

        else:
            print("No response received from API")
        logging.info(f"Order placed successfully: {order}")
    except Exception as e:
        print("\n❌ Order Failed:", str(e))
        logging.error(str(e))


if __name__ == "__main__":
    main()