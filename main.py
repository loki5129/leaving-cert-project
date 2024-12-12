from pandas import *
#csv file name
filename = "C:\\Users\\Student 2021\\Desktop\\tsw\\CS PROJECT\\Pokemon.csv"


data = read_csv(filename)


data_dict = data.to_dict(orient='records')

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

import matplotlib.pyplot as plt

y = [types["Bug"],types["Dark"],types["Dragon"],types["Electric"],types["Fairy"],types["Fighting"],types["Fire"],types["Flying"],types["Ghost"],types["Grass"],types["Ground"],types["Ice"],types["Normal"],types["Poison"],types["Psychic"],types["Rock"],types["Steel"],types["Water"]]
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

plt.plot(x,y)

plt.show()