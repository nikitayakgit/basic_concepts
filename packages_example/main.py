# main.py
#import mypackage
#import mypackage.module1  
#import mypackage.module2
#mypackage.module1.greet("Pythonista")
#mypackage.module2.depart("Pythonista")



#from mypackage import module1 as m1, module2 as m2  
#m1.greet("Pythonista")
#m2.depart("Pythonista")

#from mypackage.module1 import greet
#from mypackage.module2 import depart 
#greet("Pythonista")
#depart("Pythonista")


from mypackage.module1 import greet
from mypackage.module2 import depart
from mypackage.mysubpackage.module3 import people

for person in people:
    greet(person)
    depart(person)
