import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plt_tsline(data, title, subtitle, var_names=None):
    """
    Plots a time series chart.

    Parameters
    ----------
    data:       pandas dataframe
                a dataframe with columns date, val and optional column field if more
                than one series should be drawn
    title:      str
                a title for the chart
    subtitle:   a subtitle for the chart
    var_names:  dict
                optional, if colnames in data are not date, val & field, declare them
                here (eg. {'dates':'date', 'cum_val':'val'})

    Example
    -------
    A = gendat_ts()
    plt_tsline(data=A.loc[:, ['date', 'cum_val']],
               title="Time Series Chart",
               subtitle="example",
               var_names={'cum_val':'val'})

    Returns
    -------
    A time series chart.

    """
    data = data.rename(columns=var_names)
    data = data.set_index("date")
    fig = plt.figure()
    fig = data["val"].plot(kind="line")
    fig = plt.suptitle(title, x=0.1, y=0.95, horizontalalignment='left', verticalalignment='top')
    fig = plt.title(subtitle, y=1, fontsize=7, loc="left")
    return fig





