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
#print(data.describe())

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
 


#creates the histogram with the level list and sets x gaps as 10
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

#create a figure and add the bar chart and histogeam as traces
fig=go.Figure() 
fig.add_trace(bar_chart)
fig.add_trace(histogram)

#sets both the traces to be not visible and sets the default visble to be the bar chart 
fig.update_traces(visible=False)
fig.data[0].visible = True


fig.update_layout(
    
   
    #creates the dropdown
    updatemenus=[
        dict(
            type="dropdown",
            direction="down",
            buttons=[
                dict(
                    label="Bar chart",#label change
                    method="update",#update it to change the graph
                    args=[
                        {"visible": [True, False]},  #makes the bar chart visible and histogram not 
                        {
                            "title": "Bar Chart of types of pokemon found in trainers", # title defined
                            "xaxis":{"dtick": None,"range": None,"title": "Types of Pokémon"},#label x axis
                            "yaxis":{"title": "Frequency"}, #label y axis
                            "annotations":[ {"x":6,"y": 5000,"xref": "x","yref": "y", # postions text box for statisics
                                              "text": (
                                    #addes the statisics for the types in the box
                                     f"<b>Stats for Bar Chart</b><br>"
                                     f"Mean: {stat_type_list['mean']:.2f}<br>" #correct to 2 decimal places
                                     f"Median: {stat_type_list['median']:.2f}<br>"
                                     f"Mode: {stat_type_list['mode']}<br>"
                                     f"Range: {stat_type_list['range']}"),
                                     "showarrow": False, # make it not show messy arrows
                                     "font": {"size": 14, "color": "black"},
                                     "align": "left",
                                     "bgcolor": "rgba(255, 255, 255, 0.8)"},]}],), 
                dict(
                    label="Histogram", #label change
                    method="update",#update it to change the graph
                    args=[
                        {"visible": [False, True]},  #makes the histogram visible and bar chart not 
                        {
                            "title": "Histogram of Pokémon Levels Found in Trainers", #title defined
                            "xaxis": {"dtick": 10,"title": "Levels of Pokémon"} ,#label x axis
                            "yaxis":{"title": "Probability of level occuring",},#label y axis
                             "annotations":[ {"x": 0,"y": 15,"xref": "x","yref": "y",# postions text box for statisics
                                              "text": (
                                      #addes the statisics for the level in the box
                                     f"<b>Stats for Histogram</b><br>"
                                     f"Mean: {stat_level_list['mean']:.2f}<br>" #correct to 2 decimal places
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
    #sets the text box to appear in the default bar chart before the buttons is used
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

#sets the config to remove the logo and the buttons that i will not use
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

#test for the graph
#fig.show(config=config)



#sets the file ouput and input file path for the graph's javascriprt
output_js_path=r"plot.js"
input_templatejs_path = r"template.js"

#using template sytanx set it to replace {{fig}} with the to_html fucntion of the graph with condintons to reduce size and set custom config

plotly_jinja_data = {"fig":fig.to_html(full_html=False,include_plotlyjs=False,include_mathjax=False,default_height=800,config=config)}

#use the template funvtion to place the graph in a javascript file after replace {{fig}} with the graph export
with open(output_js_path, "w", encoding="utf-8") as output_file:
    with open(input_templatejs_path) as template_file:
        j2_template = Template(template_file.read())
        output_file.write(j2_template.render(plotly_jinja_data))

#reads the exported graph text and makes it assecislbe to view
with open(output_js_path,"r")as f:
    lines=f.read()


#takes the fist 148 characters as the div and stores it this is the div that the graph is sent to by the javascript
div=lines[:148]
#changes lines to remove the frist 215 characters and the last 48 as this are not compatilable with the javascpirt
lines=lines[215:-48]

#writes the new and cleaned graph code to the javascript file
with open(output_js_path,"w")as f:
    f.write(lines)

#define the input and ouput html files
input_html_path = r"template.html"
output_html_path = r"graph.html"

plotly_jinja_data = {"fig":div}

#using jinja template replace the {{fig}} in the input html file and place the div that the graph will be placed in and writes it to the ouput file
with open(output_html_path, "w", encoding="utf-8") as output_file:
    with open(input_html_path) as template_file:
        j2_template = Template(template_file.read())
        output_file.write(j2_template.render(plotly_jinja_data))

analysis_txt=""


if sum(types.values())<10000:
    analysis_txt= analysis_txt +"dataset is small and more data is required to refine it further"
   
elif 10000<sum(types.values())<20000:
    analysis_txt= analysis_txt +"dataset is a medsium sized more data is required to refine it further"
  
elif sum(types.values())>20000:
 analysis_txt= analysis_txt +"dataset is a large more data may be required to refine it further"



if stat_type_list["mean"]>stat_type_list["median"]:
    analysis_txt =analysis_txt + "<br>"+"data is right skewed higher values expected"
elif  stat_type_list["mean"]<stat_type_list["median"]:
    analysis_txt = analysis_txt + "<br>"+"data is left skewed lower values expected"
elif stat_type_list["mean"]==stat_type_list["median"]:
    analysis_txt =analysis_txt+"<br>"+ " the data is normally distributed"


if stat_level_list["mean"]!=50:
    analysis_txt = analysis_txt + "<br>"+"the mean of the level data is inblancled and more data is required for an accurate result"
if stat_level_list["mean"] == 50:
    analysis_txt = analysis_txt +" <br>"+" the mean of the level data is balanced, data is not required to refine the result"

if stat_level_list["range"]<80:
    analysis_txt = analysis_txt+"<br>"+"the range of the level data is inaccurate and more data is required to refine the result"
if stat_level_list["range"] >90:
    analysis_txt=analysis_txt+ " <br>"+"the range  of level data is relativitly accurate"

#print(analysis_txt)


print(sum(types.values()))
input_html_path = r"template1.html"
output_html_path = r"analysis.html"

plotly_jinja_data = {"fig":analysis_txt}

#using jinja template replace the {{fig}} in the input html file and place the div that the graph will be placed in and writes it to the ouput file
with open(output_html_path, "w", encoding="utf-8") as output_file:
    with open(input_html_path) as template_file:
        j2_template = Template(template_file.read())
        output_file.write(j2_template.render(plotly_jinja_data))