class Person:
    def __init__(self, name):
        self.name = name
        
    
    def __repr__(self):
        return f"Person('{self.name}')"
    
# Person("Monal")