from pandas import *
#csv file name
filename = "C:\\Users\\student\\Documents\\GitHub\\leaving-cert-project\\Pokemon.csv"


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
#print(types)
import matplotlib.pyplot as plt

y = [types[keys[0]],types[keys[1]],types[keys[2]],types[keys[3]],types[keys[4]],types[keys[5]],types[keys[6]],types[keys[7]],types[keys[8]],types[keys[9]],types[keys[10]],types[keys[11]],types[keys[12]],types[keys[13]],types[keys[14]],types[keys[15]],types[keys[16]],types[keys[17]]]
x = [keys[0],keys[1],keys[2],keys[3],keys[4],keys[5],keys[6],keys[7],keys[8],keys[9],keys[10],keys[11],keys[12],keys[13],keys[14],keys[15],keys[16],keys[17]]
#y= [3,7,8,7,1,3]
print(y)
plt.xlabel("types")
plt.ylabel("frequncey")
plt.bar(x,y)
plt.show()

