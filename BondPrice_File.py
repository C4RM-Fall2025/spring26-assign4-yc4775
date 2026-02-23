def getBondPrice(y, face, couponRate, m, ppy=1):
    n = int(m * ppy)
    r = y / ppy
    coupon = face * couponRate / ppy

    bondPrice = 0.0
    for t in range(1, n + 1):
        bondPrice += coupon / ((1 + r) ** t)

    bondPrice += face / ((1 + r) ** n)
    return bondPrice