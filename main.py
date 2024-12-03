from pandas import *
#csv file name
filename = "C:\\Users\\Student 2021\\Desktop\\tsw\\CS PROJECT\\Primary-energy-by-fuel.csv"


data = read_csv(filename)

years = data["Primary energy by fuel"].tolist()
oil = data["Oil"].tolist()
renewable = data["Renewables"].tolist()
gas = data["Gas"].tolist()
coal = data["Coal"].tolist()
print(years)
print(oil)