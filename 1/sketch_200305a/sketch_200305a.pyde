def setup():
    size(800, 800)
    background(255,255,0)
    rectMode(RADIUS)
    
def draw():
    rect(width/2,height/2,200,200)
    if mousePressed:
       rect(width/2,height/2,300,300)
    else:
        clear()    
