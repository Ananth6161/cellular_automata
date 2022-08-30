class cell():
    def __init__(self,i,j,x,rule):
        self.i=i
        self.j=j
        self.x=x
        self.rule=rule
    def toggle(self):
        if(self.x==0):
            self.x=1
        else:
            self.x=0
