def calc_discont(price, discont: float = 0.1):
    price_disc = (price - (price*discont))
    return price_disc