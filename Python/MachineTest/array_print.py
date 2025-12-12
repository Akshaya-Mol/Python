import random
name_list = [{
    "id":1,
    "name":"rajesh"
},
{
 "id":2,
    "name":"rahul"
},
{
"id":3,
    "name":"sruthi"
}
]
print(len(name_list))

id = random.randint(1,len(name_list))

for x in name_list:
    if x["id"]== id:
        print("Student Name:", x["name"])
