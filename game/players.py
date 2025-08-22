class Player:
    
    def __init__(self,name):
        self.name=name
        self.Marks=0
        
    def assignMarks(self,p_1,p_half,p_minushalf,p_minus1):
        addedMarks=(p_1+0.5*p_half-0.5*p_minushalf-p_minus1)
        self.Marks+=addedMarks