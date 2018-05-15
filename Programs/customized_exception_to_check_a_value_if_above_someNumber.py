class ValError(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return str(self.value)
        
class range_():
    def __init__(self,val):
        self.val=val
    def check_range(self):
        try:
            if self.val > 100:
                raise ValError("Then number you enterd above 100")
            print("Yor values is:",self.val)
            return ''
        except ValError as e:
            print(e)
            return ''
p1=range_(101)
print(p1.check_range())
