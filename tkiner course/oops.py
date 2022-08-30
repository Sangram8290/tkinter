


# from concurrent.futures.thread import _worker


# class Information:
#     num_workers=8

#     def __init__(self,aname,age,work) :
#         self.name=aname
#         self.age=age
#         self.work=work

#     def printname(self):
#         return f"Worker name is {self.name} and age is {self.age} work is {self.work}"
#     @classmethod
#     def change_worker(cls,newworker):
#         cls.num_workers=newworker

#     @classmethod
#     def from_dash(cls,string):
#         # x=string.split("-")
#         # print(x)
#         # return cls (x[0],x[1],x[2])
#         return cls(*string.split("-"))
#     @staticmethod
#     def printgood(string):
#         print("this is good"+string)

# worker=Information("ram",26,"helper") 

# shyam=Information.from_dash("shyam-32-clint")
# print(shyam.age)
# worker.printgood(" boss")
# worker.change_worker(6)
# print(worker.name)
# print(worker.age)
# print(worker.printname())
# print(Information.num_workers)



# Single line inheritance----------------------/////////////////////////

# class Information:
#     num_workers=8

#     def __init__(self,aname,age,work) :
#         self.name=aname
#         self.age=age
#         self.work=work

#     def printname(self):
#         return f"Worker name is {self.name} and age is {self.age} work is {self.work}"
#     @classmethod
#     def change_worker(cls,newworker):
#         cls.num_workers=newworker

#     @classmethod
#     def from_dash(cls,string):
#         # x=string.split("-")
#         # print(x)
#         # return cls (x[0],x[1],x[2])
#         return cls(*string.split("-"))
#     @staticmethod
#     def printgood(string):
#         print("this is good"+string)

# class timing(Information):
#     work_hours = 12    

#     def __init__(self,aname,age,work,hour) :
#      self.name=aname
#      self.age=age
#      self.work=work
#      self.hour=hour
#     def printtime(self):
#         return f"Worker name is {self.name} and age is {self.age} work hour is {self.hour}" 

# worker=timing("ram",26,12,"helper") 
# shyam=Information.from_dash("shyam-32-clint")

# karan=timing("ram",26,"helper",12) 
# print(karan.printtime())



# Multiline inheritance -------------------------///////////////////


# class Information:
#     num_workers=8

#     def __init__(self,aname,age,work) :
#         self.name=aname
#         self.age=age
#         self.work=work

#     def printname(self):
#         return f"Worker name is {self.name} and age is {self.age} work is {self.work}"
#     @classmethod
#     def change_worker(cls,newworker):
#         cls.num_workers=newworker

#     @classmethod
#     def from_dash(cls,string):
#         # x=string.split("-")
#         # print(x)
#         # return cls (x[0],x[1],x[2])
#         return cls(*string.split("-"))
#     @staticmethod
#     def printgood(string):
#         print("this is good"+string)

# class timing:
#     work_hours = 12    

#     def __init__(self,aname,age) :
#      self.name=aname
#      self.age=age
  
#     def printtime(self):
#         return f"Worker name is {self.name} and age is {self.age} " 


# class Coolworker(Information,timing):

#     who="Always complete task"

#     def printwho(self):
#         print(self.who)


# worker=timing("ram",26) 
# shyam=Information.from_dash("shyam-32-clint")

# karan=timing("ram",26) 
# print(karan.printtime())

# ram=Coolworker("ram","Always complete task",23)
# div=ram.printtime()
# print(div)



# Multilevel Inheritance -----------------////////////////////

# class Electronic_devices:
#     device = "machine"


# class Poket_gadgets(Electronic_devices):
#     gadget1 = "mobile"
#     gadget2="watch"    
    
#     def gadget(self):
#         return f" My {self.gadget1} is too good "

# class phone(Poket_gadgets):
#     brand="Apple"
#     brand2="oppo"
#     brand3="vivo"

#     def gadget(self):
#         return f" My {self.gadget1} is too good and it's company is {self.brand} "


# x=Electronic_devices()
# y=Poket_gadgets()
# z=phone()

# print(y.gadget())        
# print(z.device) 





class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


hindustani_supporter = Employee("Hindustani", "Supporter")
# nikhil_raj_pandey = Employee("Nikhil", "Raj")

print(hindustani_supporter.email)

hindustani_supporter.fname = "US"

print(hindustani_supporter.email)
hindustani_supporter.email = "this.that@codewithharry.com"
print(hindustani_supporter.fname)

del hindustani_supporter.email
print(hindustani_supporter.email)
hindustani_supporter.email = "Harry.Perry@codewithharry.com"
print(hindustani_supporter.email)
