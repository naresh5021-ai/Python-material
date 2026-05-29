
class animal:
    x=0
    
    def __init__(self):
        print('I am constructed')
    
    def part(self):
        self.x=self.x+1
        print('so far',self.x)
        
    def __del__(self):
        print('I am destructed')

an=animal()
an.part()
an.part()
an=42
print('an contains',an)