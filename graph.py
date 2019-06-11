import pandas as pd
from matplotlib import pyplot

try:
    series = pd.read_csv('stats.csv', header=0, names=['date', 'stars', 'downloads'])
    series.plot(y='stars')
    pyplot.show()

    series.plot(y='downloads')
    pyplot.show()
except FileNotFoundError:
    print("stats.csv doesn't exist.")
