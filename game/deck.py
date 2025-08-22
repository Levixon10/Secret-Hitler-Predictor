#deck.py 
class Deck:
    def __init__(self,liberal,fascist):
        self.liberalRem=liberal
        self.fascistRem=fascist

    def change(self,passedLaw,diff):
        if(passedLaw=='F'):
            self.fascistRem+=diff
        else:
            self.liberalRem+=diff

        
