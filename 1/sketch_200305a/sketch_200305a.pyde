def setup():
    size(800, 800)
    background(255,255,0)
    rectMode(RADIUS)
    
def draw():
    # rect(width/2,height/2,200,200) # nie jest potrzebny, bo w tej samej klace zakrywasz go większym lub kasujesz - mniej działań dla programu ten sam efekt to tzw. optymalizacja
    if mousePressed:
       rect(width/2,height/2,300,300)
    else:
        clear()
# brakuje mi jeszcze użycia współrzędnych myszy
# 1,75pkt
