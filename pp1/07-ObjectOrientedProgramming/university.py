class University():
    
    def __init__(self, name):
        self.name = name 
    
    def __str__(self):
        return self.name
    
my_university = University('UEK Kraków')
print(my_university)      
