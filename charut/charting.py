import matplotlib.pyplot as plt

def plt_tsline(data, title, subtitle):
    """
    Plots a time series chart.

    Parameters
    ----------
    data: dataframe
            a dataframe with columns date, id, val
    Returns
    -------
    A time series chart.
    """
    data = data.set_index("date")
    fig = plt.figure()
    fig = data["val"].plot(kind="line")
    fig = plt.suptitle(title, x=0.1, y=0.95, horizontalalignment='left', verticalalignment='top')
    fig = plt.title(subtitle, y=1, fontsize=7, loc="left")
    return fig



