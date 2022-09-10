#create a Maze game!
from pygame import *


#TODO create a Character class
class Character(sprite.Sprite):
    #TODO create init function takes in x, y, width, height, speed
    def __init__ (self, img_file, x, y, width, height, speed):
        super().__init__() #TODO create the sprite.Sprite class first
        self. image = transform.scale(image.load(img_file), (width, height))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = speed

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#TODO create Player class derived from Character
class Player(Character):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= self.speed
        if keys[K_RIGHT]:
            self.rect.x += self.speed
        if keys[K_DOWN]:
            self.rect.y += self.speed
        if keys[K_UP]:
            self.rect.y -= self.speed

#TODO create Enemy class derived from Character class
class Enemy(Character):
    def update(self):
        if self.rect.x <= 470:
            self.side = "right"
        if self.rect.x >= win_width - 85:
            self.side = "left"

        if self.side == "left":
            self.rect.x -= self.speed
        if self.side == "right":
            self.rect.x += self.speed

#TODO create Wall class derived from sprite.Sprite class
class Wall (sprite.Sprite):
    def __init__(self, width, height, xcor, ycor, color):
        super().__init__() #TODO create the sprite.Sprite class first
        self.image = Surface((width, height))
        self.image.fill(color) # * color is a set of 3 numbers (red, green, blue)

        self.rect = self.image.get_rect()
        self.rect.x = xcor
        self.rect.y = ycor

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



#game scene
win_width = 700



#game characters
hero = Player("hero.png", 50, 50, 50, 50, 2)
#width, height, xcor, ycor, color
wall1 = Wall(10, 100, 100, 0, (0,0,0)) # (0, 0 , 0) is black is black, (0, 0, 255 is blue)
wall2 = Wall(10, 200, 100, 300, (0, 0, 0))
wall3 = Wall(10, 300, 200, 100, (0, 0, 0))
wall4 = Wall(10, 100, 300, 0, (0, 0, 0))
wall5 = Wall(10, 350, 300, 200, (0, 0, 0))
wall6 = Wall(10, 400, 400, 0, (0, 0, 0))
wall7 = Wall(100, 10, 400, 400, (0, 0, 0))
wall8 = Wall(100, 10, 500, 300, (0, 0, 0))
wall9 = Wall(100, 10, 400, 200, (0, 0, 0))
wall10 = Wall(100, 10, 500, 100, (0, 0, 0))
wall11 = Wall(10, 400, 600, 100, (0, 0, 0))

enemy = Enemy("cyborg.png", 100, 100, 50, 50, 1)
enemy2 = Enemy("cyborg.png", 100, 200, 50, 50, 1)

#x, y, width, height, speed
treasure = Character("treasure.png", 630, 450, 50, 50, 1)

wall_list = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11]
wall_group = sprite.Group()
for wall in wall_list:
    wall_group.add(wall) #TODO group all Wall into a group

# #TODO create treasure from Character class using "treasure.png" file
# treasure = Character("treasure.png", 400, 400, 50, 50, 0)

font.init()
font1 = font.Font(None, 50)
win = font1.render("You win!", True, (0, 0 , 0))
lose = font1.render("You lose!", True, (0, 0, 0))

window = display.set_mode((700, 500))
display.set_caption("Maze Game")

background = \
    transform.scale(
        image.load("background.jpg"),    
        (700, 500)
    )


game = True

#music
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
kick = mixer.Sound('kick.ogg')
kick.play()

treasure_list = [treasure]
treasure_group = sprite.Group()
for treasure in treasure_list:
    treasure_group.add(treasure) #TODO group all treasure into a group

while game:
    window.blit(background,(0, 0)) #draw the background
    hero.draw()
    enemy.draw()
    hero.update()
    enemy.update()
    treasure.draw()

    wall_group.draw(window)

    for e in event.get():
        if e.type == QUIT:
            game = False



    if sprite.spritecollide(hero, wall_group, True):
        window.blit(lose, (350, 200))
        game = False

    if sprite.spritecollide(hero, treasure_group, True):
        window.blit(win, (350, 200))
        game = False


    display.update()


