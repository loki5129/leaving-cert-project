from pandas import *
import plotly.graph_objects as px
from jinja2 import Template
import re
#csv file name
oginal_filename = r"C:\Users\student\Downloads\leaving-cert-project-main\leaving-cert-project-main\Pokemon.csv"
#section  of code resolving cleaning the csv file
raw_data = read_csv(oginal_filename)
#print(raw_data)
raw_data.pop("place")
#print(raw_data)
raw_data.pop("type2")
#print(raw_data)
raw_data.pop("hp")
#print(raw_data)
raw_data.pop("maxhp")
#print(raw_data)
raw_data.pop("attack")
#print(raw_data)
raw_data.pop("defense")
#print(raw_data)
raw_data.pop("spatk")
#print(raw_data)
raw_data.pop("spdef")
#print(raw_data)
raw_data.pop("speed")
#print(raw_data)

raw_data.to_csv("cleaned_data.csv",index=False)
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
  
  string=str(string)
  string=string.lower()
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


bar_chart_y= []
bar_chart_x=[]
for i in range(len(keys)):
    bar_chart_y.append(types[keys[i]])
    bar_chart_x.append(keys[i])







bar_chart=px.Bar(
    x=bar_chart_x 
    ,y=bar_chart_y,
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
                            },
                            "yaxis":{
                                "title": "frequncey"
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
                            "xaxis": {
                                "dtick": 10,  
                                "title": "Levels of Pokémon",  
                            } ,
                            "yaxis":{
                                "title": "probality of level occuring",
                            }
                        },
                    ],
                ),  
            ],
            showactive=True,
        )
    ],
    title="frequency that types of pokemon appear in trainers",
    margin=dict(l=50, r=50, t=50, b=120), 
    xaxis_title="types of pokemon",
    yaxis_title="Frequency",
          )    
fig.update_xaxes(fixedrange=True)
config = {
   "displaylogo": False,
    "modeBarButtonsToRemove": [
        'zoom',
        'pan',
        "zoomin",
        "zoomout",
        "select",
        "lasso2d",
        "toimage"]
}

#fig.show(config=config)




output_js_path=r"plot.js"
input_templatejs_path = r"template.js"
plotly_jinja_data = {"fig":fig.to_html(full_html=False,include_plotlyjs=False,include_mathjax=False,default_height=800,config=config)}


with open(output_js_path, "w", encoding="utf-8") as output_file:
    with open(input_templatejs_path) as template_file:
        j2_template = Template(template_file.read())
        output_file.write(j2_template.render(plotly_jinja_data))


with open(output_js_path,"r")as f:
    lines=f.read()
    
div=lines[:148]
lines=lines[215:-48]

with open(output_js_path,"w")as f:
    f.write(lines)


input_html_path = r"template.html"
output_html_path = r"index_graph.html"

plotly_jinja_data = {"fig":div}
with open(output_html_path, "w", encoding="utf-8") as output_file:
    with open(input_html_path) as template_file:
        j2_template = Template(template_file.read())
        output_file.write(j2_template.render(plotly_jinja_data))
