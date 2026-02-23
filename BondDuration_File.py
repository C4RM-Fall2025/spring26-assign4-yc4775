def getBondDuration(y, face, couponRate, m, ppy=1):
    n = int(m * ppy)
    r = y / ppy
    coupon = face * couponRate / ppy

    price = 0.0
    weighted_pv_sum = 0.0

    for t in range(1, n + 1):
        cf = coupon
        if t == n:
            cf += face

        pv = cf / ((1 + r) ** t)
        price += pv
        weighted_pv_sum += (t / ppy) * pv

    bondDuration = weighted_pv_sum / price
    return bondDuration