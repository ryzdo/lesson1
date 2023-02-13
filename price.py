def format_price(price):
    if type(price) == str:
        try:
            price = float(price)
        except ValueError as error:
            return error
    price = int(price)
    return f'Цена: {price} руб.'


price_str = format_price(56.24)
print(price_str)
