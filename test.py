import plotly.graph_objects as px



fig = px.Figure()
x = ["Type A", "Type B", "Type C"]
y = [10, 20, 15]
level_list = [1, 2, 2, 3, 3, 3, 4, 4, 5, 6, 6, 7, 8, 9, 10]
color = "red"
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
    nbinsx=10
    
    
    )
fig.add_trace(bar_chart)
fig.add_trace(histogram)
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
    title="Dropdown to Toggle Between Histogram and Bar Chart",
    xaxis_title="Value",
    yaxis_title="Frequency",
          )    
fig.show()