import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from plotly.offline import download_plotlyjs, iplot, plot, init_notebook_mode

tesla = pd.read_csv('tsla.csv', index_col=0).drop('Volume', axis=1)
time_plot = tesla.plot.line(x=tesla.index, y = 'Close', figsize=(12, 4), lw=1)
box_plot = tesla.plot.box()

time_plot.figure.savefig('tesla_stock_time.png')
box_plot.figure.savefig('tesla_stock_box.png')
