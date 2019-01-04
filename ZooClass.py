class Zoo:
    name = "This is a Zoo."
    def __init__(self,zooname,timings,max_animals,exhibits):
        self.zooname = zooname
        self.timings = timings
        self.max_animals = max_animals
        self.exhibits = exhibits
        self.animals = {}

    def addAnimal(self,animal_name,number):
      
       self.animals[animal_name] = number
       print(self.animals)
        
    def removeAnimal(self,animal_name):
        del self.animals [animal_name]
        print (self.animals)

