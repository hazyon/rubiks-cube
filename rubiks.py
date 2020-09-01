import pygame
import random

pygame.init()

clock = pygame.time.Clock()

pygame.display.set_caption("rubiks")

screenx = 900
screeny = 600

screen = pygame.display.set_mode((screenx,screeny))

startx1 = 278
starty1 = 166
xInc = 58
yInc = 33

startx2 = 568
starty2 = 199

startx3 = 394
starty3 = 397

cube = pygame.image.load('assets\\cube.png')

red1 = pygame.image.load('assets\\red1.png')
orange1 = pygame.image.load('assets\\orange1.png')
yellow1 = pygame.image.load('assets\\yellow1.png')
green1 = pygame.image.load('assets\\green1.png')
blue1 = pygame.image.load('assets\\blue1.png')
white1 = pygame.image.load('assets\\white1.png')

red2 = pygame.image.load('assets\\red2.png')
orange2 = pygame.image.load('assets\\orange2.png')
yellow2 = pygame.image.load('assets\\yellow2.png')
green2 = pygame.image.load('assets\\green2.png')
blue2 = pygame.image.load('assets\\blue2.png')
white2 = pygame.image.load('assets\\white2.png')

red3 = pygame.image.load('assets\\red3.png')
orange3 = pygame.image.load('assets\\orange3.png')
yellow3 = pygame.image.load('assets\\yellow3.png')
green3 = pygame.image.load('assets\\green3.png')
blue3 = pygame.image.load('assets\\blue3.png')
white3 = pygame.image.load('assets\\white3.png')

gray11 = pygame.image.load('assets\\gray1.png')
gray12 = pygame.image.load('assets\\gray1.png')
gray13 = pygame.image.load('assets\\gray1.png')
gray14 = pygame.image.load('assets\\gray1.png')
gray15 = pygame.image.load('assets\\gray1.png')
gray16 = pygame.image.load('assets\\gray1.png')

gray21 = pygame.image.load('assets\\gray2.png')
gray22 = pygame.image.load('assets\\gray2.png')
gray23 = pygame.image.load('assets\\gray2.png')
gray24 = pygame.image.load('assets\\gray2.png')
gray25 = pygame.image.load('assets\\gray2.png')
gray26 = pygame.image.load('assets\\gray2.png')

gray31 = pygame.image.load('assets\\gray3.png')
gray32 = pygame.image.load('assets\\gray3.png')
gray33 = pygame.image.load('assets\\gray3.png')
gray34 = pygame.image.load('assets\\gray3.png')
gray35 = pygame.image.load('assets\\gray3.png')
gray36 = pygame.image.load('assets\\gray3.png')

buttons = [[gray11,gray12,gray13],[gray14,gray15,gray16],[gray21,gray22,gray23],[gray24,gray25,gray26],[gray31,gray32,gray33],[gray34,gray35,gray36]]

buttonCoords = [[],[],[],[],[],[]]

for i in range(0,3):
    buttonCoords[0].append((startx1 + ((i-1)*xInc), starty1 - ((i+1)*yInc)))

for i in range(0,3):
    buttonCoords[1].append((startx1 + ((3+i)*xInc), starty1 - ((-i+3)*yInc)))

for i in range(0,3):
    buttonCoords[2].append((startx2 + xInc, starty2 - yInc + (i*yInc*2)))

for i in range(0,3):
    buttonCoords[3].append((startx2 - (i*xInc), starty2 + (yInc*3*2) + (i*yInc)))

for i in range(0,3):
    buttonCoords[4].append((startx3 - (i*xInc), starty3 + (yInc * 2) - (i*yInc)))

for i in range(0,3):
    buttonCoords[5].append((startx3 - (3*xInc), starty3 - (yInc * 3) - (i*yInc*2)))

def inButton(i,j):
    mousePos = getMousePos()
    coords = buttonCoords[i][j]
    if i == 0 or i == 1:
        start = coords[1] + yInc
        yRange = abs((mousePos[0] - coords[0] - 58)/58)*-66 + 66
        if start + yRange > mousePos[1] > start-yRange:
            return(True)


    if i == 2 or i == 3:
        start = mousePos[1] - coords[1]
        xBox = mousePos[0] - coords[0]
        if 0 < start < 33:
            slope = -58/33
            if start * slope + 58 < xBox < 58:
                return(True)
            
        elif 33 < start < 67:
            if 0 < xBox < 58:
                return(True)
            
        elif 67 < start < 100:
            slope = -58/33
            if 0 < xBox < start * slope + 173:
                return(True)


    if i == 4 or i == 5:
        start = mousePos[1] - coords[1]
        xBox = mousePos[0] - coords[0]
        if 0 < start < 33:
            slope = 58/33
            if 0 < xBox < slope * start:
                return(True)

        elif 33 < start < 67:
            if 0 < xBox < 58:
                return(True)

        elif 67 < start < 100:
            slope = 58/33
            if slope * start < xBox < 58:
                return(True)
            
        
    return(False)

def inRegion():
    mousePos = getMousePos()
    if mousePos[0] > 450:
        if 0 < mousePos[1] < (-33/58) * (mousePos[0] - 450) + 300:
            return(2)
        elif 900 > mousePos[1] > (33/58) * (mousePos[0] - 450) + 300:
            return(4)
        else:
            return(3)
    else:
        if 900 > mousePos[1] > (-33/58) * (mousePos[0] - 450) + 300:
            return(5)
        elif 0 < mousePos[1] < (33/58) * (mousePos[0] - 450) + 300:
            return(1)
        else:
            return(6)

    return(0)
f1 = [['r','r','r'],['r','r','r'],['r','r','r']]
f2 = [['b','b','b'],['b','b','b'],['b','b','b']]
f3 = [['y','y','y'],['y','y','y'],['y','y','y']]
f4 = [['o','o','o'],['o','o','o'],['o','o','o']]
f5 = [['g','g','g'],['g','g','g'],['g','g','g']]
f6 = [['w','w','w'],['w','w','w'],['w','w','w']]


def add(i,j,a):
    s = f[a][i][j]
    s += str(a)
    return(s)

f = [0,f1,f2,f3,f4,f5,f6]

def rotateSide(face, direc):
    if direc == 'ccw':
        n = 1
    elif direc == 'cw':
        n = 3
    faceT = [[0,0,0],[0,0,0],[0,0,0]]
    for h in range(0,n):
        for i in range(0,3):
            for j in range(0,3):
                faceT[i][j] = f[face][i][j]
        for i in range(0,3):
            for j in range(0,3):
                f[face][i][j] = faceT[j][2-i]

def rotateEdge(face,direc):
    if face == 1:
        mod = [6,2,3,5]
    elif face == 2:
        mod = [4,3,1,6]
    elif face == 3:
        mod = [5,1,2,4]
    elif face == 4:
        mod = [3,2,6,5]
    elif face == 5:
        mod = [1,3,4,6]
    elif face == 6:
        mod = [2,1,5,4]

    if direc == 'ccw':
        n = 1
    elif direc == 'cw':
        n = 3

    for h in range(0,n):
        modtemp = [f[mod[0]][0][0],f[mod[0]][0][1],f[mod[0]][0][2]]

        if face < 4:
            modtemp = [f[mod[0]][0][2],f[mod[0]][0][1],f[mod[0]][0][0]]
            
            for i in range(0,3):
                f[mod[0]][0][2-i] = f[mod[1]][i][0]

            for i in range(0,3):
                f[mod[1]][i][0] = f[mod[2]][2][i]

            for i in range(0,3):
                f[mod[2]][2][i] = f[mod[3]][i][0]

            for i in range(0,3):
                f[mod[3]][i][0] = modtemp[i]
        else:
            for i in range(0,3):
                f[mod[0]][0][i] = f[mod[1]][i][2]

            for i in range(0,3):
                f[mod[1]][i][2] = f[mod[2]][2][2-i]

            for i in range(0,3):
                f[mod[2]][2][2-i] = f[mod[3]][i][2]

            for i in range(0,3):
                f[mod[3]][i][2] = modtemp[i]

def rotateMiddle(face, direc):
    if face == 1:
        mod = [6,2,3,5]
    elif face == 2:
        mod = [4,3,1,6]
    elif face == 3:
        mod = [5,1,2,4]
    elif face == 4:
        mod = [3,2,6,5]
    elif face == 5:
        mod = [1,3,4,6]
    elif face == 6:
        mod = [2,1,5,4]

    if direc == 'ccw':
        n = 1
    elif direc == 'cw':
        n = 3

    for h in range(0,n):
        if face < 4:
            modtemp = [f[mod[0]][1][2],f[mod[0]][1][1],f[mod[0]][1][0]]

            for i in range(0,3):
                f[mod[0]][1][2-i] = f[mod[1]][i][1]

            for i in range(0,3):
                f[mod[1]][i][1] = f[mod[2]][1][i]

            for i in range(0,3):
                f[mod[2]][1][i] = f[mod[3]][i][1]

            for i in range(0,3):
                f[mod[3]][i][1] = modtemp[i]

        else:
            modtemp = [f[mod[0]][1][0],f[mod[0]][1][1],f[mod[0]][1][2]]

            for i in range(0,3):
                f[mod[0]][1][i] = f[mod[1]][i][1]

            for i in range(0,3):
                f[mod[1]][i][1] = f[mod[2]][1][2-i]

            for i in range(0,3):
                f[mod[2]][1][2-i] = f[mod[3]][i][1]

            for i in range(0,3):
                f[mod[3]][i][1] = modtemp[i]
    return()

def rotateFace(face, direc):
    rotateSide(face,direc)
    rotateEdge(face,direc)
    

def rotateCube(face,direc):
    rotateFace(face,direc)
    rotateMiddle(face,direc)
    
    
    if face < 4:
        oFace = face + 3
    else:
        oFace = face - 3
        
    for i in range(0,3):
        rotateFace(oFace,direc)

def getMousePos():
    return(pygame.mouse.get_pos())


colorCode = {'r1':red1,'r2':red2,'r3':red3,
             'o1':orange1,'o2':orange2,'o3':orange3,
             'y1':yellow1,'y2':yellow2,'y3':yellow3,
             'g1':green1,'g2':green2,'g3':green3,
             'b1':blue1,'b2':blue2,'b3':blue3,
             'w1':white1,'w2':white2,'w3':white3}


turns = random.randint(20,25)
for i in range(0,turns):
    face = random.randint(1,6)
    direc = random.randint(1,2)
    
    if direc == 1:
        direc = 'ccw'
    else:
        direc = 'cw'

    rotateFace(face,'ccw')
    print(face,direc)

running = True
heldDown = False
while running:
    p = 0
    numberDown = False
    click = False
    for event in pygame.event.get():
        if True in pygame.mouse.get_pressed():
            if not heldDown:
                click = True
            heldDown = True
        else:
            heldDown = False
        if event.type == pygame.QUIT:
            running = False
        
    if click:
        i = 0
        j = 0
        while i < 6 and p != 10:
            if inButton(i,j):
                if i == 0:
                    if j == 0:
                        rotateFace(3,'ccw')
                    if j == 1:
                        rotateMiddle(3,'ccw')
                    if j == 2:
                        rotateFace(6,'cw')
                if i == 1:
                    if j == 0:
                        rotateFace(5,'ccw')
                    if j == 1:
                        rotateMiddle(2,'cw')
                    if j == 2:
                        rotateFace(2,'cw')
                if i == 2:
                    if j == 0:
                        rotateFace(1,'ccw')
                    if j == 1:
                        rotateMiddle(1,'ccw')
                    if j == 2:
                        rotateFace(4,'cw')
                if i == 3:
                    if j == 0:
                        rotateFace(6,'ccw')
                    if j == 1:
                        rotateMiddle(3,'cw')
                    if j == 2:
                        rotateFace(3,'cw')
                if i == 4:
                    if j == 0:
                        rotateFace(2,'ccw')
                    if j == 1:
                        rotateMiddle(2,'ccw')
                    if j == 2:
                        rotateFace(5,'cw')
                if i == 5:
                    if j == 0:
                        rotateFace(4,'ccw')
                    if j == 1:
                        rotateMiddle(1,'cw')
                    if j == 2:
                        rotateFace(1,'cw')
                p = 10
            j += 1
            if j == 3:
                i += 1
                j = 0
            

        if p != 10:
            region = inRegion()
            if region == 1:
                rotateCube(3,'ccw')
            if region == 2:
                rotateCube(2,'cw')
            if region == 3:
                rotateCube(1,'ccw')
            if region == 4:
                rotateCube(3,'cw')
            if region == 5:
                rotateCube(2,'ccw')
            if region == 6:
                rotateCube(1,'cw')

    
    screen.fill((190, 190, 190))

    screen.blit(cube, (277,100))

    for i in range(0,3):
        for j in range(0,3):
            screen.blit(colorCode[add(i,j,1)], (startx1 + (xInc*(i+j)), starty1 + (yInc*(i-j))))
    
    for i in range(0,3):
        for j in range(0,3):
            screen.blit(colorCode[add(i,j,2)], (startx2 - (xInc*i), starty2 + (yInc*(i+j*2))))

    for i in range(0,3):
        for j in range(0,3):
            screen.blit(colorCode[add(i,j,3)], (startx3 - (xInc*j), starty3 - (yInc*(i*2+j))))


    for i in range(0,6):
        for j in range(0,3):
            screen.blit(buttons[i][j], buttonCoords[i][j])
   
    
    pygame.display.flip()
    clock.tick(20)

pygame.quit()
