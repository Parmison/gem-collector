import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1210,690))

bg = pygame.image.load("lesson 8/images/bg.png")
bin = pygame.image.load("lesson 8/images/bin.png")
bin = pygame.transform.scale(bin,(50,89))
box = pygame.image.load("lesson 8/images/box.png")
paper_bag = pygame.image.load("lesson 8/images/paper bag.png")
paper_bag = pygame.transform.scale(paper_bag,(40,60))
pencil = pygame.image.load("lesson 8/images/pencil.png")
plastic_bag = pygame.image.load("lesson 8/images/plastic bag.png")
plastic_bag = pygame.transform.scale(plastic_bag,(40,60))

font = pygame.font.SysFont("Times New Roman",36)

score = 0
images = [box,paper_bag,pencil]
text = font.render(f"Score:{round(score,2)}",True,"white")

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = bin
        self.rect = self.image.get_rect()

class Recycle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = random.choice(images)
        self.rect = self.image.get_rect()

class Plastic_bag(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = plastic_bag
        self.rect = self.image.get_rect()

binn = pygame.sprite.Group()
recycle = pygame.sprite.Group()
plastic = pygame.sprite.Group()

Binn = Bin()
binn.add(Binn)

for i in range(20):
    Rtrash = Recycle()
    Rtrash.rect.x = random.randint(50,1160)
    Rtrash.rect.y = random.randint(50,640)
    recycle.add(Rtrash)

for i in range(20):
    trash = Plastic_bag()
    trash.rect.x = random.randint(50,1160)
    trash.rect.y = random.randint(50,640)
    plastic.add(trash)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Binn.rect.y -= 4
            if event.key == pygame.K_DOWN:
                Binn.rect.y += 4
            if event.key == pygame.K_LEFT:
                Binn.rect.x -= 4
            if event.key == pygame.K_RIGHT:
                Binn.rect.x += 4
        
    screen.fill("black")
    screen.blit(bg,(0,0))
    screen.blit(text,(570,2))

    Rtrash_list = pygame.sprite.spritecollide(Binn,recycle,True)
    trash_list = pygame.sprite.spritecollide(Binn,plastic,True)

    for item in Rtrash_list:
        score +=  1
        text = font.render(f"Score:{round(score,2)}",True,"white")
    
    for item in trash_list:
        score -= 1
        text = font.render(f"Score:{round(score,2)}",True,"white")

    binn.draw(screen)
    recycle.draw(screen)
    plastic.draw(screen)

    pygame.display.update()