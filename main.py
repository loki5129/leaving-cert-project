from pandas import *
import plotly.graph_objects as go
from jinja2 import Template
import re
from statistics import mean,median,mode
#csv file name
oginal_filename = r"Pokemon.csv"
#section  of code resolving cleaning the csv file
raw_data = read_csv(oginal_filename)

 #removes all column with the name in the list
to_remove=["place","type2","hp","maxhp","attack","defense","spatk","spdef","speed"]
raw_data.drop(columns=to_remove,inplace=True)

#wirtes cleaned to a new csv
raw_data.to_csv("cleaned_data.csv",index=False)
filename = "cleaned_data.csv"


#reads new csv and turns it into a list of rows
data = read_csv(filename)
data_dict = data.to_dict(orient='records')

#creates empty list for levels and empty dict for types
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
#counts how many times each types is in the data and writes it to the corresponping dict key
keys = list(types.keys())
for i in range(len(data_dict)):
    for c in range(len(keys)):
        key = "\'" + str(keys[c]).lower() + "\'"
        if (key in str(data_dict[i]).lower()):
            types[keys[c]] +=1
            #print("11")
#print(types)

def clean(string):
  #function to get the level out of the index of the list of data
  #uses varouis string method and re method to remove all letters extra numbers and specail characters
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

#applys the clean function to extract the level and apppend it to the level_list
for i in range(len(data_dict)):
    level_to_be_added=clean(data_dict[i])
    #print(level_to_be_added)
    level_list.append(level_to_be_added)



#defines colors for each bar in the bar chart
color = ["#1552E2","#AB2021","#147B3D","#A9702C","#48180B","#1C4B27","#4A677D","#E3E32B","#86D2F5","#5F756D","#5E2D88","#448B95","#33336B","#040706","#971944","#994025","#A42A6C","#FAF9F6"]#defien each colour for each bar in hexcode

#gets the x of the bar chart to be the the name of each type
#get the y as the correspong amount of time that tpye appears in the data
bar_chart_y= []
bar_chart_x=[]
for i in range(len(keys)):
    bar_chart_y.append(types[keys[i]])
    bar_chart_x.append(keys[i])


#get the mean meadian range and mode for the count of types in the data
stat_type_list ={
    "mean":mean(bar_chart_y),
    "median":median(bar_chart_y),
    "range":max(bar_chart_y)-min(bar_chart_y),
    "mode":mode(bar_chart_y)
}

#gets the mean meadian range and mode for the levels in the data
stat_level_list ={
    "mean":mean(level_list),
    "median":median(level_list),
    "range":max(level_list)-min(level_list),
    "mode":mode(level_list)
}




#creates the bar chart bar with a black outline and 
bar_chart=go.Bar(
    x=bar_chart_x 
    ,y=bar_chart_y,
    name ="",
    marker=dict(color=color, 
                           line=dict(color='rgb(100,100,100)', 
                                     width=1),),  
    xperiodalignment="middle",
    xhoverformat="Q%q",
    hovertemplate="<b>Type: </b>%{x}<br><b>Count: </b>%{y}"
    )
 



histogram=go.Histogram(
    x=level_list,
    histnorm="percent",
    nbinsx=10,
    name ="",
    marker=dict(
        line=dict(color='rgb(100,100,100)',
                  width=1)),
    xhoverformat="Q%q",
    hovertemplate="<b>Probability: </b>%{y}% "
    )
fig=go.Figure() 
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
                        {"visible": [True, False]},  
                        {
                            "title": "Bar Chart of types of pokemon found in trainers",
                            "xaxis":{"dtick": None,"range": None,"title": "Types of Pokémon"},
                            "yaxis":{"title": "Frequency"}, 
                            "annotations":[ {"x":6,"y": 5000,"xref": "x","yref": "y",
                                              "text": (
                                     f"<b>Stats for Bar Chart</b><br>"
                                     f"Mean: {stat_type_list['mean']:.2f}<br>"
                                     f"Median: {stat_type_list['median']:.2f}<br>"
                                     f"Mode: {stat_type_list['mode']}<br>"
                                     f"Range: {stat_type_list['range']}"),
                                     "showarrow": False,
                                     "font": {"size": 14, "color": "black"},
                                     "align": "left",
                                     "bgcolor": "rgba(255, 255, 255, 0.8)"},]}],), 
                dict(
                    label="Histogram",
                    method="update",
                    args=[
                        {"visible": [False, True]},  
                        {
                            "title": "Histogram of Pokémon Levels Found in Trainers",
                            "xaxis": {"dtick": 10,"title": "Levels of Pokémon"} ,
                            "yaxis":{"title": "Probability of level occuring",},
                             "annotations":[ {"x": 0,"y": 15,"xref": "x","yref": "y",
                                              "text": (
                                     f"<b>Stats for Histogram</b><br>"
                                     f"Mean: {stat_level_list['mean']:.2f}<br>"
                                     f"Median: {stat_level_list['median']:.2f}<br>"
                                     f"Mode: {stat_level_list['mode']}<br>"
                                     f"Range: {stat_level_list['range']}"),
                                     "showarrow": False,
                                     "font": {"size": 14, "color": "black"},
                                     "align": "left",
                                     "bgcolor": "rgba(255, 255, 255, 0.8)"},]}],),
                        
                
                
            ],
            showactive=True,
           
        )
    ],                           
    title="Frequency that types of pokemon appear in trainers",
    margin=dict(l=200, r=50, t=50, b=120), 
    xaxis_title="types of pokemon",
    xaxis=dict(scaleanchor="y"),
    yaxis_title="Frequency",annotations=[  
        {
            "x": 6,
            "y": 5000,
            "xref": "x",
            "yref": "y",
            "text": (
                f"<b>Stats for Bar Chart</b><br>"
                f"Mean: {stat_type_list['mean']:.2f}<br>"
                f"Median: {stat_type_list['median']:.2f}<br>"
                f"Mode: {stat_type_list['mode']}<br>"
                f"Range: {stat_type_list['range']}"
            ),
            "showarrow": False,
            "font": {"size": 14, "color": "black"},
            "align": "left",
            "bgcolor": "rgba(255, 255, 255, 0.8)",
            
            
        }
    ],

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
output_html_path = r"graph.html"

plotly_jinja_data = {"fig":div}
with open(output_html_path, "w", encoding="utf-8") as output_file:
    with open(input_html_path) as template_file:
        j2_template = Template(template_file.read())
        output_file.write(j2_template.render(plotly_jinja_data))


