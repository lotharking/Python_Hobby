class potencia:
    def __init__(self, x,y):
        self.x=x
        self.y=y
        self.cont=1
        self.mult=1
    def multiplication(self):
        self.mult*=self.x
        if self.cont==self.y:
            self.mostrar()
        else:
            self.cont+=1
            self.multiplication()
    def mostrar(self):
        print(self.mult)

potencia(5,3).multiplication()
