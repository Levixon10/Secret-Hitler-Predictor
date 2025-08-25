#deck.py 
class Deck:
    def __init__(self,liberal,fascist):
        self.liberalRem=liberal
        self.fascistRem=fascist
        self.Rem=fascist+liberal

    def change(self,passedLaw,diff):
        if(passedLaw=='F'):
            self.fascistRem+=diff
            self.Rem+=diff
        else:
            self.liberalRem+=diff
            self.Rem+=diff

        
