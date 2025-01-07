from pandas import *
from numpy import *
import csv
#csv file name
oginal_filename = "C:/Users/thoma/Downloads/leaving-cert-project-main/leaving-cert-project-main/Pokemon.csv"
#section  of code resolving cleaning the csv file
data_to_be_cleaned = read_csv(oginal_filename)
#print(data_to_be_cleaned)
data_to_be_cleaned.pop("place")
#print(data_to_be_cleaned)
data_to_be_cleaned.pop("type2")
#print(data_to_be_cleaned)
data_to_be_cleaned.pop("hp")
#print(data_to_be_cleaned)
data_to_be_cleaned.pop("maxhp")
#print(data_to_be_cleaned)
data_to_be_cleaned.pop("attack")
#print(data_to_be_cleaned)
data_to_be_cleaned.pop("defense")
#print(data_to_be_cleaned)
data_to_be_cleaned.pop("spatk")
#print(data_to_be_cleaned)
data_to_be_cleaned.pop("spdef")
#print(data_to_be_cleaned)
data_to_be_cleaned.pop("speed")
#print(data_to_be_cleaned)

data_to_be_cleaned.to_csv("cleaned_data.csv",index=False)
filename = "cleaned_data.csv"

data = read_csv(filename)


data_dict = data.to_dict(orient='records')

level_list = []
types = {
    "Water" :0,
    "Fire" :0,
    "Grass" :0,
    "Ground":0,
    "Rock":0,
    "Bug":0,
    "Flying":0,
    "Electric":0,
    "Bug":0,
    "Ice":0,
    "Steel":0,
    "Poison":0,
    "Dragon":0,
    "Ghost":0,
    "Dark":0,
    "Fairy":0,
    "Fighting":0,
    "Psychic":0,
    "Normal":0,

}

keys = list(types.keys())
for i in range(len(data_dict)):
    for c in range(len(keys)):
        key = "\'" + str(keys[c]).lower() + "\'"
        if (key in str(data_dict[i]).lower()):
            types[keys[c]] +=1
            #print("11")
#print(types)

def clean(string):
  import re
  string=str(string)
  cleaned =re.sub(r"[\([{})\]]","",string)
  #print(cleaned)
  cleaned = re.split(",",cleaned)
  #print(cleaned)
  cleaned.pop(0)
  #print(cleaned)
  cleaned.pop(0)
  #print(cleaned)
  cleaned.pop()
  #print(cleaned)
  cleaned=str(cleaned)
  #print(cleaned)
  cleaned =cleaned.replace("\'pokelevel\':","")
  #print(cleaned)
  cleaned = re.sub(r"[\([{})\]]"," ",cleaned)
  #print(cleaned)
  cleaned = cleaned.replace("\"","")
  #print(cleaned)
  cleaned = int(cleaned)
  #print(cleaned)
  return cleaned

for i in range(len(data_dict)):
    level_to_be_added=clean(data_dict[i])
    #print(level_to_be_added)
    level_list.append(level_to_be_added)




color = ["#1552E2","#AB2021","#147B3D","#A9702C","#48180B","#1C4B27","#4A677D","#E3E32B","#86D2F5","#5F756D","#5E2D88","#448B95","#33336B","#040706","#971944","#994025","#A42A6C","#FAF9F6"]#defien each colour for each bar in hexcode


y= []
for i in range(len(keys)):
    y.append(types[keys[i]])
x=[]
for i in range(len(keys)):
    x.append(keys[i])

standard_devetion_level=std(level_list)
mean_level = mean(level_list)




import plotly.graph_objects as px
bar_chart=px.Bar(
    x=x 
    ,y=y,
    marker=dict(color=color, 
                           line=dict(color='rgb(100,100,100)', 
                                     width=1))
    )
 



histogram=px.Histogram(
    x=level_list,
    histnorm="probability density",
    nbinsx=10,
    marker=dict(
        line=dict(color='rgb(100,100,100)',
                  width=1)
    )
    
    
    )
fig=px.Figure() 
fig.add_trace(bar_chart)
fig.add_trace(histogram)

fig.update_traces(visible=False)
fig.data[0].visible = True


fig.update_layout(
    
   
    
    updatemenus=[
        dict(
            type="dropdown",
            direction="down",
            buttons=[
                dict(
                    label="Bar chart",
                    method="update",
                    args=[
                        {"visible": [True, False]},  # Show histogram, hide bar chart
                        {
                            "title": "Bar Chart of types of pokemon found in trainers",
                            
                            
                            "xaxis":{
                               "dtick": None,
                               "range": None,  # Reset any range set by the Histogram
                               "title": "Types of Pokémon"
                            }
                             },
                    ],
                ), 
                dict(
                    label="Histogram",
                    method="update",
                    args=[
                        {"visible": [False, True]},  # Show bar chart, hide histogram
                        {
                            "title": "Histogram of Pokémon Levels Found in Trainers",
                            "annotations":[
                            dict(
                                x=.5,y=1,
                                xref="paper",yref="paper",
                                text=f"mean={mean_level}\nstandrad deveration={standard_devetion_level}",
                                font=dict(size=14),
                                showarrow=False,
                            )
                        ],
                            "xaxis": {
                                "dtick": 10,  
                                "title": "Levels of Pokémon",  
                            } 
                        },
                    ],
                ),  
            ],
            showactive=True,
        )
    ],
    title="leaving cert project grpahs",
    margin=dict(l=50, r=50, t=50, b=120), 
    xaxis_title="Value",
    yaxis_title="Frequency",
          )    

fig.show()
