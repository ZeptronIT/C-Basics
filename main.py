import random
import math
from pygame import mixer
import pygame

# Intialize the pygame
pygame.init()

# Fenster in Pixel (x, y (Achse))
screen = pygame.display.set_mode((800, 600))

# Hintergrund
background = pygame.image.load('Background.jpg')

mixer.music.load('background.wav')
mixer.music.play(-1)

# Name und Bild
pygame.display.set_caption("Finda")
icon = pygame.image.load('Biene.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('bee.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('Enemy.png'))
    enemyX.append(random.randint(0, 800))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)



# Ready - Du kann die Patrone nicht auf dem Bildschirm sehen
# Fire - Die Patrone bewegt sich gerade

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 150
bulletX_change = 0
bulletY_change = 5
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('Beyond Wonderland.ttf',70)
textX = 10
textY = 10


#over_font = pygame.font.Font('Beyond Wonderland.ttf',64)

def show_score(x,y):
    score = font.render("Score : " + str(score_value),True,(255, 255, 255))
    screen.blit(score, (x, y))
#def game_over_text(x, y):
    #over_text = over_font.render("GAME OVER",True,(255,255,255))
    #screen.blit(over_text, (x, y))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i ):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollission(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + math.pow(enemyY-bulletY,2))
    if distance < 27:
        return True
    else:
        return False

running = True
while running:

    # Farben
    screen.fill((0, 0, 0))

    # Hintergrund
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.4
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.4
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_Sound = mixer.Sound('rt-music_c81h6zot9-1667400276-0_converted-12-Gauge-Pump-Action-Shotgun-Close-Gunshot-A-www.fesliyanstudios.com.wav')
                    bullet_Sound.play()
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Border

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736


    #  Enemy Border/Movement
    for i in range(num_of_enemies):

            # if enemyY[i] > 440:
            # for j in range(num_of_enemies):
                # #enemyY[j] = 2000
            #game_over_text(200, 250)
            #break


        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]

        collision = isCollission(enemyX[i], enemyX[i], bulletX, bulletY)
        if collision:
            explosion_Sound = mixer.Sound('explosion.wav')
            explosion_Sound.play()
            explosion_Sound = mixer.Sound('MyGameGameOverSouund.wav')
            explosion_Sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            print(score_value)
            enemyX[i] = random.randint(0, 800)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(playerX, bulletY)
        bulletY -= bulletY_change


    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()



