def equation(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    print('delta:', delta)

    x1 = (-b + (delta ** 0.5)) / (2 * a)
    x2 = (-b - (delta ** 0.5)) // (2 * a)
    print('x1=', x1)
    print('x2=', x2)

