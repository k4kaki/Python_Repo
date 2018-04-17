class LenError(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return str(self.value)
        
class range_():
    def __init__(self,val):
        self.val=val
    def check_length(self):
        try:
            if len(self.val) > 10:
                raise LenError("Then number you enterd 10 char length")
            print("Yor values is:",self.val)
            return ''
        except LenError as e:
            print(e)
            return ''
p1=range_('SanjeevaKa')
print(p1.check_length())
