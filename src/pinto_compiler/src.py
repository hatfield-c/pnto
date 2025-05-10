
class Main:
    def __init__(self):
        self.a = [ 0, 1, 2, 3 ]
        self.b = [ "0", "1", "2", "3" ]
        self.c = { 4, 5 }
        self.d = { "4", "6" }
    
    def Run(self):
        self.b[1] = 9
        self.c[0] = self.a[1]
