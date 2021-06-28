  
import plotly.express as px
import csv

with open('./cordata.csv') as file1:
    df = csv.DictReader(file1)
    figure1 = px.scatter(df, x = "Marks In Percentage", y = "Days Present")
    figure1.show()