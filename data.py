import csv
with open("data.csv", newline='')as f:
     reader=csv.reader(f)
     file_data=list(reader)
file_data.pop(0)
total_people=0
total_classes=len(file_data)
for people in file_data:
    total_people=total_people+float(people[1])
mean= total_people/total_classes
print("mean is:"+str(mean))
import pandas as pd
import plotly.express as px
df=pd.read_csv("data.csv")
fig=px.scatter(df,x="classes",y="people")
fig.update_layout(shapes=[dict(
    type='line',
    y0=mean,y1=mean,
    x0=0,x1=total_classes,
)])
fig.update_yaxes(rangemode="tozero")
