class Dog:
    
    species = "doooog"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    
    def speak(self, sound):
        print(f"{self.name} says {sound}")

class Bulldog(Dog):
    pass

class JackRusselTerrier(Dog):
    
    def speak(self, sound = "Aarf"):
        return super().speak(sound)

    
    
class Dachshund(Dog):
    pass


        
buddy = JackRusselTerrier("stink", 33)
jim = Bulldog("Bob", 5)

jim.speak("Awoga")


print(buddy)
buddy.speak("Grr")
