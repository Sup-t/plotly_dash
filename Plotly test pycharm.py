import pandas as pd
import plotly.express as px
df2 = pd.read_csv(r"C:\Users\tsupr\PycharmProjects\pythonProject\venv\data\bird-window-collision-death.csv")
# This dataframe has 244 lines, but 4 distinct values for `day`

# print(df2.head())
df = px.data.tips()
fig = px.pie(df2, values='Deaths', names='Bldg #', color='Side', hole=0.4)
fig.update_traces(textinfo='label+percent', insidetextfont=dict(color = 'white'))
fig.update_layout(legend={"itemclick":False})
fig.show()