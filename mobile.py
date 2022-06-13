import ploty.figure_factory as ff
import pandas as pd
import csv

df = pd.read_csv ("data.csv")
fig = ff.create_displot([df["Mobile Brand"].tolist()],["Mobile Brand"],show_hist = False)
fig.show()