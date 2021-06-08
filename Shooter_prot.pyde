click = 0
velX = 3
velY = 3

def setup():
    size(800, 600)
    background(50)
    rectMode(CENTER)
    global targetX, targetY, targetSize
    targetX = 400
    targetY = 300
    targetSize = 100
    
def draw():
    global click, targetX, targetY, targetSize, velX, velY

    background(50)

    fill(255)
    square(targetX, targetY, targetSize)
    
    if click > 0:
        fill(255, 100, 100, 100)
        click += 1
        if (targetX-targetSize/2)<mouseX<(targetX+targetSize/2) and (targetY-targetSize/2)<mouseY<(targetY+targetSize/2) and click<30:
            square(targetX, targetY, targetSize)
    else:
        fill(255, 100)
        
    circle(mouseX, mouseY, 25)
    
    if click > 60:    
        click = 0
        
    targetX += velX
    if targetX<=0+(targetSize/2) or targetX>=width-(targetSize/2):
        velX = velX*(-1)
        
    targetY += velY
    if targetY<=0+(targetSize/2) or targetY>=height-(targetSize/2):
        velY = velY*(-1)
        
    print(click)
    
def mousePressed():
    global click
    if click == 0:
        click = 1
