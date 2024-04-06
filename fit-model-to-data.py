xi = [0.4,0.5,0.6,0.7,0.8]
yi = [0.1,0.25,0.55,0.75,0.85]



# m = Summation(xi - xBar)yi / Summation(xi - xBar)**2
def fit(xi, yi):

    xBar = sum(xi) /len(xi)
    yBar = sum(yi) /len(yi)

    print('xBar = ', xBar)
    print('yBar = ', yBar)

    top = 0
    bottom = 0
    for i in range(len(xi)):
        x = xi[i]
        y = yi[i]

        top += (x-xBar) * y
        bottom += (x-xBar) ** 2 
    m = top / bottom
    c = yBar - m * xBar
    print('m = ', m)
    print('c = ', c)

fit(xi, yi)