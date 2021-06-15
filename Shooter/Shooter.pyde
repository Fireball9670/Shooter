score = 0
start = 0
timer = 15*60

class target(object):
    def __init__(self, targetX, targetY, targetSize, velX, velY, pic):
        self.targetX = targetX
        self.targetY = targetY
        self.targetSize = targetSize
        self.velX = velX
        self.velY = velY
        self.pic = pic
        
    #targets have X- and Y-coodinates, size velocity and an image file
    
def bounce(object):
    if object.targetX<=0+(object.targetSize/2) or object.targetX>=width-(object.targetSize/2):
            object.velX = object.velX*(-1)
            
    if object.targetY<=0+(object.targetSize/2) or object.targetY>=height-(object.targetSize/2):
            object.velY = object.velY*(-1)
            
    #hitting a wall reflects the object
            
def refill(item):
    if len(item) == 0:
        for x in range(10):
            c = random(-3, 3)
            d = random(-3, 3)
            newTarget = target(400, 300, 100, c, d, targetImage)
            item.append(newTarget)
    
    #refills the targets if they are cleared
    
def setup():
    global crosshair, targetImage, targets, western
    size(800, 600, P2D)
    western = loadImage("Western.jpg")
    f = loadFont("Algerian-48.vlw")
    textFont(f)
    background(western)
    textAlign(CENTER)
    rectMode(CENTER)
    shapeMode(CENTER)
    targets = []
    targetImage = loadShape("Target2.svg")
    crosshair = loadShape("Crosshair.svg")
    
    #the images get loaded
    
def draw():
    global crosshair, targets, western, start, timer
    
    noCursor()
    
    background(western)
    
    textAlign(RIGHT)
    fill(200,50,100)
    textSize(15)
    text("by Malinda Riebenstahl and Henri Wagener", 775, 575)
    
    if start == 0:
        textAlign(CENTER)
        fill(255, 100)
        rect(400, 280, 720, 280) 
        textSize(50)
        fill(200,50,100)
        text("Wild West Saloon Shooting", 400, 200)
        textSize(40)
        text("Gunfighters of America", 400, 300)
        text("-Click to Start-", 400, 400)
        
        shape(crosshair, mouseX, mouseY, 80, 80)
        
    else:
        if timer>0:
            refill(targets)
    
            fill(255, 100, 100)
            textSize(32)
            textAlign(LEFT)
            text("Score:"+str(score), 50, 50)
            textAlign(RIGHT)
            text("Timer:"+str(timer/60), 750, 50)

            fill(255)
    
            for any in targets:
                shape(any.pic, any.targetX, any.targetY, any.targetSize, any.targetSize)
                any.targetX += any.velX
                any.targetY += any.velY
                bounce(any)
        
            shape(crosshair, mouseX, mouseY, 80, 80)
        
            timer = timer - 1
            
        else:
            start = -1
            textAlign(CENTER)
            fill(255, 100)
            rect(400, 280, 720, 280) 
            textSize(50)
            fill(200,50,100)
            text("Wild West Saloon Shooting", 400, 200)
            textSize(40)
            text("Gunfighters of America", 400, 300)
            text("Your score:"+str(score), 400, 400)
        
            shape(crosshair, mouseX, mouseY, 80, 80)
            
    
def mousePressed():
    global targets, score, start
    if start != -1 and start != 0:
        hit = 0
        targets.reverse()
        for any in targets:
            if (dist(any.targetX, any.targetY, mouseX, mouseY)<any.targetSize/2):
                targets.remove(any)
                score += 100
                hit = 1
                break
        targets.reverse()
        if hit == 0:
            score = score - 200
    start = 1
