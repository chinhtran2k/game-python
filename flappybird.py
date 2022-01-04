import pygame
from random import randint
pygame.init()
screen=pygame.display.set_mode((400,600))
pygame.display.set_caption('flappy bird')
clock = pygame.time.Clock()
backgroup_imp=pygame.image.load('D:/Users/PC/Downloads/background.png')
backgroup_imp=pygame.transform.scale(backgroup_imp,(400,600))
bird_img=pygame.image.load('D:/Users/PC/Downloads/bird2.png')
bird_img=pygame.transform.scale(bird_img,(35,35))

tube_img=pygame.image.load('D:/Users/PC/Downloads/tube.png')

tube_op_img=pygame.image.load('D:/Users/PC/Downloads/tube_op.png')

song=pygame.mixer.Sound('D:/Users/PC/Downloads/no6.wav')
white=(255,255,255)
#tọa độ con chim
bird_x=50
bird_y=350

#tọa độ của ống
tube1_x=400
tube2_x=600
tube3_x=800

tube_width=50
tube1_hieght=randint(100,400)
tube2_hieght=randint(100,400)
tube3_hieght=randint(100,400)
d_tube=200
#vận tốc ban đầu và trọng lực
velocity=0
gravity=0.5

tube_velocity=2
score = 0

tube1_pass = False
tube2_pass = False
tube3_pass = False
tube4_pass=False

font = pygame.font.SysFont('sans', 30)
font1 = pygame.font.SysFont('sans', 40)
BLACK = (0, 0, 0)

pausing=False
plus=1
running=True
while running:
    pygame.mixer.Sound.play(song)#chạy âm thanh
    clock.tick(60)
    screen.fill(white)
    screen.blit(backgroup_imp,(0,0))
#vẽ con chim
    bird=screen.blit(bird_img,(bird_x,bird_y))
#vẽ ống trên
    tube1_img=pygame.transform.scale(tube_img,(tube_width,tube1_hieght))
    tube1=screen.blit(tube1_img,(tube1_x,0))
    tube2_img = pygame.transform.scale(tube_img, (tube_width, tube2_hieght))
    tube2 = screen.blit(tube2_img, (tube2_x, 0))
    tube3_img = pygame.transform.scale(tube_img, (tube_width, tube3_hieght))
    tube3 = screen.blit(tube3_img, (tube3_x, 0))
# vẽ ống đối diện
    tube1_op_img = pygame.transform.scale(tube_op_img, (tube_width,600-( tube1_hieght+d_tube)))
    tube_op1 = screen.blit(tube1_op_img, (tube1_x, tube1_hieght+d_tube))
    tube2_op_img = pygame.transform.scale(tube_op_img, (tube_width,600-( tube2_hieght+d_tube)))
    tube_op2 = screen.blit(tube2_op_img, (tube2_x, tube2_hieght+d_tube))
    tube3_op_img = pygame.transform.scale(tube_op_img, (tube_width,600-( tube3_hieght - d_tube)))
    tube_op3 = screen.blit(tube3_op_img, (tube3_x, tube3_hieght+d_tube))
#di chuyển ống sang trái
    tube1_x-=tube_velocity
    tube2_x -= tube_velocity
    tube3_x -= tube_velocity

    if tube1_x<-tube_width:
        tube1_x=550
        tube1_hieght=randint(100,400)
        tube1_pass=False
    if tube2_x < -tube_width:
        tube2_x = 550
        tube2_hieght = randint(100, 400)
        tube2_pass = False
    if tube3_x < -tube_width:
        tube3_x = 550
        tube3_hieght = randint(100, 400)
        tube3_pass = False
#vẽ biến điểm
    score_txt = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_txt, (0, 0))

#tính điểm
    if tube1_x + tube_width <= bird_x and tube1_pass == False:
        score += 1
        tube1_pass = True
    if tube2_x + tube_width <= bird_x and tube2_pass == False:
        score += 1
        tube2_pass = True
    if tube3_x + tube_width <= bird_x and tube3_pass == False:
        score += 1
        tube3_pass = True

#di chuyển con chim duoi xuống

    bird_y+=velocity
    velocity+=gravity

#kiểm tra va chạm
    for tube in [tube1,tube2,tube3,tube_op1,tube_op2,tube_op3]:
        if bird.colliderect(tube) or bird_y > 600:#kiểm tra con chim vói ống
            pygame.mixer.pause()#dừng âm thanh
            velocity=0
            tube_velocity=0
            game_over_txt=font1.render("Game over !!! score: "+str(score),True,BLACK)
            screen.blit(game_over_txt,(30,250))
            game_over_txt = font1.render("press Space to continue!!!", True, BLACK)
            screen.blit(game_over_txt, (30, 290))
            pausing=True#dừng

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            velocity=0
            velocity-=7
        if pausing:
            pygame.mixer.unpause()#chay âm nhanh
            bird_x=50
            bird_y=350
            tube1_x=400
            tube2_x=600
            tube3_x=800
            tube_velocity=2
            score=0
            pausing=False

    pygame.display.flip()
pygame.quit()