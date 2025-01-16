    # """
    
    
    # single inheritence
    # """
    
    
# class parent():
#     def ouput(self):
#         print("i am the parent")

# class child(parent):
#     def ouputc(self):
#         print("i am the child")



# c = child()
# c.ouputc()
# c.ouput()
# p = parent()
# p.ouput()



# class father():
#     def outputf(self):
#         print("i am your father")


# class mother():
#     def outputm(self):
#         print("i am your mother")
        
        
# class child(father, mother):
#     def outpu(self):
#         print("i am your child")
        
        
# c = child()
# c.outputm()




# class father():
#     def outputf(self):
#         print("i am your father")
        
# class childq(father):
#     def child1out(self):
#         print("i am the child1")
# class child2(father):
#     def child1out(self):
#         print("i am the child2")
        
        


# Object
# can create any no of ojects for class
# memory is allocated when oject is created

# sysntax : Object name = classname()
# using ibject we can access methods and variables
# syntax = objectname.mehots(), objectname.variable()
# class a():
#   class body



# b = a() --> object creating


# class Student():
#     a= 3
#     print(a)



# class cal():
#     a=2
#     def output(self):
#         print(self.a) 
        

# b = cal()
# b.output()


# Encapsulation
# wrappping of variable and methods into a single unit
# accesss specifiers
# public, private, prtected


# Pl=olymorphosm
# many forms

## Data abstraction
# Hiding of information




"""
# Encapsulation
# wrappping of variable and methods into a single unit
public
private __
protected _ 
"""



# class demo():
#     def __init__(self,a,b):
#         self.__a=a # private
#         self._b =b # protected
    


# class demo2(demo):
#     def output(self):
#         print(self._b)
        
# c = demo2(13,14)
# c.output()


# import time


# def connect() -> None:
#     print('Connecting to internet...')
#     time.sleep(5)
#     print("you are connected")
    
    
    
# if __name__ == "__main__" : 
#     connect()       
    
    

# def greet() -> None:
#     print('Hellp world')
    
# def bye() -> None:
#     print("Bye, World")
    
# def main() -> None:
#     greet()
#     bye()
    
    
# if __name__ == "__main__":
#     main()
    
    

# def enter_club(name: str, age: int, has_id: bool) -> None:
#     if name.lower() == 'bob':
#         print( "get out of ther bob, we dont wnat to trouble")
#         return
    
#     if age>=21  and has_id:
#         print("you may enter the club")
#     else:
#         print(" you many not enter the lclub")
        
        
# def main() -> None:
#     enter_club('Bob', 29, has_id =True)
#     enter_club('Jame', 29, has_id =True)
#     enter_club('Bob', 29, has_id =True)
#     enter_club('Bob', 29, has_id =True)
    
    

# def is_an_adult(ae:int, has_id: bool) -->bool:
    
    
    
    

# number: int = 10.0 


# Tyoe annnotation
def upper_everything(elements:list[str]) -> list[str]:
    return [ elem.upper() for element in elements]

    
    
sample : list[int] = ['a',1,3,'b']


# list comprehension


