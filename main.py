from pandas import *
#csv file name
filename = "C:\\Users\\Student 2021\\Desktop\\tsw\\CS PROJECT\\Pokemon.csv"


data = read_csv(filename)

ids = data["trainerID"].tolist()
name= data["name"].tolist()



# zip the two lists together to create a list of key-value pairs
key_value_pairs = zip(ids, name)

# convert the list of key-value pairs to a dictionary
data = dict(key_value_pairs)

keys = list(data.keys())

for i in range(len(data)):
 with open("test.txt","a+") as f :
  f.write("\n"+ keys[i],data[i])
  
#print(keys)