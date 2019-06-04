# Space Invaders

gracz = loadImage("246x0w.png")

def setup():
    size(500,500)
    background(234,111,123)
    global gracz
    #pozycja_Gracz = (250,490)
    print(gracz)
    
    def draw():
        image(gracz, 250, 490)
