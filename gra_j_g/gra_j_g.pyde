# Space Invaders
def setup():
    size(500,500)
    background(0)
    skorka= "zabity"
    
# szkic klasy przeciwnika
class Przeciwnik():
    def __init__ (self, pozycja):
        self.pozycja=pozycja
    def __init__ (self, rozmiar):
        self.rozmiar=rozmiar
    def __init__ (self, przesun):
        self.przesun=przesun
    def __init__ (self, wyglad):
        self.wyglad=skorka
    def __init__ (self, zycie):
        self.zycie=1
        
def draw():
    def zmien_wyglad(skorka):
        global wyglad
        wyglad = skorka

    zmien_stroj("atak")
    zmien_stroj("zabity")
