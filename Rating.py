import ploty.figure_factory as ff
import pandas as pd
import csv

df = pd.read_csv ("data.csv")
fig = ff.create_displot([df["Avg Rating"].tolist()],["Avg Rating"],show_hist = False)
fig.show()