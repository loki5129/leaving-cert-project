from pandas import *
#csv file name
filename = "C:\\Users\\Student 2021\\Downloads\\leaving-cert-project-main\\leaving-cert-project-main\\Pokemon.csv"


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
  cleaned =cleaned.replace("\'level\':","")
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


import matplotlib.pyplot as plt

color = ["#1552E2","#AB2021","#147B3D","#A9702C","#48180B","#1C4B27","#4A677D","#E3E32B","#86D2F5","#5F756D","#5E2D88","#448B95","#33336B","#040706","#971944","#994025","#A42A6C","#FAF9F6"]

edgecolor = ["black"]

y = [types[keys[0]],types[keys[1]],types[keys[2]],types[keys[3]],types[keys[4]],types[keys[5]],types[keys[6]],types[keys[7]],types[keys[8]],types[keys[9]],types[keys[10]],types[keys[11]],types[keys[12]],types[keys[13]],types[keys[14]],types[keys[15]],types[keys[16]],types[keys[17]]]

x = [keys[0],keys[1],keys[2],keys[3],keys[4],keys[5],keys[6],keys[7],keys[8],keys[9],keys[10],keys[11],keys[12],keys[13],keys[14],keys[15],keys[16],keys[17]]


plt.xlabel("types of pokemon used by trainer")

plt.ylabel("frequncey of types used")

plt.title("frequnecy of pokemon types found in trainer's teams")

plt.bar(x,
      y,
      color =color,
      edgecolor=edgecolor,
       linewidth =1)
#plt.subplot(plt.hist(level_list))
plt.show()
