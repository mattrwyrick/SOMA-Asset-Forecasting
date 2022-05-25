
from matplotlib import pyplot as plt

from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import ExponentialSmoothing

from soma_forecasts.forecast_mbs.tools import load_aggregate

from soma_forecasts.settings import (
    ROOT_DIRECTORY
)


plt.show(block=True)


def run():
    """
    Run the forecast
    :return:
    """
    df = load_aggregate()
    train, test = df[:503], df[503:]
    n_forecasts = len(test)

    hwes3_add_model = ExponentialSmoothing(train["Current Face Value"], trend="add", seasonal="add", seasonal_periods=8).fit()
    hwes3_mul_model = ExponentialSmoothing(train["Current Face Value"], trend="mul", seasonal="mul", seasonal_periods=8).fit()





def decompoase_balance(df):
    """
    Decompose the balance
    :param df:
    :return:
    """
    decomposition = seasonal_decompose(df["Current Face Value"], model="multiplicative")
    decomposition.plot()
    return decomposition


def set_alpha(df):
    """

    :param df:
    :return:
    """
    m = len(df)
    alpha = 1 / (2 * m)
    return alpha


def forecast(df):
    """

    :param df:
    :return:
    """
    df["HWES3_ADD"] = ExponentialSmoothing(df["Current Face Value"], trend="add", seasonal="add", seasonal_periods=52).fit().fittedvalues
    df["HWES3_MUL"] = ExponentialSmoothing(df["Current Face Value"], trend="mul", seasonal="mul", seasonal_periods=52).fit().fittedvalues
