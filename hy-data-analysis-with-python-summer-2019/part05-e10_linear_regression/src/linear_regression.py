#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fit_line(x, y):
    model = LinearRegression()
    model.fit(x[:,np.newaxis], y)
    return model.coef_[0], model.intercept_

def main():
    n = 100
    x = np.linspace(0, 10, n)
    y = x*1.5 + 2 + 1*np.random.randn(n)
    slope, intercept = fit_line(x,y)
    print('Slope: ', slope)
    print('Intercept: ', intercept)
    plt.plot(x, y, 'ro')
    xf = np.linspace(0, 10, 50)
    yf = xf*slope + intercept
    plt.plot(xf, yf, color="black")
    plt.show()


if __name__ == "__main__":
    main()
