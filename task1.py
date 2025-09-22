fruits =["apple","orange","mango"]
vegetables=["carrot","beans","chilli"]
beverages=["coke","shake","lime","Water"]

fruits.append("guava")
print(fruits)

vegetables.insert(2,"beetroot")
print(vegetables)

beverages.pop()
print(beverages)

inventory = fruits+vegetables+beverages
print(inventory)

print(fruits[:2])

print(vegetables[-1])

listcom=[len(x) for x in fruits]
print(listcom)

print("Water" in beverages)

my_tuple=(fruits[0],vegetables[0],beverages[0])
print(my_tuple)

Python ={"Achu","mol","varun","vishnu","tharun"}
DataScience = {"kannan","rj","koushi","Achu","varun"}

Python.add("hari")
print(Python)

DataScience.remove("koushi")
print(DataScience)

print(Python & DataScience)
print(Python - DataScience)
print(Python|DataScience)

course={
    "Python": 2,
    "React":5,
    "Java": 7
}

for x,y in course.items():
    print("Course:",x,", Students:",y)

doubleCourse = { x: y+y for x,y in course.items()}
print(doubleCourse)

