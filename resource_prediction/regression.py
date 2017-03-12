from pprint import pprint
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.svm import SVR
from etc import plotter
import numpy as np
from etc import reader


def ridge(alpha=10):
    dp = reader.create_regression_dp()
    X = dp.T[0]
    X = np.reshape(X, (len(X),1))
    Y = dp.T[1]

    X_train = X[:2500]
    X_train = np.reshape(X_train, (2500,1))
    Y_train = Y[:2500]
    Y_train = np.reshape(Y_train, (2500,1))

    X_test = X[2500:]
    X_test = np.reshape(X_test, (len(X_test),1))
    Y_test = Y[2500:]

    model = Ridge(alpha=alpha).fit(X_train, Y_train)
    Y_result = model.predict(X)

    plotter.plot_ridge(X, Y, Y_result)
    return

def polynomial(alpha = 10000, degree = 2):
    dp = reader.create_regression_dp()
    X = dp.T[0]
    X = np.reshape(X, (len(X), 1))
    Y = dp.T[1]

    X = PolynomialFeatures(degree).fit_transform(X)

    X_train = X[:2500]
    Y_train = Y[:2500]

    X_test = X[2500:]
    Y_test = Y[2500:]

    model = Ridge(alpha=alpha).fit(X_train, Y_train)
    Y_result = model.predict(X)

    plotter.plot_ridge(X, Y, Y_result)
    return

def svr():
    dp = reader.create_regression_dp()
    X = dp.T[0]
    X = np.reshape(X, (len(X), 1))
    Y = dp.T[1]

    X_train = X[:2500]
    Y_train = Y[:2500]

    X_test = X[2500:]

    clf = SVR(C=1.0, epsilon=0.2)
    clf.fit(X_train, Y_train)
    Y_result = clf.predict(X)

    plotter.plot_ridge(X, Y, Y_result)

    return


