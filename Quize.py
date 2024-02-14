#list=[["khan",1],["luama9",2],["luaman",3]]
#dict1=dict(list)

#for item in  dict1:
 #   print(item)

list=["kham","luama9",1,3,5,6,8.0,23,59,65,456,4676]

for item in list:
    if str(item).isnumeric() and item>6:
        print(item)