class Ruler:
    president=None
    chancellor=None
    
    @classmethod
    def voting(cls,president, chancellor):
        cls.president = president
        cls.chancellor = chancellor