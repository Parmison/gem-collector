import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1250,690))

bg = pygame.image.load("lesson 8/images/bg gem.jpg")
purple = pygame.image.load("lesson 8/images/gem.png")
purple = pygame.transform.scale(purple,(40,40))
blue = pygame.image.load("lesson 8/images/gem_blue-removebg-preview.png")
blue = pygame.transform.scale(blue,(40,40))
evil = pygame.image.load("lesson 8/images/evil-removebg-preview (1).png")
evil = pygame.transform.scale(evil,(140,130))
collector = pygame.image.load("lesson 8/images/collector.webp")
collector = pygame.transform.scale(collector,(148,148))

font = pygame.font.SysFont("love",36)

score = 0
images = [purple,blue]
text = font.render(f"Score:{round(score,2)}",True,"white")

class Collector(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = collector
        self.rect = self.image.get_rect()

class Gem(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = random.choice(images)
        self.rect = self.image.get_rect()

class Evil(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = evil
        self.rect = self.image.get_rect()

collector_group = pygame.sprite.Group()
gem_group = pygame.sprite.Group()
evil_group = pygame.sprite.Group()

core = Collector()
collector_group.add(core)

for i in range(30):
    allgem = Gem()
    allgem.rect.x = random.randint(50,1160)
    allgem.rect.y = random.randint(50,640)
    gem_group.add(allgem)

for i in range(10):
    bad = Evil()
    bad.rect.x = random.randint(50,1160)
    bad.rect.y = random.randint(50,640)
    evil_group.add(bad)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                core.rect.y -= 4
            if event.key == pygame.K_DOWN:
                core.rect.y += 4
            if event.key == pygame.K_LEFT:
                core.rect.x -= 4
            if event.key == pygame.K_RIGHT:
                core.rect.x += 4
        
    screen.fill("black")
    screen.blit(bg,(0,0))
    screen.blit(text,(570,2))

    allgem_list = pygame.sprite.spritecollide(core,gem_group,True)
    evil_list = pygame.sprite.spritecollide(core,evil_group,True)

    for item in allgem_list:
        score +=  1
        text = font.render(f"Score:{round(score,2)}",True,"white")
    
    for item in evil_list:
        score -= 1
        text = font.render(f"Score:{round(score,2)}",True,"white")

    collector_group.draw(screen)
    gem_group.draw(screen)
    evil_group.draw(screen)

    pygame.display.update()