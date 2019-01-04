from ZooClass import Zoo
zoo1 = Zoo("California Zoo","9:00 am to 5:00 pm","50 animals","20 exhibits")
zoo2 = Zoo("Oregon Zoo","8:00 am to 4:00 pm","30 animals","15 exhibits")

zoo1.addAnimal("giraffe",10)

print (zoo1.zooname)
print(zoo1.timings)
print (zoo1.max_animals)
print (zoo1.exhibits)
print (" ")
print (zoo2.zooname)
print(zoo2.timings)
print (zoo2.max_animals)
print (zoo2.exhibits)
print (" ")
