import pygame,sys
import button as b
import random as r
from pygame.locals import *
pygame.init()

#initial set up
mainClock = pygame.time.Clock()
surf = pygame.display.set_mode((1200,800))
pygame.display.set_caption("The totally awesome text adventure game")

#player stuff
player1 = pygame.image.load("Images/characters/player.png")
p = b.player(250,380,100,player1,10)#creates a player instance in the player class

#colours
grey = ((200,200,200))
black = ((0,0,0))
white = ((255,255,255))
yellow = ((255, 255, 87))
yellow2 = ((255, 255, 160))
red = ((255,25,31))

#randomness
R3random = r.randint(1,2)

#switches
Map = False
checked1 = False
activated = False
c1 = False
c2 = False
c3 = False
c4 = False
c4a = False
c5 = False
c6 = False
c7 = False
c8 = False
blob1 = False
blob2 = False
blob3 = False
key = False

#music
start = True
general_combat = False
mini_boss = False
maze = False
final = False
final_boss = False
frog_death = False
Victory = False


def check():
    c = pygame.mixer.music.get_busy()

    if music == True:
        if c == False:
            if start == True:
                pygame.mixer.music.load('music/start.mp3')
                pygame.mixer.music.play(0,0.10)
            elif general_combat == True:
                pygame.mixer.music.load('music/general combat.mp3')
                pygame.mixer.music.play(1,0.00)
            elif mini_boss == True:
                pygame.mixer.music.load('music/mini bosses.mp3')
                pygame.mixer.music.play(1,0.00)
            elif maze == True:
                pygame.mixer.music.load('music/maze.mp3')
                pygame.mixer.music.play(0,0.15)
            elif final == True:
                pygame.mixer.music.load('music/final area.mp3')
                pygame.mixer.music.play(0,0.00)
            elif final_boss == True:
                pygame.mixer.music.load('music/final boss.mp3')
                pygame.mixer.music.play(1,0.00)
            elif frog_death == True:
                pygame.mixer.music.load('music/post final boss.mp3')
                pygame.mixer.music.play(0,0.00)
            elif Victory == True:
                pygame.mixer.music.load('music/victory.mp3')
                pygame.mixer.music.play(1,0.00)
    elif music == False:
        if c == True:
            pygame.mixer.music.unload()

#basic settings
def settings():#this is setting the variables for the settings
    global music,sound_effect,mini_me
    music = True
    sound_effect = True
    mini_me = True
    #music related ones
    

def main_menu():
    #loading images
    bg = pygame.image.load('Images/backgrounds/MenuBG.png').convert()
    img1 = pygame.image.load("Images/normal/Play_button.png").convert()
    img2 = pygame.image.load("Images/normal/MOptions_button.png").convert()
    img3 = pygame.image.load("Images/normal/Quit_button.png").convert()
    img4 = pygame.image.load("Images/backgrounds/Title3.png").convert()

    #assigning variables to a class
    play = b.buttons(150,595,img1,1)
    options = b.buttons(450,595,img2,1)
    quits = b.buttons(870,595,img3,1)
    first = True
    pygame.mouse.set_visible(True)
    
    while True:
        check()
        #loading the images on the screen
        surf.blit(bg,(0,0))
        surf.blit(bg,(0,400))
        surf.blit(img4,(150,150))

        if play.draw(surf) and first == False:#making it so that after the first go of the loop inputs can be taken
            play_menu()
        if options.draw(surf) and first == False:
            options_menu()
        if quits.draw(surf) and first == False:
            quit_menu()

        #event loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        pygame.display.update()#updates the screen
        mainClock.tick(30)#the FPS (how many times the loop is ran per second


def quit_menu():
    first = True
    bg = pygame.image.load('Images/backgrounds/MenuBG.png').convert()
    img1 = pygame.image.load("Images/normal/Yes.png").convert()
    img2 = pygame.image.load("Images/normal/no.png").convert()
    img3 = pygame.image.load("Images/backgrounds/Quit_popup.png").convert()

    yes = b.buttons(439,442,img1,1)
    no = b.buttons(650,442,img2,1)
    while True:
        check()
        surf.blit(bg,(0,0))
        surf.blit(bg,(0,400))
        surf.blit(img3,(400,200))

        if no.draw(surf) and first == False:
            main_menu()
        if yes.draw(surf) and first == False:
            pygame.quit()
            sys.exit()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        pygame.display.update()
        mainClock.tick(30)


    
def play_menu():
    first = True
    bg = pygame.image.load('Images/backgrounds/PlayBG.png').convert()
    img1 = pygame.image.load("Images/normal/new_file.png").convert()
    img2 = pygame.image.load("Images/normal/load_file.png").convert()
    img3 = pygame.image.load("Images/normal/pm_back.png").convert()

    new_file = b.buttons(375,125,img1,1)
    load_file = b.buttons(375,325,img2,1)
    back = b.buttons(375,525,img3,1)
    while True:
        check()
        surf.blit(bg,(0,0))

        if new_file.draw(surf) and first == False:
            #nf()
            scene1()
        if load_file.draw(surf) and first == False:
            lf()
        if back.draw(surf) and first == False:
            main_menu()


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        pygame.display.update()
        mainClock.tick(30)


def options_menu():
    global music,sound_effect,mini_me
    first = True

    #loading images
    bg = pygame.image.load('Images/backgrounds/OptionsBG.png').convert()
    bg2 = pygame.image.load("Images/backgrounds/Options2BG.png").convert()
    img1 = pygame.image.load("Images/normal/Music_toggle.png").convert()
    img2 = pygame.image.load("Images/normal/Sound_effect_toggle.png").convert()
    img3 = pygame.image.load("Images/normal/Mini_me_toggle.png").convert()
    img4 = pygame.image.load("Images/normal/Options_back.png").convert()
    img5 = pygame.image.load("Images/other/on.png").convert()
    img6 = pygame.image.load("Images/other/off.png").convert()

    #making images buttons
    music_toggle = b.buttons(200,215,img1,1)
    sound_effect_toggle = b.buttons(200,365,img2,1)
    mini_me_toggle = b.buttons(200,515,img3,1)
    back = b.buttons(60,675,img4,1)
    while True:
        check()
        #putting the images on screen
        surf.blit(bg,(0,0))
        surf.blit(bg2,(150,150))

        #code that makes the images next to the toggle red or green
        if music == True:
            surf.blit(img5,(850,215))
        elif music == False:
            surf.blit(img6,(850,215))
        if sound_effect == True:
            surf.blit(img5,(850,365))
        elif sound_effect == False:
            surf.blit(img6,(850,365))
        if mini_me == True:
            surf.blit(img5,(850,515))
        elif mini_me == False:
            surf.blit(img6,(850,515))

        #logic behind the toggles and settings
        if music_toggle.draw(surf) and first == False:
            if music == True:
                music = False
            elif music == False:
                music = True

        if sound_effect_toggle.draw(surf) and first == False:
            if sound_effect == True:
                sound_effect = False
            elif sound_effect == False:
                sound_effect = True

        if mini_me_toggle.draw(surf) and first == False:
            if mini_me == True:
                mini_me = False
            elif mini_me == False:
                mini_me = True

        if back.draw(surf) and first == False:
            main_menu()

        #makes it so the game quits when the "x" is pressed
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        #first makes sure that the buttons can only be pressed from the second frame of each function
        first = False
        mainClock.tick(30)#frame rate
        pygame.display.update()#updates the screen with any changes


def lf():#TypeError: 'buttons' object is not callable
    first = True
    bg = pygame.image.load('Images/backgrounds/load_fileBG.png').convert()
    img1 = pygame.image.load("Images/normal/file1.png").convert()
    img2 = pygame.image.load("Images/normal/file2.png").convert()
    img3 = pygame.image.load("Images/normal/file3.png").convert()
    img4 = pygame.image.load("Images/normal/load_file_back.png").convert()

    file1 = b.buttons(400,100,img1,1)
    file2 = b.buttons(400,325,img2,1)
    file3 = b.buttons(400,550,img3,1)
    back = b.buttons(50,675,img4,1)
    while True:
        check()
        surf.blit(bg,(0,0))

        if file1.draw(surf) and first == False:
            print("file1")
        if file2.draw(surf) and first == False:
            print("file2")
        if file3.draw(surf) and first == False:
            print("file3")
        if back.draw(surf) and first == False:
            play_menu()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        pygame.display.update()
        mainClock.tick(30)


def nf():
    first = True
    img1 = pygame.image.load("Images/normal/new_file_filename.png").convert()
    img2 = pygame.image.load("Images/normal/new_file_playername.png").convert()
    img3 = pygame.image.load("Images/normal/new_file_chooseclass.png").convert()
    img4 = pygame.image.load("Images/normal/new_file_done.png").convert()

    filename = b.buttons(50,75,img1,1)
    playername = b.buttons(50,200,img2,1)
    chooseclass = b.buttons(50,325,img3,0.75)
    done = b.buttons(75,650,img4,1.3)
    while True:
        check()

        surf.fill((0,0,0))

        filename.draw(surf)
        playername.draw(surf)

        if chooseclass.draw(surf):
            print("CC")
        if done.draw(surf):
            pygame.mouse.set_visible(False)
            scene1()
    
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        pygame.display.update()
        mainClock.tick(30)

        
def scene1():
    pygame.mouse.set_visible(False)
    Txt1 = pygame.image.load("Images/textboxes/txt1.png")
    op1 = pygame.image.load("Images/characters/old_person.png")
    op = b.images(775,200,op1,10)
    first = True

    while True:
        check()
        surf.fill((0,0,0))
        surf.blit(Txt1,(150,580))
        op.draw(surf)
        
        keys = pygame.key.get_pressed()
        
        if keys[K_RETURN] and first == False:
            scene2()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        mainClock.tick(30)
        pygame.display.update()


                
def scene2():
    Txt2 = pygame.image.load("Images/textboxes/txt2.png")
    op1 = pygame.image.load("Images/characters/old_person.png")
    op = b.images(775,200,op1,10)
    first = True
    count = 0

    while True:
        surf.fill((0,0,0))
        surf.blit(Txt2,(150,580))
        op.draw(surf)
        
        keys = pygame.key.get_pressed()

        if keys[K_RETURN] and first == False and count > 15:
            scene3()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        count += 1
        mainClock.tick(30)
        pygame.display.update()

def scene3():
    Txt3 = pygame.image.load("Images/textboxes/txt3.png")
    op1 = pygame.image.load("Images/characters/old_person.png")
    op = b.images(775,200,op1,10)
    first = True
    count = 0

    while True:
        surf.fill((0,0,0))
        surf.blit(Txt3,(150,580))
        op.draw(surf)
        
        keys = pygame.key.get_pressed()

        if keys[K_RETURN] and first == False and count > 15:
            scene4()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        count += 1
        mainClock.tick(30)
        pygame.display.update()

def scene4():
    Txt4 = pygame.image.load("Images/textboxes/txt4.png")
    op1 = pygame.image.load("Images/characters/old_person_dark.png")
    op = b.images(775,200,op1,10)
    p1 = pygame.image.load("Images/characters/player.png")
    p = b.images(25,205,p1,10)
    first = True
    count = 0

    while True:
        surf.fill((0,0,0))
        surf.blit(Txt4,(150,580))
        op.draw(surf)
        p.draw(surf)
        
        keys = pygame.key.get_pressed()

        if keys[K_RETURN] and first == False and count > 15:
            scene5()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        count += 1
        mainClock.tick(30)
        pygame.display.update()

def scene5():
    Txt5 = pygame.image.load("Images/textboxes/txt5.png")
    op1 = pygame.image.load("Images/characters/old_person.png")
    op = b.images(775,200,op1,10)
    p1 = pygame.image.load("Images/characters/player_dark.png")
    p = b.images(25,205,p1,10)
    first = True
    count = 0

    while True:
        surf.fill((0,0,0))
        surf.blit(Txt5,(150,580))
        op.draw(surf)
        p.draw(surf)
        
        keys = pygame.key.get_pressed()

        if keys[K_RETURN] and first == False and count > 15:
            scene6()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        count += 1
        mainClock.tick(30)
        pygame.display.update()

def scene6():
    Txt6 = pygame.image.load("Images/textboxes/txt6.png")
    op1 = pygame.image.load("Images/characters/old_person_dark.png")
    op = b.images(775,200,op1,10)
    p1 = pygame.image.load("Images/characters/player.png")
    p = b.images(25,205,p1,10)
    first = True
    count = 0

    while True:
        surf.fill((0,0,0))
        surf.blit(Txt6,(150,580))
        op.draw(surf)
        p.draw(surf)
        
        keys = pygame.key.get_pressed()

        if keys[K_RETURN] and first == False and count > 15:
            scene7()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        count += 1
        mainClock.tick(30)
        pygame.display.update()

def scene7():
    Txt7 = pygame.image.load("Images/textboxes/txt7.png")
    op1 = pygame.image.load("Images/characters/old_person.png")
    op = b.images(775,200,op1,10)
    p1 = pygame.image.load("Images/characters/player_dark.png")
    p = b.images(25,205,p1,10)
    first = True
    count = 0

    while True:
        surf.fill((0,0,0))
        surf.blit(Txt7,(150,580))
        op.draw(surf)
        p.draw(surf)
        
        keys = pygame.key.get_pressed()

        if keys[K_RETURN] and first == False and count > 15:
            scene8()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        count += 1
        mainClock.tick(30)
        pygame.display.update()

def scene8():
    Txt8 = pygame.image.load("Images/textboxes/txt8.png")
    op1 = pygame.image.load("Images/characters/old_person_dark.png")
    op = b.images(775,200,op1,10)
    p1 = pygame.image.load("Images/characters/player.png")
    p = b.images(25,205,p1,10)
    first = True
    count = 0

    while True:
        surf.fill((0,0,0))
        surf.blit(Txt8,(150,580))
        op.draw(surf)
        p.draw(surf)
        
        keys = pygame.key.get_pressed()

        if keys[K_RETURN] and first == False and count > 15:
            scene9()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        count += 1
        mainClock.tick(30)
        pygame.display.update()

def scene9():
    Txt9 = pygame.image.load("Images/textboxes/txt9.png")
    op1 = pygame.image.load("Images/characters/old_person_dark.png")
    op = b.images(775,200,op1,10)
    p1 = pygame.image.load("Images/characters/player.png")
    p = b.images(25,205,p1,10)
    first = True
    count = 0

    while True:
        surf.fill((0,0,0))
        surf.blit(Txt9,(150,580))

        op.draw(surf)
        p.draw(surf)
        
        keys = pygame.key.get_pressed()

        if keys[K_RETURN] and first == False and count > 15:
            scene10()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        count += 1
        mainClock.tick(30)
        pygame.display.update()

def scene10():
    Txt10 = pygame.image.load("Images/textboxes/txt10.png")
    op1 = pygame.image.load("Images/characters/old_person.png")
    op = b.images(775,200,op1,10)
    p1 = pygame.image.load("Images/characters/player_dark.png")
    p = b.images(25,205,p1,10)
    first = True
    count = 0

    while True:
        surf.fill((0,0,0))
        surf.blit(Txt10,(150,580))
        op.draw(surf)
        p.draw(surf)
        
        keys = pygame.key.get_pressed()

        if keys[K_RETURN] and first == False and count > 15:
            scene11()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        count += 1
        mainClock.tick(30)
        pygame.display.update()

def scene11():
    Txt11 = pygame.image.load("Images/textboxes/txt11.png")
    op1 = pygame.image.load("Images/characters/old_person.png")
    op = b.images(775,200,op1,10)
    p1 = pygame.image.load("Images/characters/player_dark.png")
    p = b.images(25,205,p1,10)
    first = True
    count = 0

    while True:
        surf.fill((0,0,0))
        surf.blit(Txt11,(150,580))
        op.draw(surf)
        p.draw(surf)
        
        keys = pygame.key.get_pressed()

        if keys[K_RETURN] and first == False and count > 15:
            scene12()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        count += 1
        mainClock.tick(30)
        pygame.display.update()

def scene12():
    Txt12 = pygame.image.load("Images/textboxes/txt12.png")
    op1 = pygame.image.load("Images/characters/old_person_dark.png")
    op = b.images(775,200,op1,10)
    p1 = pygame.image.load("Images/characters/player.png")
    p = b.images(25,205,p1,10)
    first = True
    count = 0

    while True:
        surf.fill((0,0,0))
        surf.blit(Txt12,(150,580))
        op.draw(surf)
        p.draw(surf)
        
        keys = pygame.key.get_pressed()

        if keys[K_RETURN] and first == False and count > 15:
            scene13()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        count += 1
        mainClock.tick(30)
        pygame.display.update()

def scene13():
    Txt13 = pygame.image.load("Images/textboxes/txt13.png")
    op1 = pygame.image.load("Images/characters/old_person_dark.png")
    op = b.images(775,200,op1,10)
    p1 = pygame.image.load("Images/characters/player.png")
    p = b.images(25,205,p1,10)
    first = True
    count = 0

    while True:
        surf.fill((0,0,0))
        surf.blit(Txt13,(150,580))
        op.draw(surf)
        p.draw(surf)
        
        keys = pygame.key.get_pressed()

        if keys[K_RETURN] and first == False and count > 15:
            scene14()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        count += 1
        mainClock.tick(30)
        pygame.display.update()

def scene14():
    Txt14 = pygame.image.load("Images/textboxes/txt14.png")
    op1 = pygame.image.load("Images/characters/old_person.png")
    op = b.images(775,200,op1,10)
    p1 = pygame.image.load("Images/characters/player_dark.png")
    p = b.images(25,205,p1,10)
    first = True
    count = 0

    while True:
        surf.fill((0,0,0))
        surf.blit(Txt14,(150,580))
        op.draw(surf)
        p.draw(surf)
        
        keys = pygame.key.get_pressed()

        if keys[K_RETURN] and first == False and count > 15:
            scene15()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        count += 1
        mainClock.tick(30)
        pygame.display.update()

def scene15():
    Txt15 = pygame.image.load("Images/textboxes/txt15.png")
    op1 = pygame.image.load("Images/characters/old_person.png")
    op = b.images(775,200,op1,10)
    p1 = pygame.image.load("Images/characters/player_dark.png")
    p = b.images(25,205,p1,10)
    first = True
    count = 0

    while True:
        surf.fill((0,0,0))
        surf.blit(Txt15,(150,580))
        op.draw(surf)
        p.draw(surf)
        
        keys = pygame.key.get_pressed()

        if keys[K_RETURN] and first == False and count > 15:
            scene16()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        count += 1
        mainClock.tick(30)
        pygame.display.update()

def scene16():
    Txt16 = pygame.image.load("Images/textboxes/txt16.png")
    op1 = pygame.image.load("Images/characters/old_person.png")
    op = b.images(775,200,op1,10)
    p1 = pygame.image.load("Images/characters/player_dark.png")
    p = b.images(25,205,p1,10)
    first = True
    count = 0

    while True:
        surf.fill((0,0,0))
        surf.blit(Txt16,(150,580))
        op.draw(surf)
        p.draw(surf)
        
        keys = pygame.key.get_pressed()

        if keys[K_RETURN] and first == False and count > 15:
            scene17()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        count += 1
        mainClock.tick(30)
        pygame.display.update()

def scene17():
    Txt17 = pygame.image.load("Images/textboxes/txt17.png")
    op1 = pygame.image.load("Images/characters/old_person.png")
    op = b.images(775,200,op1,10)
    p1 = pygame.image.load("Images/characters/player_dark.png")
    p = b.images(25,205,p1,10)
    first = True
    count = 0

    while True:
        surf.fill((0,0,0))
        surf.blit(Txt17,(150,580))
        op.draw(surf)
        p.draw(surf)
        
        keys = pygame.key.get_pressed()

        if keys[K_RETURN] and first == False and count > 15:
            scene18()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        count += 1
        mainClock.tick(30)
        pygame.display.update()

def scene18():
    Txt18 = pygame.image.load("Images/textboxes/txt18.png")
    op1 = pygame.image.load("Images/characters/old_person.png")
    op = b.images(775,200,op1,10)
    p1 = pygame.image.load("Images/characters/player_dark.png")
    p = b.images(25,205,p1,10)
    first = True
    count = 0

    while True:
        surf.fill((0,0,0))
        surf.blit(Txt18,(150,580))
        op.draw(surf)
        p.draw(surf)
        
        keys = pygame.key.get_pressed()

        if keys[K_RETURN] and first == False and count > 15:
            scene19()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        count += 1
        mainClock.tick(30)
        pygame.display.update()

def scene19():
    Txt19 = pygame.image.load("Images/textboxes/txt19.png")
    op1 = pygame.image.load("Images/characters/old_person_dark.png")
    op = b.images(775,200,op1,10)
    p1 = pygame.image.load("Images/characters/player.png")
    p = b.images(25,205,p1,10)
    first = True
    count = 0

    while True:
        surf.fill((0,0,0))
        surf.blit(Txt19,(150,580))

        op.draw(surf)
        p.draw(surf)
        
        keys = pygame.key.get_pressed()

        if keys[K_RETURN] and first == False and count > 15:
            scene20()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        count += 1
        mainClock.tick(30)
        pygame.display.update()

def scene20():
    Txt20 = pygame.image.load("Images/textboxes/txt20.png")
    op1 = pygame.image.load("Images/characters/old_person_dark.png")
    op = b.images(775,200,op1,10)
    p1 = pygame.image.load("Images/characters/player.png")
    p = b.images(25,205,p1,10)
    first = True
    count = 0

    while True:
        surf.fill((0,0,0))
        surf.blit(Txt20,(150,580))
        op.draw(surf)
        p.draw(surf)
        
        keys = pygame.key.get_pressed()

        if keys[K_RETURN] and first == False and count > 15:
            scene21()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        count += 1
        mainClock.tick(30)
        pygame.display.update()

def scene21():
    Txt21 = pygame.image.load("Images/textboxes/txt21.png")
    op1 = pygame.image.load("Images/characters/old_person.png")
    op = b.images(775,200,op1,10)
    p1 = pygame.image.load("Images/characters/player_dark.png")
    p = b.images(25,205,p1,10)
    first = True
    count = 0

    while True:
        surf.fill((0,0,0))
        surf.blit(Txt21,(150,580))
        op.draw(surf)
        p.draw(surf)
        
        keys = pygame.key.get_pressed()

        if keys[K_RETURN] and first == False and count > 15:
            scene22()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        count += 1
        mainClock.tick(30)
        pygame.display.update()

def scene22():
    Txt22 = pygame.image.load("Images/textboxes/txt22.png")
    op1 = pygame.image.load("Images/characters/old_person.png")
    op = b.images(775,200,op1,10)
    p1 = pygame.image.load("Images/characters/player_dark.png")
    p = b.images(25,205,p1,10)
    first = True
    count = 0

    while True:
        surf.fill((0,0,0))
        surf.blit(Txt22,(150,580))
        op.draw(surf)
        p.draw(surf)
        
        keys = pygame.key.get_pressed()

        if keys[K_RETURN] and first == False and count > 15:
            scene23()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        count += 1
        mainClock.tick(30)
        pygame.display.update()

def scene23():
    Txt23 = pygame.image.load("Images/textboxes/txt23.png")
    op1 = pygame.image.load("Images/characters/old_person.png")
    p1 = pygame.image.load("Images/characters/player.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    op = b.images(775,200,op1,10)
    p = b.images(25,205,p1,10)
    st = b.images(700,180,st1,8)
    first = True
    count = 0

    while True:
        surf.fill((0,0,0))
        surf.blit(Txt23,(150,580))
        p.draw(surf)
        st.draw(surf)
        op.draw(surf)
        
        keys = pygame.key.get_pressed()

        if keys[K_RETURN] and first == False and count > 15:
            scene24()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        count += 1
        mainClock.tick(30)
        pygame.display.update()

def scene24():
    Txt24 = pygame.image.load("Images/textboxes/txt24.png")
    op1 = pygame.image.load("Images/characters/old_person.png")
    p1 = pygame.image.load("Images/characters/player.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    op = b.images(775,200,op1,10)
    p = b.images(25,205,p1,10)
    st = b.images(700,180,st1,9)
    ch = b.images(500,200,ch1,7)
    first = True
    count = 0

    while True:
        surf.fill((0,0,0))
        surf.blit(Txt24,(150,580))
        op.draw(surf)
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)
        
        keys = pygame.key.get_pressed()

        if keys[K_RETURN] and first == False and count > 15:
            scene25()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        count += 1
        mainClock.tick(30)
        pygame.display.update()

def scene25():
    Txt25 = pygame.image.load("Images/textboxes/txt25.png")
    p1 = pygame.image.load("Images/characters/player.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,200,st1,9)
    ch = b.images(450,200,ch1,8)
    first = True
    count = 0

    while True:
        surf.fill((0,0,0))
        surf.blit(Txt25,(150,580))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)
        
        keys = pygame.key.get_pressed()

        if keys[K_RETURN] and first == False and count > 15:
            scene26()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        count += 1
        mainClock.tick(30)
        pygame.display.update()

def scene26():
    Txt26 = pygame.image.load("Images/textboxes/txt26.png")
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger_dark.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,200,st1,9)
    ch = b.images(180,230,ch1,9)
    first = True
    count = 0

    while True:
        surf.fill((0,0,0))
        surf.blit(Txt26,(150,580))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)
        
        keys = pygame.key.get_pressed()

        if keys[K_RETURN] and first == False and count > 15:
            scene26a()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        count += 1
        mainClock.tick(30)
        pygame.display.update()

def scene26a():
    Txt26 = pygame.image.load("Images/textboxes/txt26.png")
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger_dark.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,200,st1,9)
    ch = b.images(450,200,ch1,8)
    first = True
    count = 0
    font = pygame.font.SysFont("comicsans",45,True)
    text = font.render("The answer is yes, you have no choice",1,grey)

    while True:
        surf.fill((0,0,0))
        surf.blit(Txt26,(150,580))
        surf.blit(text,(170,685))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)
        
        keys = pygame.key.get_pressed()

        if keys[K_RETURN] and first == False and count > 15:
            scene27()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        count += 1
        mainClock.tick(30)
        pygame.display.update()

def scene27():
    Txt27 = pygame.image.load("Images/textboxes/txt27.png")
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog_dark.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,200,st1,9)
    ch = b.images(450,200,ch1,8)
    first = True
    count = 0

    while True:
        surf.fill((0,0,0))
        surf.blit(Txt27,(150,580))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)
        
        keys = pygame.key.get_pressed()

        if keys[K_RETURN] and first == False and count > 15:
            scene28()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        count += 1
        mainClock.tick(30)
        pygame.display.update()

def scene28():
    Txt28 = pygame.image.load("Images/textboxes/txt28.png")
    p1 = pygame.image.load("Images/characters/player.png")
    st1 = pygame.image.load("Images/characters/stranger_dark.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog_dark.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,200,st1,9)
    ch = b.images(450,200,ch1,8)
    first = True
    count = 0

    while True:
        surf.fill((0,0,0))
        surf.blit(Txt28,(150,580))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)
        
        keys = pygame.key.get_pressed()

        if keys[K_RETURN] and first == False and count > 15:
            scene28a()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        count += 1
        mainClock.tick(30)
        pygame.display.update()

def scene28a():
    Txt28 = pygame.image.load("Images/textboxes/txt28.png")
    p1 = pygame.image.load("Images/characters/player.png")
    st1 = pygame.image.load("Images/characters/stranger_dark.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog_dark.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,200,st1,9)
    ch = b.images(450,200,ch1,8)
    first = True
    count = 0
    font = pygame.font.SysFont("comicsans",30,True)
    text = font.render("the answer is yes.you weren't going to say no were you?",1,grey)
    

    while True:
        surf.fill((0,0,0))
        surf.blit(Txt28,(150,580))
        surf.blit(text,(170,685))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)
        
        keys = pygame.key.get_pressed()

        if keys[K_RETURN] and first == False and count > 15:
            scene29()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        count += 1
        mainClock.tick(30)
        pygame.display.update()

def scene29():
    Txt29 = pygame.image.load("Images/textboxes/txt29.png")
    p1 = pygame.image.load("Images/characters/player.png")
    st1 = pygame.image.load("Images/characters/stranger_dark.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog_dark.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,200,st1,9)
    ch = b.images(450,200,ch1,8)
    first = True
    count = 0

    while True:
        surf.fill((0,0,0))
        surf.blit(Txt29,(150,580))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)
        
        keys = pygame.key.get_pressed()

        if keys[K_RETURN] and first == False and count > 15:
            scene30()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        count += 1
        mainClock.tick(30)
        pygame.display.update()

def scene30():
    Txt30 = pygame.image.load("Images/textboxes/txt30.png")
    p1 = pygame.image.load("Images/characters/player.png")
    st1 = pygame.image.load("Images/characters/stranger_dark.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog_dark.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,200,st1,9)
    ch = b.images(450,200,ch1,8)
    first = True
    count = 0

    while True:
        surf.fill((0,0,0))
        surf.blit(Txt30,(150,580))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)
        
        keys = pygame.key.get_pressed()

        if keys[K_RETURN] and first == False and count > 15:
            scene31()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        count += 1
        mainClock.tick(30)
        pygame.display.update()

def scene31():
    Txt31 = pygame.image.load("Images/textboxes/txt31.png")
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog_dark.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,200,st1,9)
    ch = b.images(450,200,ch1,8)
    first = True
    count = 0

    while True:
        surf.fill((0,0,0))
        surf.blit(Txt31,(150,580))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)
        
        keys = pygame.key.get_pressed()

        if keys[K_RETURN] and first == False and count > 15:
            scene32()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        count += 1
        mainClock.tick(30)
        pygame.display.update()

def scene32():
    Txt32 = pygame.image.load("Images/textboxes/txt32.png")
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog_dark.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,200,st1,9)
    ch = b.images(450,200,ch1,8)
    first = True
    count = 0

    while True:
        surf.fill((0,0,0))
        surf.blit(Txt32,(150,580))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)
        
        keys = pygame.key.get_pressed()

        if keys[K_RETURN] and first == False and count > 15:
            scene33()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        count += 1
        mainClock.tick(30)
        pygame.display.update()

def scene33():
    Txt33 = pygame.image.load("Images/textboxes/txt33.png")
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog_dark.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,200,st1,9)
    ch = b.images(450,200,ch1,8)
    first = True
    count = 0

    while True:
        surf.fill((0,0,0))
        surf.blit(Txt33,(150,580))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)
        
        keys = pygame.key.get_pressed()

        if keys[K_RETURN] and first == False and count > 15:
            leave1()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        first = False
        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave1():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,190,st1,9)
    ch = b.images(465,200,ch1,8)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave2()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave2():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,180,st1,9)
    ch = b.images(480,200,ch1,8)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave3()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave3():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,170,st1,9)
    ch = b.images(495,200,ch1,8)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave4()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave4():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,160,st1,9)
    ch = b.images(510,200,ch1,8)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave5()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave5():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,150,st1,9)
    ch = b.images(525,200,ch1,8)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave6()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave6():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,140,st1,9)
    ch = b.images(540,200,ch1,8)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave7()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave7():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,130,st1,9)
    ch = b.images(555,200,ch1,8)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave8()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave8():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,120,st1,9)
    ch = b.images(560,200,ch1,8)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave9()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave9():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,110,st1,9)
    ch = b.images(575,200,ch1,8)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave10()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave10():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,100,st1,9)
    ch = b.images(575,190,ch1,8)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave11()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave11():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,90,st1,9)
    ch = b.images(575,180,ch1,8)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave12()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave12():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,80,st1,9)
    ch = b.images(575,170,ch1,8)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave13()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave13():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,70,st1,9)
    ch = b.images(575,160,ch1,8)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave14()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave14():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,60,st1,9)
    ch = b.images(575,150,ch1,8)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave15()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave15():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,50,st1,9)
    ch = b.images(575,140,ch1,8)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave16()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave16():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,40,st1,9)
    ch = b.images(575,130,ch1,8)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave17()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave17():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,30,st1,9)
    ch = b.images(575,120,ch1,8)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave18()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave18():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,20,st1,8)
    ch = b.images(575,110,ch1,7)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave19()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave19():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,10,st1,8)
    ch = b.images(575,100,ch1,7)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave20()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave20():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,0,st1,8)
    ch = b.images(575,90,ch1,7)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave21()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave21():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,-10,st1,8)
    ch = b.images(575,80,ch1,7)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave22()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave22():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,-20,st1,8)
    ch = b.images(575,70,ch1,7)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave23()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave23():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,-30,st1,8)
    ch = b.images(575,60,ch1,7)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave24()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave24():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,-40,st1,7)
    ch = b.images(575,50,ch1,6)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave25()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave25():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,-50,st1,7)
    ch = b.images(575,40,ch1,6)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave26()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave26():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,-60,st1,7)
    ch = b.images(575,30,ch1,6)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave27()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave27():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,-70,st1,7)
    ch = b.images(575,20,ch1,6)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave28()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave28():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,-80,st1,7)
    ch = b.images(575,10,ch1,6)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave29()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave29():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,-90,st1,7)
    ch = b.images(575,0,ch1,6)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave30()


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave30():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,-100,st1,7)
    ch = b.images(575,-10,ch1,6)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave31()


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave31():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,-110,st1,7)
    ch = b.images(575,-20,ch1,6)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave32()


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave32():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,-120,st1,7)
    ch = b.images(575,-30,ch1,6)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave33()


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave33():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,-130,st1,7)
    ch = b.images(575,-40,ch1,6)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave34()


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave34():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,-140,st1,7)
    ch = b.images(575,-50,ch1,6)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave35()


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave35():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,-150,st1,7)
    ch = b.images(575,-60,ch1,6)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave36()


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave36():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,-160,st1,7)
    ch = b.images(575,-70,ch1,6)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave37()


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave37():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,-170,st1,7)
    ch = b.images(575,-80,ch1,6)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave38()


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave38():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,-180,st1,7)
    ch = b.images(575,-90,ch1,6)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave39()


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave39():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,-190,st1,7)
    ch = b.images(575,-100,ch1,6)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave40()


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave40():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,-200,st1,7)
    ch = b.images(575,-110,ch1,6)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave41()


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave41():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,-210,st1,7)
    ch = b.images(575,-120,ch1,6)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave42()


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave42():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,-220,st1,7)
    ch = b.images(575,-130,ch1,6)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave43()


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave43():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,-230,st1,7)
    ch = b.images(575,-140,ch1,6)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave44()


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave44():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,-240,st1,7)
    ch = b.images(575,-150,ch1,6)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave45()


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave45():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,-250,st1,7)
    ch = b.images(575,-160,ch1,6)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave46()


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave46():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,-250,st1,7)
    ch = b.images(575,-170,ch1,6)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave47()


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave47():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,-250,st1,7)
    ch = b.images(575,-180,ch1,6)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave48()


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave48():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,-250,st1,7)
    ch = b.images(575,-190,ch1,6)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave49()


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave49():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,-250,st1,7)
    ch = b.images(575,-200,ch1,6)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            leave50()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def leave50():
    p1 = pygame.image.load("Images/characters/player_dark.png")
    st1 = pygame.image.load("Images/characters/stranger.png")
    ch1 = pygame.image.load("Images/characters/raccoon_dog.png")
    p = b.images(25,205,p1,10)
    st = b.images(700,-250,st1,7)
    ch = b.images(575,-210,ch1,6)

    count = 0

    while True:
        surf.fill((0,0,0))
        p.draw(surf)
        st.draw(surf)
        ch.draw(surf)

        if count >= 2:
            gp0()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        mainClock.tick(30)
        pygame.display.update()

def gp0():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")
    textb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)

    text = font.render("From this point onwards, you can type 'settings' to",1,grey)
    text2 = font.render("access the options menu from anywhere in the game",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,textb1,1)

    first = True

    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,630))
        
        for event in pygame.event.get():
            if event == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_RETURN and first == False:
                    gp1()
                else:
                    pass

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp1():
    #loading images and fonts
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    #setting user input up
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    #text
    text = font.render("You eventually wake up with a headache and sit",1,grey)
    text2 = font.render("up. Do you look around the room?",1,grey)

    text3 = font.render("Options:",1,grey)
    text4 = font.render("yes",1,grey)

    #assigning variables classes
    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    #setting variables
    first = True
    
    while True:
        check()
        #loading in images
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,630))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))

        #event loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]#this removes the last inputted character from the string
                elif user_text == "yes" and K_RETURN:
                    gp2()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp1)
                else:
                    user_text += event.unicode#takes the keyboard input and makes it text

        pygame.draw.rect(surf,colour,input_rect,2)#surface,colour,rectangle info,border width
        text_surf = base_font.render(user_text,True,(white))#text,anti-asailing,colour
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 10))#text,using the coords of input rectangle to position the text
        input_rect.w = max(100,text_surf.get_width() + 15)#this means that the textbox expands with the length of the text

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp2():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("In the room there is a desk, a fireplace and a door.",1,grey)
    text2 = font.render("What do you do?",1,grey)
    text3 = font.render("Options:",1,grey)
    text4 = font.render("investigate desk",1,grey)
    text5 = font.render("investigate fireplace",1,grey)
    text6 = font.render("go to door",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,630))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text5,(90,70))
        surf.blit(text6,(90,100))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "investigate desk" and K_RETURN:
                    gp2a()
                elif user_text == "investigate fireplace" and K_RETURN:
                    gp2b()
                elif user_text == "go to door" and K_RETURN:
                    gp2c()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp2) 
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp2a():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("On the desk is a pile of paper, the top one",1,grey)
    text2 = font.render("has writing on it. What do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("read the paper",1,grey)
    text5 = font.render("leave it",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,630))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text5,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "read the paper" and K_RETURN:
                    gp2a1()
                elif user_text == "leave it" and K_RETURN:
                    gp2()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp2a)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp2a1():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("It says 'day 112: i have stared at this wall all day",1,grey)
    text2 = font.render("it is a very good wall'. Do you turn back?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("yes",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,630))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "yes" and K_RETURN:
                    gp2()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp2a1)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp2b():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("It is just a fireplace, i don't know what",1,grey)
    text2 = font.render("you were expecting. Do you turn back?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("yes",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,630))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "yes" and K_RETURN:
                    gp2()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp2b)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp2c():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("The door leads to a dark corridoor.",1,grey)
    text2 = font.render("What do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("through the door",1,grey)
    text5 = font.render("turn back",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,630))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text5,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "through the door" and K_RETURN:
                    gp3()
                elif user_text == "turn back" and K_RETURN:
                    gp2()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp2c)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp3():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("There are a few barrels infront of you and beyond",1,grey)
    text2 = font.render("that the corridoor carries on. What do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("investigate barrels",1,grey)
    text5 = font.render("carry on",1,grey)
    text6 = font.render("turn back",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)
    
    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,630))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text5,(90,70))
        surf.blit(text6,(90,100))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "investigate barrels" and K_RETURN:
                    gp3a()
                elif user_text == "carry on" and K_RETURN:
                    gp3b()
                elif user_text == "turn back" and K_RETURN:
                    gp2()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp3)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp3a():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("One of the three barrels have a rusty, dented helmet",1,grey)
    text2 = font.render("What do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("wear the helmet",1,grey)
    text5 = font.render("leave it",1,grey)
    
    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,630))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text5,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "wear the helmet" and K_RETURN:
                    gp3a1()
                elif user_text == "leave it" and K_RETURN:
                    gp3()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp3a)
                else:
                    user_text += event.unicode
                    
        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp3a1():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)

    text = font.render("Helmet equipped",1,yellow2)
    
    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    gp3()

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp3b():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("A long corridoor is in front of you.",1,grey)
    text2 = font.render("What do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("carry on",1,grey)
    text5 = font.render("turn back",1,grey)
    
    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)
    
    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,630))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text5,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "carry on" and K_RETURN:
                    gp3c()
                elif user_text == "turn back" and K_RETURN:
                    gp3()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp3b)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp3c():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("You're now in a small room.",1,grey)
    text2 = font.render("What do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("search room",1,grey)
    text5 = font.render("turn back",1,grey)
    
    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,630))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text5,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "search room" and K_RETURN:
                    gp3d()
                elif user_text == "turn back" and K_RETURN:
                    gp3b()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp3c)
                else:
                    user_text += event.unicode
                    
        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp3d():
    global start,general_combat
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("The room is empty except for a small trapdoor",1,grey)
    text2 = font.render("in the corner. What do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("enter trapdoor",1,grey)
    text5 = font.render("turn back",1,grey)
    
    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,630))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text5,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "enter trapdoor" and K_RETURN:
                    if c1 == False:
                        pygame.mixer.music.unload()
                        start = False
                        general_combat = True
                        gp4C0()
                    else:
                        gp4()
                elif user_text == "turn back" and K_RETURN:
                    gp3b()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp3d)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp4C0():
    bg1 = pygame.image.load("Images/backgrounds/combat_tutorial.png")
    bg = b.images(0,0,bg1,1)
    
    while True:
        check()
        bg.draw(surf)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    pygame.mouse.set_visible(True)
                    gp4C()

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp4C():
    global p,c1
    panel1 = pygame.image.load("Images/combat/combat_bottom.png")#not made by me
    enemy1 = pygame.image.load("Images/enemies/slime.png")
    dodge = pygame.image.load("Images/other/dodge.png")

    e = b.enemy(950,480,50,3,enemy1,10)#creates an enemy instance in the enemy class
    panel = b.images(0,560,panel1,1.5)
    d = b.images(400,230,dodge,2)

    count = 0
    count1 = 0
    count2 = 0
    mcount = 0

    pressed = False
    
    while True:
        check()
        surf.fill((45,45,45))
        panel.draw(surf)
        p.draw(surf)
        e.draw(surf)

        key = pygame.key.get_pressed()

        count += 1

        if count%15 == 0:#cooldown for primary
            count1 += 1

        if count%20 == 0:
            mcount += 1

        if count%60 == 0:#cooldown for secondary
            count2 += 1

        if mcount != 0 and pressed == False:
            d.draw(surf)
        
        if mcount != 0:
            if key[K_d]:
                mcount = 0
                pressed = True

        if count%30 == 0:
            mcount = 0
            if pressed == True:
                pressed = False
            else:
                damage = r.randint(1,e.strength)
                p.hurt1(damage)

        if count1 >= 1:#player primary attack, having it wait at least 1/2 a second between attacks
            if e.action():
                count1 = 0
                e.hurt1()

        if count2 >= 1:#player secondary attack
            if e.action2():
                count2 = 0
                damage = r.randint(15,30)
                e.hurt2(damage)

        if e.alive == False:#checking if enemy has any hp
            pygame.mouse.set_visible(False)
            del e#removes enemy from class
            c1 = True
            gp4()

        if p.alive == False:#checking if player has any hp
            pygame.mouse.set_visible(False)
            gp3d()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        mainClock.tick(30)
        pygame.display.update()

def gp4():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("You enter a room that has a wooden floor covered",1,grey)
    text2 = font.render("in strange red stains. What do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("look around",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,630))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "look around" and K_RETURN:
                    gp4a()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp4)
                else:
                    user_text += event.unicode
                    

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp4a():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("The room is mostly empty except for a single doorway",1,grey)
    text2 = font.render("What do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("go through door",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,630))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "go through door" and K_RETURN:
                    gp4b()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp4a)
                else:
                    user_text += event.unicode
                    

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp4b():#root for 'phase 2'
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("The corridoor is dark and you can only go 2 ways",1,grey)
    text2 = font.render("What do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("left",1,grey)
    text5 = font.render("right",1,grey)
    text6 = font.render("turn back",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,630))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text5,(90,70))
        surf.blit(text6,(90,100))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "left" and K_RETURN:
                    gp6()
                elif user_text == "right" and K_RETURN:
                    gp5()
                elif user_text == "turn back" and K_RETURN:
                    gp4()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp4b)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp4b
                        mapp(prev)
                    else:
                        pass
                else:
                    user_text += event.unicode
                    

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp6():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("The corridoor is dark and there doens't seem",1,grey)
    text2 = font.render("to be an end. What do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("carry on",1,grey)
    text6 = font.render("turn back",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,630))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text6,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "carry on" and K_RETURN:
                    gp6a()
                elif user_text == "turn back" and K_RETURN:
                    gp4b()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp6)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp6
                        mapp(prev)
                    else:
                        pass
                else:
                    user_text += event.unicode
                    

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp6a():
    global start,general_combat
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("There is a small opening to your left, a room to the right",1,grey)
    text2 = font.render("and a room straight ahead. What do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("left",1,grey)
    text5 = font.render("right",1,grey)
    text6 = font.render("straight ahead",1,grey)
    text7 = font.render("turn back",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,630))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text5,(90,70))
        surf.blit(text6,(90,100))
        surf.blit(text7,(90,130))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "left" and K_RETURN:
                    if c2 == False:
                        pygame.mouse.set_visible(True)
                        pygame.mixer.music.unload()
                        start = False
                        general_combat = True
                        gp6bC()
                    else:
                        gp6b()
                elif user_text == "right" and K_RETURN:
                    gp6c()#archeology room
                elif user_text == "straight ahead" and K_RETURN:
                    if c3 == False:
                        pygame.mouse.set_visible(True)
                        pygame.mixer.music.unload()
                        start = False
                        general_combat = True
                        gp6dC()#ice combat
                    else:
                        gp6d()
                elif user_text == "turn back" and K_RETURN:
                    gp6()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp6a)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp6a
                        mapp(prev)
                    else:
                        pass
                else:
                    user_text += event.unicode
                    

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()


def gp6bC():
    global p,c2,start,general_combat
    panel1 = pygame.image.load("Images/combat/combat_bottom.png")#not made by me
    enemy1 = pygame.image.load("Images/enemies/raccoon.png")
    dodge = pygame.image.load("Images/other/dodge.png")

    e = b.enemy(950,460,75,6,enemy1,8)#creates an enemy instance in the enemy class
    panel = b.images(0,560,panel1,1.5)
    d = b.images(400,230,dodge,2)

    count = 0
    count1 = 0
    count2 = 0
    mcount = 0

    pressed = False

    p.hp = 100
    
    while True:
        check()
        surf.fill((45,45,45))
        panel.draw(surf)
        p.draw(surf)
        e.draw(surf)

        key = pygame.key.get_pressed()

        count += 1

        if count%15 == 0:#cooldown for primary
            count1 += 1

        if count%20 == 0:
            mcount += 1

        if count%60 == 0:#cooldown for secondary
            count2 += 1

        if mcount != 0 and pressed == False:
            d.draw(surf)
        
        if mcount != 0:
            if key[K_d]:
                mcount = 0
                pressed = True

        if count%30 == 0:
            mcount = 0
            if pressed == True:
                pressed = False
            else:
                damage = r.randint(1,e.strength)
                p.hurt1(damage)

        if count1 >= 1:#player primary attack, having it wait at least 1/2 a second between attacks
            if e.action():
                count1 = 0
                e.hurt1()

        if count2 >= 1:#player secondary attack
            if e.action2():
                count2 = 0
                damage = r.randint(15,30)
                e.hurt2(damage)

        if e.alive == False:#checking if enemy has any hp
            pygame.mouse.set_visible(False)
            del e#removes enemy from class
            c2 = True
            pygame.mixer.music.unload()
            start = True
            general_combat = False
            gp6b()

        if p.alive == False:#checking if player has any hp
            pygame.mouse.set_visible(False)
            pygame.mixer.music.unload()
            start = True
            general_combat = False
            gp6a()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        mainClock.tick(30)
        pygame.display.update()

def gp6b():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("The floor is made of soft dirt and you can see a small",1,grey)
    text2 = font.render("chest in the corner. What do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("open chest",1,grey)
    text6 = font.render("leave",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,630))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text6,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "open chest" and K_RETURN:
                    gp6b1()
                elif user_text == "leave" and K_RETURN:
                    gp6a()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp6b)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp6b
                        mapp(prev)
                else:
                    user_text += event.unicode
                    

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp6b1():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)

    text = font.render("There is an upgraded weapon inside",1,yellow2)
    text2 = font.render("YOU WILL TAKE IT :)",1,red)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,630))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN and first == False:
                if K_RETURN:
                    gp6b()

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp6c():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("The floor shifts under your feet as you walk into the room",1,grey)
    text2 = font.render("What do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("look around",1,grey)
    text6 = font.render("leave",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,630))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text6,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "look around" and K_RETURN:
                    gp6c1()
                elif user_text == "leave" and K_RETURN:
                    gp6a()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp6c)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp6c
                        mapp(prev)
                else:
                    user_text += event.unicode
                    

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp6c1():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("There are strange engravings in the wall. You see",1,grey)
    text2 = font.render("something in the sandy floor. What do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("pick it up",1,grey)
    text6 = font.render("leave",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,630))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text6,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "pick it up" and K_RETURN:
                    gp6c2()
                elif user_text == "leave" and K_RETURN:
                    gp6a()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp6c1)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp6c1
                        mapp(prev)
                else:
                    user_text += event.unicode
                    

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp6c2():
    global blob1
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)

    text = font.render("You have obtained the weird blob",1,yellow)
    text2 = font.render("You may or may not regret this",1,red)
    
    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    blob1 = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,630))


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN and first == False:
                if K_RETURN:
                    gp6a()

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp6dC():
    global p,c3,start,general_combat
    panel1 = pygame.image.load("Images/combat/combat_bottom.png")#not made by me
    enemy1 = pygame.image.load("Images/enemies/bat.png")
    dodge = pygame.image.load("Images/other/dodge.png")

    e = b.enemy(885,400,40,3,enemy1,6)#creates an enemy instance in the enemy class
    panel = b.images(0,560,panel1,1.5)
    d = b.images(400,230,dodge,2)

    count = 0
    count1 = 0
    count2 = 0
    mcount = 0

    pressed = False

    p.hp = 100
    
    while True:
        check()
        surf.fill((45,45,45))
        panel.draw(surf)
        p.draw(surf)
        e.draw(surf)

        key = pygame.key.get_pressed()

        count += 1

        if count%15 == 0:#cooldown for primary
            count1 += 1

        if count%20 == 0:
            mcount += 1

        if count%60 == 0:#cooldown for secondary
            count2 += 1

        if mcount != 0 and pressed == False:
            d.draw(surf)
        
        if mcount != 0:
            if key[K_d]:
                mcount = 0
                pressed = True

        if count%30 == 0:
            mcount = 0
            if pressed == True:
                pressed = False
            else:
                damage = r.randint(1,e.strength)
                p.hurt1(damage)

        if count1 >= 1:#player primary attack, having it wait at least 1/2 a second between attacks
            if e.action():
                count1 = 0
                e.hurt1()

        if count2 >= 1:#player secondary attack
            if e.action2():
                count2 = 0
                damage = r.randint(15,30)
                e.hurt2(damage)

        if e.alive == False:#checking if enemy has any hp
            pygame.mouse.set_visible(False)
            del e#removes enemy from class
            c3 = True
            pygame.mixer.music.unload()
            start = True
            general_combat = False
            gp6d()

        if p.alive == False:#checking if player has any hp
            pygame.mouse.set_visible(False)
            pygame.mixer.music.unload()
            start = True
            general_combat = False
            gp6a()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        mainClock.tick(30)
        pygame.display.update()

def gp6d():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    text = font.render("The room is empty and cold",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    gp6a()

        first = False
        mainClock.tick(30)
        pygame.display.update()


def gp5():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("There is a fork in the path",1,grey)
    text2 = font.render("Which way do you go?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("left",1,grey)
    text6 = font.render("right",1,grey)
    text7 = font.render("turn back",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,630))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text6,(90,70))
        surf.blit(text7,(90,100))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "left" and K_RETURN:
                    gp5a()#trapdoor
                elif user_text == "right" and K_RETURN:
                    gp5b()#trap area
                elif user_text == "turn back" and K_RETURN:
                    gp4b()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp5)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp5
                        mapp(prev)
                else:
                    user_text += event.unicode
                    

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()


def gp5a():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("There is a trapdoor, do you go in?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("yes",1,grey)
    text6 = font.render("no",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text6,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "yes" and K_RETURN:
                    gp5a1()
                elif user_text == "no" and K_RETURN:
                    gp5()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp5a)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp5a
                        mapp(prev)
                else:
                    user_text += event.unicode
                    

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp5a1():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("There is a chest, do you open it?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("yes",1,grey)
    text6 = font.render("no",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text6,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "yes" and K_RETURN:
                    gp5a2()
                elif user_text == "no" and K_RETURN:
                    gp5a()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp5a1)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp5a1
                        mapp(prev)
                else:
                    user_text += event.unicode
                    

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp5a2():
    global Map
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)

    text = font.render("You have obtained a map",1,yellow)
    text2 = font.render("You can use it at anytime by typing 'map'",1,white)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))

        Map = True
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    gp5()

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp5b():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    map1 = pygame.image.load("Images/other/map.jpg")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("The floor feels different",1,grey)
    text2 = font.render("Which way do you go?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("carry on",1,grey)
    text6 = font.render("left",1,grey)
    text7 = font.render("turn back",1,grey)
    text8 = font.render("poke ground with weapon",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)
    mapI = b.images(100,100,map1,0.51)

    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,630))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text6,(90,70))
        surf.blit(text7,(90,100))
        surf.blit(text8,(90,130))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "carry on" and K_RETURN:
                    if checked1 == False:
                        death1()
                    else:
                        gp5c()
                elif user_text == "left" and K_RETURN:
                    if checked1 == False:
                        death1()
                    else:
                        gp7()
                elif user_text == "turn back" and K_RETURN:
                    gp5()
                elif user_text == "poke ground with weapon" and K_RETURN:
                    gp5b1()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp5b)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp5b
                        mapp(prev)
                    else:
                        pass
                else:
                    user_text += event.unicode
                    

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()


def gp5b1():
    global checked1
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("Arrows shoot through the floor just scraping the edge",1,grey)
    text2 = font.render("of your weapon. Do you poke the floor again?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("yes",1,grey)
    text6 = font.render("no",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    checked1 = True
    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text6,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "yes" and K_RETURN:
                    gp5b2()
                elif user_text == "no" and K_RETURN:
                    chance = r.randint(1,3)
                    if chance == 1:
                        death1()
                    elif chance == 2:
                        gp5b()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp5b1)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp5b1
                        mapp(prev)
                else:
                    user_text += event.unicode
                    

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()
        

def gp5b2():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("The sound of your weapon hitting the floor bounces off",1,grey)
    text2 = font.render("the walls. Do you poke the floor again?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("yes",1,grey)
    text6 = font.render("no",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text6,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "yes" and K_RETURN:
                    gp5b2()
                elif user_text == "no" and K_RETURN:
                    gp5b()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp5b2)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp5b2
                        mapp(prev)
                else:
                    user_text += event.unicode
                    

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()


def gp5c():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("There is a chest, do you open it?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("yes",1,grey)
    text6 = font.render("no",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text6,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "yes" and K_RETURN:
                    gp5c1()
                elif user_text == "no" and K_RETURN:
                    gp5b()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp5c)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp5c
                        mapp(prev)
                else:
                    user_text += event.unicode
                    

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp5c1():#TEMPORARY REWARD
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)

    text = font.render("There is a thing inside",1,yellow2)
    text2 = font.render("YOU WILL TAKE IT :)",1,red)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,630))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN and first == False:
                if K_RETURN:
                    gp5b()

        first = False
        mainClock.tick(30)
        pygame.display.update()


def gp7():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("A long, dark corridoor is infront of",1,grey)
    text2 = font.render("you. Do you carry on?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("yes",1,grey)
    text6 = font.render("no",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text6,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "yes" and K_RETURN:
                    gp7a()
                elif user_text == "no" and K_RETURN:
                    gp5b()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp7)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp7
                        mapp(prev)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp7a():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("There is a opening to your left. The corridoor",1,grey)
    text2 = font.render("continues past the opening. What do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("through opening",1,grey)
    text6 = font.render("carry on",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text6,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "through opening" and K_RETURN:
                    gp8()
                elif user_text == "carry on" and K_RETURN:
                    gp7a1()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp7a)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp7a
                        mapp(prev)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

                    

def gp7a1():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("There is another opening to your left. The corridoor",1,grey)
    text2 = font.render("continues past the opening. What do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("through opening",1,grey)
    text6 = font.render("carry on",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text6,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "through opening" and K_RETURN:
                    gp9a()
                elif user_text == "carry on" and K_RETURN:
                    gp7a2()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp7a1)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp7a1
                        mapp(prev)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()


def gp7a2():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("The corridoor meets a dead end, there is an opening",1,grey)
    text2 = font.render("to your left. What do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("left",1,grey)
    text6 = font.render("turn back",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text6,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "left" and K_RETURN:
                    gp7a3()
                elif user_text == "turn back" and K_RETURN:
                    gp7a1()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp7a2)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp7a2
                        mapp(prev)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()


def gp7a3():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("There is a doorway to your left. The corridoor continues",1,grey)
    text2 = font.render("past the doorway. What do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("through doorway",1,grey)
    text6 = font.render("carry on",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text6,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "through doorway" and K_RETURN:
                    gp9b()
                elif user_text == "carry on" and K_RETURN:
                    gp9a()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp7a3)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp7a3
                        mapp(prev)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp8():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("The floor shifts under your feet as you walk into the room",1,grey)
    text2 = font.render("What do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("look around",1,grey)
    text6 = font.render("leave",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text6,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "look around" and K_RETURN:
                    gp8a()
                elif user_text == "leave" and K_RETURN:
                    gp7a()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp8)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp8
                        mapp(prev)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()


def gp8a():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("There are strange engravings in the wall. You see",1,grey)
    text2 = font.render("something in the sandy floor. What do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("pick it up",1,grey)
    text6 = font.render("leave",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,630))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text6,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "pick it up" and K_RETURN:
                    gp8a1()
                elif user_text == "leave" and K_RETURN:
                    gp7a()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp8a)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp8a
                        mapp(prev)
                else:
                    user_text += event.unicode
                    

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp8a1():
    global blob2
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)

    text = font.render("You have your second obtained the weird blob",1,yellow)
    text2 = font.render("You have a small collection now",1,yellow2)
    text4 = font.render("Hmmmmmmm, you may regret this (•_•)",1,red)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    blob2 = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        surf.blit(text4,(175,650))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN and first == False:
                if K_RETURN:
                    gp8()

        first = False
        mainClock.tick(30)
        pygame.display.update()


def gp9a():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("The corridoor meets a dead end, there is an opening",1,grey)
    text2 = font.render("to your right. What do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("right",1,grey)
    text5 = font.render("carry on",1,grey)
    text6 = font.render("turn back",1,grey)
    

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text5,(90,70))
        surf.blit(text6,(90,100))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "right" and K_RETURN:
                    gp9b()#trapped room
                elif user_text == "carry on" and K_RETURN:
                    gp10()#miniboss
                elif user_text == "turn back" and K_RETURN:
                    gp7a1()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp9a)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp9a
                        mapp(prev)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()


def gp9b():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("The room is dark and you can hardly see the floor.",1,grey)
    text2 = font.render("There is a shiny thing infront of you. What do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("poke it with weapon",1,grey)
    text6 = font.render("pick it up",1,grey)#will make player lose 20% for next battle, damage 25% reduction
    text7 = font.render("walk around it",1,grey)
    text9 = font.render("walk over it",1,yellow)
    text8 = font.render("leave",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)

        if activated == False:
            surf.blit(text,(175,590))
            surf.blit(text2,(175,620))
            surf.blit(text3,(90,10))
            surf.blit(text4,(90,40))
            surf.blit(text6,(90,70))
            surf.blit(text7,(90,100))
            surf.blit(text9,(90,130))
            surf.blit(text8,(90,160))

        elif activated == True:
            surf.blit(text3,(90,10))
            surf.blit(text7,(90,40))
            surf.blit(text8,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "poke it with weapon" and K_RETURN:
                    gp9b1()
                elif user_text == "pick it up" and K_RETURN:
                    i1()
                elif user_text == "walk around it" and K_RETURN:
                    gp9b2()#NEED TO DO
                elif user_text == "walk over it" and K_RETURN:
                    death2()
                elif user_text == "leave" and K_RETURN:
                    gp7a1()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp9b)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp9b
                        mapp(prev)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()


def gp9b1():
    global activated
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)

    text = font.render("4 giant spikes come out of the ground, you didn't",1,grey)
    text2 = font.render("get stabbed O_O well done!",1,grey)
    
    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    activated = True

    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    gp9b()

        first = False
        mainClock.tick(30)
        pygame.display.update()


def gp9b2():
    global activated
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("As you walk past it 4 giant spikes come out",1,grey)
    text2 = font.render("of the ground, you didn't get stabbed O_O well done!",1,grey) 
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("look around",1,grey)
    text6 = font.render("leave",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    activated = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text6,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "look around" and K_RETURN:
                    gp9b2a
                elif user_text == "leave" and K_RETURN:
                    gp7a1()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp9b2)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp9b2
                        mapp(prev)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()


def gp9b1():
    global activated
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)

    text = font.render("There is a trapdoor you try to open, but it",1,grey)
    text2 = font.render("doesn't open, so you leave",1,grey)
    
    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    activated = True

    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    gp7a1()

        first = False
        mainClock.tick(30)
        pygame.display.update()



def gp9b3():
    global activated
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("There is a trapdoor in the floor.",1,grey)
    text2 = font.render("Do you go through it",1,grey) 
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("yes",1,grey)
    text6 = font.render("no",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    activated = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text6,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "yes" and K_RETURN:
                    gp9b1()#YELLOW TRAPDOOR!!!
                elif user_text == "no" and K_RETURN:
                    gp9b()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp9b3)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()



def gp10():
    global start,mini_boss
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("The corridoor meets a dead end, there is an opening",1,grey)
    text2 = font.render("to your right. What do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("right",1,grey)
    text5 = font.render("carry on",1,grey)
    text6 = font.render("turn back",1,grey)
    

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text5,(90,70))
        surf.blit(text6,(90,100))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "carry on" and K_RETURN:
                    if c4a == False:
                        pygame.mouse.set_visible(True)
                        pygame.mixer.music.unload()
                        start = False
                        mini_boss = True
                        gp10C()#miniboss
                    else:
                        gp10a()
                elif user_text == "turn back" and K_RETURN:
                    gp9a()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp10)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp10
                        mapp(prev)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp10C():
    global p,c4,start,mini_boss
    panel1 = pygame.image.load("Images/combat/combat_bottom.png")#not made by me
    enemy1 = pygame.image.load("Images/enemies/scorp.png")
    dodge = pygame.image.load("Images/other/dodge.png")

    e = b.enemy(900,315,200,12,enemy1,5)#creates an enemy instance in the enemy class
    panel = b.images(0,560,panel1,1.5)
    d = b.images(400,230,dodge,2)

    count = 0
    count1 = 0
    count2 = 0
    mcount = 0

    pressed = False

    p.hp = 100
    
    while True:
        check()
        surf.fill((45,45,45))
        panel.draw(surf)
        p.draw(surf)
        e.draw(surf)

        key = pygame.key.get_pressed()

        count += 1

        if count%15 == 0:#cooldown for primary
            count1 += 1

        if count%20 == 0:
            mcount += 1

        if count%60 == 0:#cooldown for secondary
            count2 += 1

        if mcount != 0 and pressed == False:
            d.draw(surf)
        
        if mcount != 0:
            if key[K_d]:
                mcount = 0
                pressed = True

        if count%30 == 0:
            mcount = 0
            if pressed == True:
                pressed = False
            else:
                damage = r.randint(1,e.strength)
                p.hurt1(damage)

        if count1 >= 1:#player primary attack, having it wait at least 1/2 a second between attacks
            if e.action():
                count1 = 0
                e.hurt1()

        if count2 >= 1:#player secondary attack
            if e.action2():
                count2 = 0
                damage = r.randint(15,30)
                e.hurt2(damage)

        if e.alive == False:#checking if enemy has any hp
            pygame.mouse.set_visible(False)
            del e#removes enemy from class
            c4 = True
            gp10C1()

        if p.alive == False:#checking if player has any hp
            pygame.mouse.set_visible(False)
            pygame.mixer.music.unload()
            start = True
            mini_boss = False
            gp10()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        mainClock.tick(30)
        pygame.display.update()

def gp10C1():
    global p,c4a,start,mini_boss
    pygame.mouse.set_visible(True)
    panel1 = pygame.image.load("Images/combat/combat_bottom.png")#not made by me
    enemy1 = pygame.image.load("Images/enemies/scorpe.png")
    dodge = pygame.image.load("Images/other/dodge.png")

    e = b.enemy(900,315,175,15,enemy1,5)#creates an enemy instance in the enemy class
    panel = b.images(0,560,panel1,1.5)
    d = b.images(400,230,dodge,2)

    count = 0
    count1 = 0
    count2 = 0
    mcount = 0

    pressed = False
    
    while True:
        check()
        surf.fill((45,45,45))
        panel.draw(surf)
        p.draw(surf)
        e.draw(surf)

        key = pygame.key.get_pressed()

        count += 1

        if count%15 == 0:#cooldown for primary
            count1 += 1

        if count%20 == 0:
            mcount += 1

        if count%60 == 0:#cooldown for secondary
            count2 += 1

        if mcount != 0 and pressed == False:
            d.draw(surf)
        
        if mcount != 0:
            if key[K_d]:
                mcount = 0
                pressed = True

        if count%30 == 0:
            mcount = 0
            if pressed == True:
                pressed = False
            else:
                damage = r.randint(1,e.strength)
                p.hurt1(damage)

        if count1 >= 1:#player primary attack, having it wait at least 1/2 a second between attacks
            if e.action():
                count1 = 0
                e.hurt1()

        if count2 >= 1:#player secondary attack
            if e.action2():
                count2 = 0
                damage = r.randint(15,30)
                e.hurt2(damage)

        if e.alive == False:#checking if enemy has any hp
            pygame.mouse.set_visible(False)
            del e#removes enemy from class
            c4a = True
            pygame.mixer.music.unload()
            start = True
            mini_boss = False
            gp10a()

        if p.alive == False:#checking if player has any hp
            pygame.mouse.set_visible(False)
            pygame.mixer.music.unload()
            start = True
            mini_boss = False
            gp10()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        mainClock.tick(30)
        pygame.display.update()

def gp10a():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("Well done for beating your first mini boss. The",1,grey)
    text2 = font.render("corridoor carries on ahead and the left. What do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("left",1,grey)
    text5 = font.render("carry on",1,grey)
    text6 = font.render("turn back",1,grey)
    

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text5,(90,70))
        surf.blit(text6,(90,100))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "carry on" and K_RETURN:
                    gp10b()
                elif user_text == "left" and K_RETURN:
                    gp11()#next thing
                elif user_text == "turn back" and K_RETURN:
                    gp9a()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp10a)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp10a
                        mapp(prev)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()


def gp10b():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)

    text = font.render("You have reached a dead end. you can only turn back",1,grey)
    
    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text3,(90,10))
        surf.blit(text6,(90,40))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    gp10a()


        mainClock.tick(30)
        pygame.display.update()

def gp11():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("The corridoor leads into a small chamber, there is a",1,grey)
    text2 = font.render("a slight glow to the right. What do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("look around",1,grey)
    text5 = font.render("go towards the light",1,grey)
    text6 = font.render("turn back",1,grey)
    

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text5,(90,70))
        surf.blit(text6,(90,100))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "look around" and K_RETURN:
                    gp11a()
                elif user_text == "go towards the light" and K_RETURN:
                    gp11b()
                elif user_text == "turn back" and K_RETURN:
                    gp10a()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp11)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp11
                        mapp(prev)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp11a():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("The floor has some weird markings on it but nothing",1,grey)
    text2 = font.render("dangerous. What do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("towards the light",1,grey)
    text6 = font.render("turn back",1,grey)
    

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text6,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "towards the light" and K_RETURN:
                    gp11b()
                elif user_text == "turn back" and K_RETURN:
                    gp11()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp11a)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp11a
                        mapp(prev)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp11b():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("The corridoor is dark but there is a wall in front of you",1,grey)
    text2 = font.render("and nothing to the right of you. What do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("right",1,grey)
    text6 = font.render("turn back",1,grey)
    

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text6,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "right" and K_RETURN:
                    gp11c()
                elif user_text == "turn back" and K_RETURN:
                    gp11a()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp11b)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp11b
                        mapp(prev)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()


def gp11c():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("You make your way down the corridoor and there is an",1,grey)
    text2 = font.render("opening to your left. What do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("left",1,grey)
    text5 = font.render("carry on",1,grey)
    text6 = font.render("turn back",1,grey)
    

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text5,(90,70))
        surf.blit(text6,(90,100))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "carry on" and K_RETURN:
                    gp11d()
                elif user_text == "left" and K_RETURN:
                    fbp()
                elif user_text == "turn back" and K_RETURN:
                    gp11b()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp11c)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp11c
                        mapp(prev)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()


def gp11d():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("The corridoor once again meets a deadend. there is an",1,grey)
    text2 = font.render("opening to your right. What do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("right",1,grey)
    text6 = font.render("turn back",1,grey)
    

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text6,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "right" and K_RETURN:
                    gp12()
                elif user_text == "turn back" and K_RETURN:
                    gp11c()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp11d)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp11d
                        mapp(prev)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()


def gp12():
    global start,general_combat
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("There is a doorway infront of you and a corridoor",1,grey)
    text2 = font.render("to your left. What do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("left",1,grey)
    text5 = font.render("carry on",1,grey)
    text6 = font.render("turn back",1,grey)
    

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text5,(90,70))
        surf.blit(text6,(90,100))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "carry on" and K_RETURN:
                    if c5 == False:#R11
                        pygame.mouse.set_visible(True)
                        pygame.mixer.music.unload()
                        start = False
                        general_combat = True
                        gp12C()
                    else:
                        gp12a()
                elif user_text == "left" and K_RETURN:
                    gp12b()#C9
                elif user_text == "turn back" and K_RETURN:
                    gp11d()#C8
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp12)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp12
                        mapp(prev)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()


def gp12C():
    global p,start,general_combat
    panel1 = pygame.image.load("Images/combat/combat_bottom.png")#not made by me
    enemy1 = pygame.image.load("Images/enemies/ghost.png")
    dodge = pygame.image.load("Images/other/dodge.png")

    e = b.enemy(885,400,150,3,enemy1,15)#creates an enemy instance in the enemy class
    panel = b.images(0,560,panel1,1.5)
    d = b.images(400,230,dodge,2)

    count = 0
    count1 = 0
    count2 = 0
    mcount = 0

    pressed = False

    p.hp = 100
    
    while True:
        check()
        surf.fill((45,45,45))
        panel.draw(surf)
        p.draw(surf)
        e.draw(surf)

        key = pygame.key.get_pressed()

        count += 1

        if count%15 == 0:#cooldown for primary
            count1 += 1

        if count%20 == 0:
            mcount += 1

        if count%60 == 0:#cooldown for secondary
            count2 += 1

        if mcount != 0 and pressed == False:
            d.draw(surf)
        
        if mcount != 0:
            if key[K_d]:
                mcount = 0
                pressed = True

        if count%30 == 0:
            mcount = 0
            if pressed == True:
                pressed = False
            else:
                damage = r.randint(1,e.strength)
                p.hurt1(damage)

        if count1 >= 1:#player primary attack, having it wait at least 1/2 a second between attacks
            if e.action():
                count1 = 0
                e.hurt1()

        if count2 >= 1:#player secondary attack
            if e.action2():
                count2 = 0
                damage = r.randint(15,30)
                e.hurt2(damage)

        if e.alive == False:#checking if enemy has any hp
            print("deleted")
            del e#removes enemy from class
            gp12Ca()

        if p.alive == False:#checking if player has any hp
            pygame.mixer.music.unload()
            start = True
            general_combat = False
            gp12()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        mainClock.tick(30)
        pygame.display.update()


def gp12Ca():
    global p,c5,start,general_combat
    panel1 = pygame.image.load("Images/combat/combat_bottom.png")#not made by me
    enemy1 = pygame.image.load("Images/enemies/ghost.png")
    dodge = pygame.image.load("Images/other/dodge.png")

    e = b.enemy(885,400,150,3,enemy1,15)#creates an enemy instance in the enemy class
    panel = b.images(0,560,panel1,1.5)
    d = b.images(400,230,dodge,2)

    count = 0
    count1 = 0
    count2 = 0
    mcount = 0

    pressed = False
    
    while True:
        check()
        surf.fill((45,45,45))
        panel.draw(surf)
        p.draw(surf)
        e.draw(surf)

        key = pygame.key.get_pressed()

        count += 1

        if count%15 == 0:#cooldown for primary
            count1 += 1

        if count%20 == 0:
            mcount += 1

        if count%60 == 0:#cooldown for secondary
            count2 += 1

        if mcount != 0 and pressed == False:
            d.draw(surf)
        
        if mcount != 0:
            if key[K_d]:
                mcount = 0
                pressed = True

        if count%30 == 0:
            mcount = 0
            if pressed == True:
                pressed = False
            else:
                damage = r.randint(1,e.strength)
                p.hurt1(damage)

        if count1 >= 1:#player primary attack, having it wait at least 1/2 a second between attacks
            if e.action():
                count1 = 0
                e.hurt1()

        if count2 >= 1:#player secondary attack
            if e.action2():
                count2 = 0
                damage = r.randint(15,30)
                e.hurt2(damage)

        if e.alive == False:#checking if enemy has any hp
            pygame.mouse.set_visible(False)
            del e#removes enemy from class
            c5 = True
            pygame.mixer.music.unload()
            start = True
            general_combat = False
            gp12a()#chest

        if p.alive == False:#checking if player has any hp
            pygame.mouse.set_visible(False)
            pygame.mixer.music.unload()
            start = True
            general_combat = False
            gp12()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        mainClock.tick(30)
        pygame.display.update()

def gp12a():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("A chest sits in the corner. what do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("open chest",1,grey)
    text6 = font.render("turn back",1,grey)
    

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text6,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "open chest" and K_RETURN:
                    gp12a1()
                elif user_text == "turn back" and K_RETURN:
                    gp12()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp12a)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp12a
                        mapp(prev)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp12a1():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)

    text = font.render("There is a red cape inside",1,yellow2)
    text2 = font.render("YOU WILL TAKE IT :)",1,red)
    
    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,630))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN and first == False:
                if K_RETURN:
                    gp12()

        first = False
        mainClock.tick(30)
        pygame.display.update()


def gp12b():
    global start,maze
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("There is an opening to your right and the corridoor",1,grey)
    text2 = font.render("carries on. what do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("carry on",1,grey)
    text5 = font.render("right",1,grey)
    text6 = font.render("turn back",1,grey)
    

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text5,(90,70))
        surf.blit(text6,(90,100))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "carry on" and K_RETURN:
                    gp12b1()#corridoor
                elif user_text == "right" and K_RETURN:
                    pygame.mixer.music.unload()
                    start = False
                    maze = True
                    gp13()#maze
                elif user_text == "turn back" and K_RETURN:
                    gp12()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp12b)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp12b
                        mapp(prev)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()


def gp13():
    global start,maze
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("You enter a dark room with wooden walls.",1,grey)
    text2 = font.render("what do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("carry on",1,grey)
    text6 = font.render("turn back",1,grey)
    

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text6,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "carry on" and K_RETURN:
                    gp13a()
                elif user_text == "turn back" and K_RETURN:
                    pygame.mixer.music.unload()
                    maze = False
                    start = True
                    gp12b()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp13)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp13
                        mapp(prev)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()


def gp13a():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("There is a doorway to your left and a wall",1,grey)
    text2 = font.render("in front of you and to your right. what do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text5 = font.render("left",1,grey)
    text6 = font.render("turn back",1,grey)
    

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        surf.blit(text3,(90,10))
        surf.blit(text5,(90,40))
        surf.blit(text6,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "left" and K_RETURN:
                    gp13a1()
                elif user_text == "turn back" and K_RETURN:
                    gp13()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp13a)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp13a
                        mapp(prev)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp13a1():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("There is an opening to your left and right",1,grey)
    text2 = font.render("what do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("left",1,grey)
    text5 = font.render("right",1,grey)
    text6 = font.render("turn back",1,grey)
    

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text5,(90,70))
        surf.blit(text6,(90,100))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "right" and K_RETURN:
                    gp13b()
                elif user_text == "left" and K_RETURN:
                    gp13a2()
                elif user_text == "turn back" and K_RETURN:
                    gp13a()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp13a1)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp13a1
                        mapp(prev)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp13b():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    text = font.render("There is nothing there but a wall",1,grey)    

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    gp13a1()
                else:
                    user_text += event.unicode


        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp13a2():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("You have reached a dead end, there is a",1,grey)
    text2 = font.render("path to your left. what do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text5 = font.render("left",1,grey)
    text6 = font.render("turn back",1,grey)
    

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        surf.blit(text3,(90,10))
        surf.blit(text5,(90,40))
        surf.blit(text6,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "left" and K_RETURN:
                    gp13a3()
                elif user_text == "turn back" and K_RETURN:
                    gp13a1()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp13a2)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp13a2
                        mapp(prev)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp13a3():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("The corridoor carries on in front of you",1,grey)
    text2 = font.render("what do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("carry on",1,grey)
    text6 = font.render("turn back",1,grey)
    

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text6,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "carry on" and K_RETURN:
                    gp13a4()
                elif user_text == "turn back" and K_RETURN:
                    gp13a2()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp13a3)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp13a3
                        mapp(prev)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp13a4():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("There is a hole to your right and the corridoor",1,grey)
    text2 = font.render("carries on. what do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("carry on",1,grey)
    text5 = font.render("right",1,grey)
    text6 = font.render("turn back",1,grey)
    

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text5,(90,70))
        surf.blit(text6,(90,100))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "carry on" and K_RETURN:
                    gp13c()
                elif user_text == "right" and K_RETURN:
                    gp13a5()
                elif user_text == "turn back" and K_RETURN:
                    gp13a3()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp13a4)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp13a4
                        mapp(prev)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp13c():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)

    text = font.render("Dead end -.-",1,grey)    

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    gp13a4()

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp13a5():
    global maze,mini_boss
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("You can hear heavy breathing infront of you",1,grey)
    text2 = font.render("what do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("carry on",1,grey)
    text6 = font.render("turn back",1,grey)
    

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text6,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "carry on" and K_RETURN:
                    if c5 == False:
                        pygame.mouse.set_visible(True)
                        pygame.mixer.music.unload()
                        maze = False
                        mini_boss = True
                        gp13C()
                    else:
                        gp13a7()
                elif user_text == "turn back" and K_RETURN:
                    gp13a4()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp13a5)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp13a5
                        mapp(prev)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp13C():
    global p,c5,maze,mini_boss
    panel1 = pygame.image.load("Images/combat/combat_bottom.png")#not made by me
    enemy1 = pygame.image.load("Images/enemies/red dragon.png")
    dodge = pygame.image.load("Images/other/dodge.png")

    e = b.enemy(900,315,250,15,enemy1,5.5)#creates an enemy instance in the enemy class
    panel = b.images(0,560,panel1,1.5)
    d = b.images(400,230,dodge,2)

    count = 0
    count1 = 0
    count2 = 0
    mcount = 0

    pressed = False

    p.hp = 100
    
    while True:
        check()
        surf.fill((45,45,45))
        panel.draw(surf)
        p.draw(surf)
        e.draw(surf)

        key = pygame.key.get_pressed()

        count += 1

        if count%15 == 0:#cooldown for primary
            count1 += 1

        if count%20 == 0:
            mcount += 1

        if count%60 == 0:#cooldown for secondary
            count2 += 1

        if mcount != 0 and pressed == False:
            d.draw(surf)
        
        if mcount != 0:
            if key[K_d]:
                mcount = 0
                pressed = True

        if count%30 == 0:
            mcount = 0
            if pressed == True:
                pressed = False
            else:
                damage = r.randint(1,e.strength)
                p.hurt1(damage)

        if count1 >= 1:#player primary attack, having it wait at least 1/2 a second between attacks
            if e.action():
                count1 = 0
                e.hurt1()

        if count2 >= 1:#player secondary attack
            if e.action2():
                count2 = 0
                damage = r.randint(15,30)
                e.hurt2(damage)

        if e.alive == False:#checking if enemy has any hp
            print("deleted")
            del e#removes enemy from class
            gp13C1()

        if p.alive == False:#checking if player has any hp
            pygame.mixer.music.unload()
            maze = True
            mini_boss = False
            gp13a5()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        mainClock.tick(30)
        pygame.display.update()

def gp13C1():
    global p,c5,maze,mini_boss
    panel1 = pygame.image.load("Images/combat/combat_bottom.png")#not made by me
    enemy1 = pygame.image.load("Images/enemies/purple dragon.png")
    dodge = pygame.image.load("Images/other/dodge.png")

    e = b.enemy(900,315,300,20,enemy1,5.5)#creates an enemy instance in the enemy class
    panel = b.images(0,560,panel1,1.5)
    d = b.images(400,230,dodge,2)

    count = 0
    count1 = 0
    count2 = 0
    mcount = 0

    pressed = False
    
    while True:
        check()
        surf.fill((45,45,45))
        panel.draw(surf)
        p.draw(surf)
        e.draw(surf)

        key = pygame.key.get_pressed()

        count += 1

        if count%15 == 0:#cooldown for primary
            count1 += 1

        if count%20 == 0:
            mcount += 1

        if count%60 == 0:#cooldown for secondary
            count2 += 1

        if mcount != 0 and pressed == False:
            d.draw(surf)
        
        if mcount != 0:
            if key[K_d]:
                mcount = 0
                pressed = True

        if count%30 == 0:
            mcount = 0
            if pressed == True:
                pressed = False
            else:
                damage = r.randint(1,e.strength)
                p.hurt1(damage)

        if count1 >= 1:#player primary attack, having it wait at least 1/2 a second between attacks
            if e.action():
                count1 = 0
                e.hurt1()

        if count2 >= 1:#player secondary attack
            if e.action2():
                count2 = 0
                damage = r.randint(15,30)
                e.hurt2(damage)

        if e.alive == False:#checking if enemy has any hp
            pygame.mouse.set_visible(False)
            del e#removes enemy from class
            c5 = True
            pygame.mixer.music.unload()
            maze = True
            mini_boss = False
            gp13a6()

        if p.alive == False:#checking if player has any hp
            pygame.mouse.set_visible(False)
            pygame.mixer.music.unload()
            maze = True
            mini_boss = False
            gp13a5()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        mainClock.tick(30)
        pygame.display.update()

def gp13a6():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)

    text = font.render("You have slain the dragon. there is a",1,grey)
    text2 = font.render("doorway in front of you",1,grey)    

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    gp13a7()
                
        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp13a7():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    text = font.render("You slowly walk down a dark corridoor",1,grey)
    text2 = font.render("Your footsteps bounce off the walls",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    gp13a8()

        first = False
        mainClock.tick(30)
        pygame.display.update()


def gp13a8():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    text = font.render("There is a big grey tent in front of you",1,grey)
    text2 = font.render("its covered in dust and the front is closed",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    gp13a9()

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp13a9():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    text = font.render("You open the zip to the tent and walk in",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    gp13a10()

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp13a10():
    bg1 = pygame.image.load("Images/backgrounds/tent.png")
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    text = font.render("The tent is almost empty",1,grey)
    text2 = font.render("A desk sits against the back wall",1,grey)

    bg = b.images(180,10,bg1,0.7)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    gp13a11()

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp13a11():
    bg1 = pygame.image.load("Images/backgrounds/tent.png")
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    text = font.render("You slowly walk towards the desk",1,grey)

    bg = b.images(180,10,bg1,0.7)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    gp13a12()

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp13a12():
    bg1 = pygame.image.load("Images/backgrounds/tent.png")
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    text = font.render("There is a book of some sort, damaged paper",1,grey)
    text2 = font.render("and loose sheets of paper",1,grey)

    bg = b.images(180,10,bg1,0.7)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    gp13a13()

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp13a13():
    bg1 = pygame.image.load("Images/backgrounds/tent.png")
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    text = font.render("You read the open pages",1,grey)

    bg = b.images(180,10,bg1,0.7)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    surf.fill((0,0,0))
                    gp13a14()

        first = False
        mainClock.tick(30)
        pygame.display.update()


def gp13a14():
    bg1 = pygame.image.load("Images/backgrounds/lore bg 1.png")
    bg = b.images(150,75,bg1,1)
    first = True
    mcount = 0
    count = 0
    while True:
        check()
        bg.draw(surf)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[K_RETURN] and count > 15:
            surf.fill((0,0,0))
            gp13a15()

        count += 1
        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp13a15():
    bg1 = pygame.image.load("Images/backgrounds/lore bg 2.png")
    bg = b.images(150,75,bg1,1)
    first = True
    mcount = 0
    count = 0
    while True:
        check()
        bg.draw(surf)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[K_RETURN] and count > 15:
            surf.fill((0,0,0))
            gp13a16()

        count += 1
        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp13a16():
    bg1 = pygame.image.load("Images/backgrounds/lore bg 3.png")
    bg = b.images(150,75,bg1,1)
    first = True
    mcount = 0
    count = 0
    while True:
        check()
        bg.draw(surf)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[K_RETURN] and count > 15:
            surf.fill((0,0,0))
            gp13a17()

        count += 1
        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp13a17():
    bg1 = pygame.image.load("Images/backgrounds/lore bg.png")
    bg = b.images(150,75,bg1,1)
    first = True
    while True:
        check()
        bg.draw(surf)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[K_RETURN] and first == False:
            surf.fill((0,0,0))
            gp13a18()

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp13a18():
    bg1 = pygame.image.load("Images/backgrounds/tent.png")
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    text = font.render("You get teleported back to the entrance",1,grey)
    text2 = font.render("of the maze",1,grey)

    bg = b.images(180,10,bg1,0.7)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    gp13()

        first = False
        mainClock.tick(30)
        pygame.display.update()
    

def gp12b1():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("There is a dead end in front of you and an opening",1,grey)
    text2 = font.render("to your left. what do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text5 = font.render("left",1,grey)
    text6 = font.render("turn back",1,grey)
    

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        surf.blit(text3,(90,10))
        surf.blit(text5,(90,40))
        surf.blit(text6,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "left" and K_RETURN:
                    gp12b2()#C10
                elif user_text == "turn back" and K_RETURN:
                    gp12b()#corridoor behind, close to maze entrance
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp12b1)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp12b1
                        mapp(prev)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp12b2():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("There is a dead end in front of you and an opening",1,grey)
    text2 = font.render("to your right. what do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text5 = font.render("right",1,grey)
    text6 = font.render("turn back",1,grey)
    

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        surf.blit(text3,(90,10))
        surf.blit(text5,(90,40))
        surf.blit(text6,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "right" and K_RETURN:
                    gp12b3()#C10
                elif user_text == "turn back" and K_RETURN:
                    gp12b()#corridoor behind, close to maze entrance
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp12b2)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp12b2
                        mapp(prev)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp12b3():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("There is a dead end in front of you and an opening",1,grey)
    text2 = font.render("to your right. what do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text5 = font.render("right",1,grey)
    text4 = font.render("left",1,grey)
    text6 = font.render("turn back",1,grey)
    

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        surf.blit(text3,(90,10))
        surf.blit(text5,(90,40))
        surf.blit(text4,(90,70))
        surf.blit(text6,(90,100))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "right" and K_RETURN:
                    gp14()#archeology room
                elif user_text == "left" and K_RETURN:
                    gp15()#corridoor for BR and R14
                elif user_text == "turn back" and K_RETURN:
                    gp12b2()
                elif user_text == "carry on" and K_RETURN:
                    gp12b4()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp12b3)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp12b3
                        mapp(prev)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()


def gp12b4():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)

    text = font.render("You have reached a deadend",1,grey)
        
    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    gp12b3()
                    
        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp14():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    text = font.render("The room is dark, but you go further in",1,grey)    

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    gp14a()

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp14a():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    text = font.render("It feels like you're walking through sand",1,grey)    

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    gp14b()

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp14b():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    text = font.render("You hit something with your foot, your foot hurts now",1,grey)
    text2 = font.render("You lean down to look at what it is",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text,(175,620))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    gp14c()

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp14c():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)

    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''
    
    text = font.render("Do you pick up the object?",1,grey)
    text2 = font.render("options",1,grey)
    text3 = font.render("yes",1,grey)
    text4 = font.render("no",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(90,10))
        surf.blit(text3,(90,40))
        surf.blit(text4,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "yes" and K_RETURN:
                    gp14d()
                elif user_text == "no" and K_RETURN:
                    gp12b3()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp14c)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()


def gp14d():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    text = font.render("the blob is a weird shape with random dips",1,red)
    text2 = font.render("its freezing",1,red)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    gp14e()

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp14e():
    global blob3
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    text = font.render("You put it in your bag",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    blob3 = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    gp12b3()

        first = False
        mainClock.tick(30)
        pygame.display.update()


def gp15():
    global start,final
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("There is an opening to your left, the room looks",1,grey)
    text2 = font.render("endless. The corridoor carries on. What do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("left",1,grey)
    text5 = font.render("carry on",1,grey)
    text6 = font.render("turn back",1,grey)
    

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text5,(90,70))
        surf.blit(text6,(90,100))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "left" and K_RETURN:
                    pygame.mixer.music.unload()
                    start = False
                    final = True
                    gp17()#BR
                elif user_text == "turn back" and K_RETURN:
                    gp12b3()
                elif user_text == "carry on" and K_RETURN:
                    gp15a()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp15)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp15
                        mapp(prev)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp15a():
    global start,general_combat
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("There is a wall in front of you and an opening to your",1,grey)
    text2 = font.render("right, it feels cold. What do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("right",1,grey)
    text6 = font.render("turn back",1,grey)
    

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text6,(90,100))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "right" and K_RETURN:
                    if c6 == False:
                        pygame.mouse.set_visible(True)
                        pygame.mixer.music.unload()
                        start = False
                        general_combat = True
                        gp16C()#R14
                    else:
                        gp16a()
                elif user_text == "turn back" and K_RETURN:
                    gp15()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp15a)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp15a
                        mapp(prev)
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp16C():
    global p,start,general_combat
    panel1 = pygame.image.load("Images/combat/combat_bottom.png")#not made by me
    enemy1 = pygame.image.load("Images/enemies/spider.png")
    dodge = pygame.image.load("Images/other/dodge.png")

    e = b.enemy(900,450,75,8,enemy1,3)#creates an enemy instance in the enemy class
    panel = b.images(0,560,panel1,1.5)
    d = b.images(400,230,dodge,2)

    count = 0
    count1 = 0
    count2 = 0
    mcount = 0

    pressed = False

    p.hp = 100
    
    while True:
        check()
        surf.fill((45,45,45))
        panel.draw(surf)
        p.draw(surf)
        e.draw(surf)

        key = pygame.key.get_pressed()

        count += 1

        if count%15 == 0:#cooldown for primary
            count1 += 1

        if count%20 == 0:
            mcount += 1

        if count%60 == 0:#cooldown for secondary
            count2 += 1

        if mcount != 0 and pressed == False:
            d.draw(surf)
        
        if mcount != 0:
            if key[K_d]:
                mcount = 0
                pressed = True

        if count%30 == 0:
            mcount = 0
            if pressed == True:
                pressed = False
            else:
                damage = r.randint(1,e.strength)
                p.hurt1(damage)

        if count1 >= 1:#player primary attack, having it wait at least 1/2 a second between attacks
            if e.action():
                count1 = 0
                e.hurt1()

        if count2 >= 1:#player secondary attack
            if e.action2():
                count2 = 0
                damage = r.randint(15,30)
                e.hurt2(damage)

        if e.alive == False:#checking if enemy has any hp
            print("deleted")
            del e#removes enemy from class
            gp16C1()

        if p.alive == False:#checking if player has any hp
            pygame.mixer.music.unload()
            start = True
            general_combat = False
            gp15a()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        mainClock.tick(30)
        pygame.display.update()

def gp16C1():
    global p,c6,start,general_combat
    panel1 = pygame.image.load("Images/combat/combat_bottom.png")#not made by me
    enemy1 = pygame.image.load("Images/enemies/spider.png")
    dodge = pygame.image.load("Images/other/dodge.png")

    e = b.enemy(900,450,80,8,enemy1,3)#creates an enemy instance in the enemy class
    panel = b.images(0,560,panel1,1.5)
    d = b.images(400,230,dodge,2)

    count = 0
    count1 = 0
    count2 = 0
    mcount = 0

    pressed = False
    
    while True:
        check()
        surf.fill((45,45,45))
        panel.draw(surf)
        p.draw(surf)
        e.draw(surf)

        key = pygame.key.get_pressed()

        count += 1

        if count%15 == 0:#cooldown for primary
            count1 += 1

        if count%20 == 0:
            mcount += 1

        if count%60 == 0:#cooldown for secondary
            count2 += 1

        if mcount != 0 and pressed == False:
            d.draw(surf)
        
        if mcount != 0:
            if key[K_d]:
                mcount = 0
                pressed = True

        if count%30 == 0:
            mcount = 0
            if pressed == True:
                pressed = False
            else:
                damage = r.randint(1,e.strength)
                p.hurt1(damage)

        if count1 >= 1:#player primary attack, having it wait at least 1/2 a second between attacks
            if e.action():
                count1 = 0
                e.hurt1()

        if count2 >= 1:#player secondary attack
            if e.action2():
                count2 = 0
                damage = r.randint(15,30)
                e.hurt2(damage)

        if e.alive == False:#checking if enemy has any hp
            pygame.mouse.set_visible(False)
            del e#removes enemy from class
            c6 = True
            pygame.mixer.music.unload()
            start = True
            general_combat = False
            gp16a()

        if p.alive == False:#checking if player has any hp
            pygame.mouse.set_visible(False)
            pygame.mixer.music.unload()
            start = True
            general_combat = False
            gp15a()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        mainClock.tick(30)
        pygame.display.update()

def gp16a():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    text = font.render("Your feet slide, the spiders bodies are crushed",1,grey)
    text2 = font.render("against the far wall. You leave the empty room",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    gp15a()

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp17():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)

    text = font.render("You enter an impossibly big room with low lighting",1,grey)
    
    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    gp17a()

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp17a():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)

    text = font.render("There is a bookshelf against the wall but its too",1,grey)
    text2 = font.render("dark to see any of the titles",1,grey)
    
    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    gp17b()

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp17b():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)

    text = font.render("You reach out and feel a circular wall on one",1,grey)
    text2 = font.render("side and a straight wall on the other",1,grey)
    
    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    gp17c()

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp17c():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)

    text = font.render("You follow the straight wall",1,grey)
    
    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    gp17d()

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp17d():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)

    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("The area opens up and there are 2 options. You can",1,grey)
    text2 = font.render("either follow the circle or the straight wall. which one?",1,grey)

    text3 = font.render("Options:",1,grey)
    text4 = font.render("circle",1,grey)
    text6 = font.render("straight",1,grey)

    
    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text6,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "circle" and K_RETURN:
                    gp17e()
                elif user_text == "straight" and K_RETURN:
                    if c7 == True:
                        pass
                    else:
                        gp18()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp17d)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp17d
                        mapp(prev)
                    else:
                        pass
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)


        first = False
        mainClock.tick(30)
        pygame.display.update()


def gp18():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("The path infront of you is dark and",1,grey)
    text2 = font.render("is the floor feels uneven. What do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("walk",1,grey)
    text5 = font.render("run",1,grey)
    text6 = font.render("hit floor",1,grey)
    
    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text5,(90,70))
        surf.blit(text6,(90,100))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "walk" and K_RETURN:
                    death3()
                elif user_text == "run" and K_RETURN:
                    gp18a()
                elif user_text == "hit floor" and K_RETURN:
                    gp18b()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp18)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp18
                        mapp(prev)
                    else:
                        pass
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp18a():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)

    text = font.render("You feel a wave of heat behind you and the tunnel",1,grey)
    text2 = font.render("infront of you gets bathed in light. It quickly disappears",1,grey)
    
    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    gp18a1()

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp18a1():
    global final,general_combat
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)

    text = font.render("An eerie laugh echoes somewhere ahead",1,grey)
    text2 = font.render("but you continue walking",1,grey)
    
    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    pygame.mouse.set_visible(True)
                    pygame.mixer.music.unload()
                    final = False
                    general_combat = True
                    gp18aC()

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp18aC():
    global p,c7,final,general_combat
    panel1 = pygame.image.load("Images/combat/combat_bottom.png")#not made by me
    enemy1 = pygame.image.load("Images/enemies/pirate.png")
    dodge = pygame.image.load("Images/other/dodge.png")

    e = b.enemy(900,300,100,10,enemy1,10)#creates an enemy instance in the enemy class
    panel = b.images(0,560,panel1,1.5)
    d = b.images(400,230,dodge,2)

    count = 0
    count1 = 0
    count2 = 0
    mcount = 0

    pressed = False

    p.hp = 100
    
    while True:
        check()
        surf.fill((45,45,45))
        panel.draw(surf)
        p.draw(surf)
        e.draw(surf)

        key = pygame.key.get_pressed()

        count += 1

        if count%15 == 0:#cooldown for primary
            count1 += 1

        if count%20 == 0:
            mcount += 1

        if count%60 == 0:#cooldown for secondary
            count2 += 1

        if mcount != 0 and pressed == False:
            d.draw(surf)
        
        if mcount != 0:
            if key[K_d]:
                mcount = 0
                pressed = True

        if count%30 == 0:
            mcount = 0
            if pressed == True:
                pressed = False
            else:
                damage = r.randint(1,e.strength)
                p.hurt1(damage)

        if count1 >= 1:#player primary attack, having it wait at least 1/2 a second between attacks
            if e.action():
                count1 = 0
                e.hurt1()

        if count2 >= 1:#player secondary attack
            if e.action2():
                count2 = 0
                damage = r.randint(15,30)
                e.hurt2(damage)

        if e.alive == False:#checking if enemy has any hp
            pygame.mouse.set_visible(False)
            del e#removes enemy from class
            c7 = True
            pygame.mixer.music.unload()
            final = True
            general_combat = False
            gp18a3()

        if p.alive == False:#checking if player has any hp
            pygame.mouse.set_visible(False)
            pygame.mixer.music.unload()
            final = True
            general_combat = False
            gp18a2()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        mainClock.tick(30)
        pygame.display.update()

def gp18a3():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)

    text = font.render("Behind the body of the pirate is a chest",1,grey)
    
    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    gp18a4()

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp18a4():
    global key
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)

    text = font.render("You slowly open the chest and there is a key.",1,grey)
    text2 = font.render("I wonder what this is for... maybe a door...",1,grey)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    key = True
                    gp17d()

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp18a5():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)

    text = font.render("You put the key in your pocket and leave",1,grey)
    
    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    gp17d()

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp18b():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("A second after you hit the floor flames come out but miss",1,grey)
    text2 = font.render("you, it comes from a small square on the floor. What do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("walk",1,grey)
    text5 = font.render("run",1,grey)
    text6 = font.render("hit floor",1,grey)
    
    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text5,(90,70))
        surf.blit(text6,(90,100))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "walk" and K_RETURN:
                    death3()
                elif user_text == "run" and K_RETURN:
                    gp18a()
                elif user_text == "hit floor" and K_RETURN:
                    gp18b()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(gp18b)
                elif user_text == "map" and K_RETURN:
                    if Map == True:
                        prev = gp18b
                        mapp(prev)
                    else:
                        pass
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp17e():
    global final,mini_boss
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)

    text = font.render("There is a faint hissing but you carry on",1,grey)
    
    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    pygame.mouse.set_visible(True)
                    pygame.mixer.music.unload()
                    final = False
                    mini_boss = True
                    gp17C()

        first = False
        mainClock.tick(30)
        pygame.display.update()

def gp17C():
    global p,final,mini_boss
    panel1 = pygame.image.load("Images/combat/combat_bottom.png")#not made by me
    enemy1 = pygame.image.load("Images/enemies/green snek.png")
    dodge = pygame.image.load("Images/other/dodge.png")

    e = b.enemy(885,400,80,8,enemy1,7)
    panel = b.images(0,560,panel1,1.5)
    d = b.images(400,230,dodge,2)

    count = 0
    count1 = 0
    count2 = 0
    mcount = 0

    pressed = False

    p.hp = 100
    
    while True:
        check()
        surf.fill((45,45,45))
        panel.draw(surf)
        p.draw(surf)
        e.draw(surf)

        key = pygame.key.get_pressed()

        count += 1

        if count%15 == 0:#cooldown for primary
            count1 += 1

        if count%20 == 0:
            mcount += 1

        if count%60 == 0:#cooldown for secondary
            count2 += 1

        if mcount != 0 and pressed == False:
            d.draw(surf)
        
        if mcount != 0:
            if key[K_d]:
                mcount = 0
                pressed = True

        if count%30 == 0:
            mcount = 0
            if pressed == True:
                pressed = False
            else:
                damage = r.randint(1,e.strength)
                p.hurt1(damage)

        if count1 >= 1:#player primary attack, having it wait at least 1/2 a second between attacks
            if e.action():
                count1 = 0
                e.hurt1()

        if count2 >= 1:#player secondary attack
            if e.action2():
                count2 = 0
                damage = r.randint(15,30)
                e.hurt2(damage)

        if e.alive == False:#checking if enemy has any hp
            del e#removes enemy from class
            pygame.mouse.set_visible(True)
            gp17C1()

        if p.alive == False:#checking if player has any hp
            pygame.mixer.music.unload()
            final = True
            mini_boss = False
            gp17e()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        mainClock.tick(30)
        pygame.display.update()

def gp17C1():
    global p,final,mini_boss
    panel1 = pygame.image.load("Images/combat/combat_bottom.png")#not made by me
    enemy1 = pygame.image.load("Images/enemies/blue snek.png")
    dodge = pygame.image.load("Images/other/dodge.png")

    e = b.enemy(885,400,90,8,enemy1,7)
    panel = b.images(0,560,panel1,1.5)
    d = b.images(400,230,dodge,2)

    count = 0
    count1 = 0
    count2 = 0
    mcount = 0

    pressed = False

    while True:
        check()
        surf.fill((45,45,45))
        panel.draw(surf)
        p.draw(surf)
        e.draw(surf)

        key = pygame.key.get_pressed()

        count += 1

        if count%15 == 0:#cooldown for primary
            count1 += 1

        if count%20 == 0:
            mcount += 1

        if count%60 == 0:#cooldown for secondary
            count2 += 1

        if mcount != 0 and pressed == False:
            d.draw(surf)
        
        if mcount != 0:
            if key[K_d]:
                mcount = 0
                pressed = True

        if count%30 == 0:
            mcount = 0
            if pressed == True:
                pressed = False
            else:
                damage = r.randint(1,e.strength)
                p.hurt1(damage)

        if count1 >= 1:#player primary attack, having it wait at least 1/2 a second between attacks
            if e.action():
                count1 = 0
                e.hurt1()

        if count2 >= 1:#player secondary attack
            if e.action2():
                count2 = 0
                damage = r.randint(15,30)
                e.hurt2(damage)

        if e.alive == False:#checking if enemy has any hp
            pygame.mouse.set_visible(True)
            del e#removes enemy from class
            gp17C2()

        if p.alive == False:#checking if player has any hp
            pygame.mixer.music.unload()
            final = True
            mini_boss = False
            gp17e()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        mainClock.tick(30)
        pygame.display.update()

def gp17C2():
    global p,c8,final,mini_boss
    panel1 = pygame.image.load("Images/combat/combat_bottom.png")#not made by me
    enemy1 = pygame.image.load("Images/enemies/purple snek.png")
    dodge = pygame.image.load("Images/other/dodge.png")

    e = b.enemy(885,400,80,8,enemy1,7)
    panel = b.images(0,560,panel1,1.5)
    d = b.images(400,230,dodge,2)

    count = 0
    count1 = 0
    count2 = 0
    mcount = 0

    pressed = False
    
    while True:
        check()
        surf.fill((45,45,45))
        panel.draw(surf)
        p.draw(surf)
        e.draw(surf)

        key = pygame.key.get_pressed()

        count += 1

        if count%15 == 0:#cooldown for primary
            count1 += 1

        if count%20 == 0:
            mcount += 1

        if count%60 == 0:#cooldown for secondary
            count2 += 1

        if mcount != 0 and pressed == False:
            d.draw(surf)
        
        if mcount != 0:
            if key[K_d]:
                mcount = 0
                pressed = True

        if count%30 == 0:
            mcount = 0
            if pressed == True:
                pressed = False
            else:
                damage = r.randint(1,e.strength)
                p.hurt1(damage)

        if count1 >= 1:#player primary attack, having it wait at least 1/2 a second between attacks
            if e.action():
                count1 = 0
                e.hurt1()

        if count2 >= 1:#player secondary attack
            if e.action2():
                count2 = 0
                damage = r.randint(15,30)
                e.hurt2(damage)

        if e.alive == False:#checking if enemy has any hp
            del e#removes enemy from class
            c8 = True
            pygame.mouse.set_visible(False)
            pygame.mixer.music.unload()
            final = True
            mini_boss = False
            gp17f()

        if p.alive == False:#checking if player has any hp
            pygame.mixer.music.unload()
            final = True
            mini_boss = False
            gp17e()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        mainClock.tick(30)
        pygame.display.update()

def gp17f():
    global start,final
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)

    text = font.render("There is nothing but empty barrels and an",1,grey)
    text2 = font.render("upside down chest, so you leave the BRs",1,grey)
    
    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    pygame.mixer.music.unload()
                    start = True
                    final = False
                    gp15()

        first = False
        mainClock.tick(30)
        pygame.display.update()




def fbp():
    global start,final
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    input_rect = pygame.Rect(175,680,600,60)
    colour = pygame.Color("lightslategray")
    user_text = ''

    text = font.render("There is a locked door in front of you. What do you do?",1,grey)
    
    text3 = font.render("Options:",1,grey)
    text4 = font.render("open the door",1,grey)
    text6 = font.render("turn back",1,grey)
    

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text3,(90,10))
        surf.blit(text4,(90,40))
        surf.blit(text6,(90,70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == "open the door" and K_RETURN:
                    if key == True:
                        pygame.mixer.music.unload()
                        final = True
                        start = False
                        fb1()
                    else:
                        fbp1()
                elif user_text == "settings" and K_RETURN:
                    running_options_menu(fbp)
                elif user_text == "turn back" and K_RETURN:
                    gp11c()
                else:
                    user_text += event.unicode

        pygame.draw.rect(surf,colour,input_rect,2)
        text_surf = base_font.render(user_text,True,(white))
        surf.blit(text_surf,(input_rect.x + 12, input_rect.y + 12))
        input_rect.w = max(500,text_surf.get_width() + 15)

        first = False
        mainClock.tick(30)
        pygame.display.update()


def fbp1():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)
    
    text = font.render("The door is locked. Why would the only door be",1,grey)
    text2 = font.render("unlocked? you have to find something that can open it",1,grey)    

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text2,(175,620))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                elif K_RETURN:
                    gp11c()

        first = False
        mainClock.tick(30)
        pygame.display.update()


def fb1():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)

    text = font.render("The key fits the lock and unlocks the door",1,grey)
    
    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    fb2()

        first = False
        mainClock.tick(30)
        pygame.display.update()

def fb2():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)

    text = font.render("You walk up the stairs and see a figure",1,grey)
    text2 = font.render("lurking in the darkness",1,grey)
    
    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        check()
        surf.fill((0,0,0))
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    fbS1()

        first = False
        mainClock.tick(30)
        pygame.display.update()

def fbS1():
    Txt1 = pygame.image.load("Images/textboxes/txt34.png")
    p1 = pygame.image.load("Images/characters/player_dark.png")
    m1 = pygame.image.load("Images/other/mystery.png")

    p = b.images(25,205,p1,10)
    m = b.images(775,300,m1,3.5)
    first = True
    count = 0

    while True:
        check()
        surf.fill((0,0,0))
        surf.blit(Txt1,(150,580))
        p.draw(surf)
        m.draw(surf)
        
        keys = pygame.key.get_pressed()
        
        if keys[K_RETURN] and count > 15:
            fbS2()#selected prefrog

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        first = False
        mainClock.tick(30)
        pygame.display.update()

def fbS2():
    Txt1 = pygame.image.load("Images/textboxes/txt35.png")
    p1 = pygame.image.load("Images/characters/player_dark.png")
    m1 = pygame.image.load("Images/other/mystery.png")

    p = b.images(25,205,p1,10)
    m = b.images(775,300,m1,3.5)
    first = True

    count = 0

    while True:
        check()
        surf.fill((0,0,0))
        surf.blit(Txt1,(150,580))
        p.draw(surf)
        m.draw(surf)
        
        keys = pygame.key.get_pressed()
        
        if keys[K_RETURN] and count > 15:
            fbS3()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        first = False
        mainClock.tick(30)
        pygame.display.update()

def fbS3():
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    p1 = pygame.image.load("Images/characters/player.png")
    m1 = pygame.image.load("Images/other/mystery.png")
    font = pygame.font.SysFont("comicsans",30,True)

    p = b.images(25,205,p1,10)
    m = b.images(775,300,m1,3.5)
    txtb = b.images(150,580,txtb1,1)

    text = font.render("You move closer towards the figure",1,grey)
    
    first = True
    count = 0

    while True:
        check()
        surf.fill((0,0,0))
        txtb.draw(surf)
        p.draw(surf)
        m.draw(surf)
        surf.blit(text,(175,590))
        
        keys = pygame.key.get_pressed()
        
        if keys[K_RETURN] and count > 15:
            fbS4()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        first = False
        mainClock.tick(30)
        pygame.display.update()

def fbS4():
    Txt1 = pygame.image.load("Images/textboxes/txt36.png")
    p1 = pygame.image.load("Images/characters/player_dark.png")
    m1 = pygame.image.load("Images/enemies/prefrog_sel.png")

    p = b.images(25,205,p1,10)
    m = b.images(735,230,m1,0.45)
    first = True
    count = 0

    while True:
        check()
        surf.fill((0,0,0))
        surf.blit(Txt1,(150,580))
        p.draw(surf)
        m.draw(surf)
        
        keys = pygame.key.get_pressed()
        
        if keys[K_RETURN] and count > 15:
            fbS5()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        first = False
        mainClock.tick(30)
        pygame.display.update()

def fbS5():
    Txt1 = pygame.image.load("Images/textboxes/txt37.png")
    p1 = pygame.image.load("Images/characters/player.png")
    m1 = pygame.image.load("Images/enemies/prefrog.png")

    p = b.images(25,205,p1,10)
    m = b.images(735,230,m1,0.25)
    first = True
    count = 0

    while True:
        check()
        surf.fill((0,0,0))
        surf.blit(Txt1,(150,580))
        p.draw(surf)
        m.draw(surf)
        
        keys = pygame.key.get_pressed()
        
        if keys[K_RETURN] and count > 15:
            fbS6()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        first = False
        mainClock.tick(30)
        pygame.display.update()

def fbS6():
    global final, final_boss,start
    Txt1 = pygame.image.load("Images/textboxes/txt38.png")
    p1 = pygame.image.load("Images/characters/player_dark.png")
    m1 = pygame.image.load("Images/enemies/prefrog_sel.png")

    p = b.images(25,205,p1,10)
    m = b.images(735,230,m1,0.45)
    first = True
    count = 0

    while True:
        check()
        surf.fill((0,0,0))
        surf.blit(Txt1,(150,580))
        p.draw(surf)
        m.draw(surf)
        
        keys = pygame.key.get_pressed()
        
        if keys[K_RETURN] and count > 15:
            pygame.mouse.set_visible(True)
            pygame.mixer.music.unload()
            final = False
            start = False
            final_boss = True
            fbC1()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        first = False
        mainClock.tick(30)
        pygame.display.update()

def fbC1():
    global p,final,final_boss
    panel1 = pygame.image.load("Images/combat/combat_bottom.png")#not made by me
    enemy1 = pygame.image.load("Images/enemies/prefrog.png")
    dodge = pygame.image.load("Images/other/dodge.png")

    e = b.enemy(885,400,25,1,enemy1,0.25)
    panel = b.images(0,560,panel1,1.5)
    d = b.images(400,230,dodge,2)

    count = 0
    count1 = 0
    count2 = 0
    mcount = 0

    pressed = False

    p.hp = 100
    
    while True:
        check()
        surf.fill((45,45,45))
        panel.draw(surf)
        p.draw(surf)
        e.draw(surf)

        key = pygame.key.get_pressed()

        count += 1

        if count%15 == 0:#cooldown for primary
            count1 += 1

        if count%20 == 0:
            mcount += 1

        if count%60 == 0:#cooldown for secondary
            count2 += 1

        if mcount != 0 and pressed == False:
            d.draw(surf)
        
        if mcount != 0:
            if key[K_d]:
                mcount = 0
                pressed = True

        if count%30 == 0:
            mcount = 0
            if pressed == True:
                pressed = False
            else:
                damage = r.randint(1,e.strength)
                p.hurt1(damage)

        if count1 >= 1:#player primary attack, having it wait at least 1/2 a second between attacks
            if e.action():
                count1 = 0
                e.hurt1()

        if count2 >= 1:#player secondary attack
            if e.action2():
                count2 = 0
                damage = r.randint(15,30)
                e.hurt2(damage)

        if e.alive == False:#checking if enemy has any hp
            del e#removes enemy from class
            fbC2()

        if p.alive == False:#checking if player has any hp
            pygame.mixer.music.unload()
            final = True
            final_boss = False
            fbS6()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        mainClock.tick(30)
        pygame.display.update()

def fbC2():
    global p,final,final_boss
    panel1 = pygame.image.load("Images/combat/combat_bottom.png")#not made by me
    enemy1 = pygame.image.load("Images/enemies/frog.png")
    dodge = pygame.image.load("Images/other/dodge.png")

    e = b.enemy(900,510,40,2,enemy1,3)
    panel = b.images(0,560,panel1,1.5)
    d = b.images(400,230,dodge,2)

    count = 0
    count1 = 0
    count2 = 0
    mcount = 0

    pressed = False

    while True:
        check()
        surf.fill((45,45,45))
        panel.draw(surf)
        p.draw(surf)
        e.draw(surf)

        key = pygame.key.get_pressed()

        count += 1

        if count%15 == 0:#cooldown for primary
            count1 += 1

        if count%20 == 0:
            mcount += 1

        if count%60 == 0:#cooldown for secondary
            count2 += 1

        if mcount != 0 and pressed == False:
            d.draw(surf)
        
        if mcount != 0:
            if key[K_d]:
                mcount = 0
                pressed = True

        if count%30 == 0:
            mcount = 0
            if pressed == True:
                pressed = False
            else:
                damage = r.randint(1,e.strength)
                p.hurt1(damage)

        if count1 >= 1:#player primary attack, having it wait at least 1/2 a second between attacks
            if e.action():
                count1 = 0
                e.hurt1()

        if count2 >= 1:#player secondary attack
            if e.action2():
                count2 = 0
                damage = r.randint(15,30)
                e.hurt2(damage)

        if e.alive == False:#checking if enemy has any hp
            del e#removes enemy from class
            fbC3()

        if p.alive == False:#checking if player has any hp
            pygame.mixer.music.unload()
            final = True
            final_boss = False
            fbS6()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        mainClock.tick(30)
        pygame.display.update()

def fbC3():
    global p,final,final_boss
    panel1 = pygame.image.load("Images/combat/combat_bottom.png")#not made by me
    enemy1 = pygame.image.load("Images/enemies/frog1.png")
    dodge = pygame.image.load("Images/other/dodge.png")

    e = b.enemy(900,510,50,4,enemy1,2)
    panel = b.images(0,560,panel1,1.5)
    d = b.images(400,230,dodge,2)

    count = 0
    count1 = 0
    count2 = 0
    mcount = 0
    
    pressed = False

    while True:
        check()
        surf.fill((45,45,45))
        panel.draw(surf)
        p.draw(surf)
        e.draw(surf)

        key = pygame.key.get_pressed()

        count += 1

        if count%15 == 0:#cooldown for primary
            count1 += 1

        if count%20 == 0:
            mcount += 1

        if count%60 == 0:#cooldown for secondary
            count2 += 1

        if mcount != 0 and pressed == False:
            d.draw(surf)
        
        if mcount != 0:
            if key[K_d]:
                mcount = 0
                pressed = True

        if count%30 == 0:
            mcount = 0
            if pressed == True:
                pressed = False
            else:
                damage = r.randint(1,e.strength)
                p.hurt1(damage)

        if count1 >= 1:#player primary attack, having it wait at least 1/2 a second between attacks
            if e.action():
                count1 = 0
                e.hurt1()

        if count2 >= 1:#player secondary attack
            if e.action2():
                count2 = 0
                damage = r.randint(15,30)
                e.hurt2(damage)

        if e.alive == False:#checking if enemy has any hp
            del e#removes enemy from class
            fbC4()

        if p.alive == False:#checking if player has any hp
            pygame.mixer.music.unload()
            final = True
            final_boss = False
            fbS6()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        mainClock.tick(30)
        pygame.display.update()

def fbC4():
    global p,final,final_boss
    panel1 = pygame.image.load("Images/combat/combat_bottom.png")#not made by me
    enemy1 = pygame.image.load("Images/enemies/frog2.png")
    dodge = pygame.image.load("Images/other/dodge.png")

    e = b.enemy(900,500,75,10,enemy1,2.5)
    panel = b.images(0,560,panel1,1.5)
    d = b.images(400,230,dodge,2)

    count = 0
    count1 = 0
    count2 = 0
    mcount = 0
    
    pressed = False

    while True:
        check()
        surf.fill((45,45,45))
        panel.draw(surf)
        p.draw(surf)
        e.draw(surf)

        key = pygame.key.get_pressed()

        count += 1

        if count%15 == 0:#cooldown for primary
            count1 += 1

        if count%20 == 0:
            mcount += 1

        if count%60 == 0:#cooldown for secondary
            count2 += 1

        if mcount != 0 and pressed == False:
            d.draw(surf)
        
        if mcount != 0:
            if key[K_d]:
                mcount = 0
                pressed = True

        if count%30 == 0:
            mcount = 0
            if pressed == True:
                pressed = False
            else:
                damage = r.randint(1,e.strength)
                p.hurt1(damage)

        if count1 >= 1:#player primary attack, having it wait at least 1/2 a second between attacks
            if e.action():
                count1 = 0
                e.hurt1()

        if count2 >= 1:#player secondary attack
            if e.action2():
                count2 = 0
                damage = r.randint(15,30)
                e.hurt2(damage)

        if e.alive == False:#checking if enemy has any hp
            del e#removes enemy from class
            fbC5()

        if p.alive == False:#checking if player has any hp
            pygame.mixer.music.unload()
            final = True
            final_boss = False
            fbS6()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        mainClock.tick(30)
        pygame.display.update()

def fbC5():
    global p,final,final_boss
    panel1 = pygame.image.load("Images/combat/combat_bottom.png")#not made by me
    enemy1 = pygame.image.load("Images/enemies/frog3.png")
    dodge = pygame.image.load("Images/other/dodge.png")

    e = b.enemy(900,490,100,12,enemy1,3)
    panel = b.images(0,560,panel1,1.5)
    d = b.images(400,230,dodge,2)

    count = 0
    count1 = 0
    count2 = 0
    mcount = 0
    
    pressed = False

    while True:
        check()
        surf.fill((45,45,45))
        panel.draw(surf)
        p.draw(surf)
        e.draw(surf)

        key = pygame.key.get_pressed()

        count += 1

        if count%15 == 0:#cooldown for primary
            count1 += 1

        if count%20 == 0:
            mcount += 1

        if count%60 == 0:#cooldown for secondary
            count2 += 1

        if mcount != 0 and pressed == False:
            d.draw(surf)
        
        if mcount != 0:
            if key[K_d]:
                mcount = 0
                pressed = True

        if count%30 == 0:
            mcount = 0
            if pressed == True:
                pressed = False
            else:
                damage = r.randint(1,e.strength)
                p.hurt1(damage)

        if count1 >= 1:#player primary attack, having it wait at least 1/2 a second between attacks
            if e.action():
                count1 = 0
                e.hurt1()

        if count2 >= 1:#player secondary attack
            if e.action2():
                count2 = 0
                damage = r.randint(15,30)
                e.hurt2(damage)

        if e.alive == False:#checking if enemy has any hp
            del e#removes enemy from class
            fbC6()

        if p.alive == False:#checking if player has any hp
            pygame.mixer.music.unload()
            final = True
            final_boss = False
            fbS6()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        mainClock.tick(30)
        pygame.display.update()

def fbC6():
    global p,final,final_boss
    panel1 = pygame.image.load("Images/combat/combat_bottom.png")#not made by me
    enemy1 = pygame.image.load("Images/enemies/frog4.png")
    dodge = pygame.image.load("Images/other/dodge.png")

    e = b.enemy(900,410,150,15,enemy1,7)
    panel = b.images(0,560,panel1,1.5)
    d = b.images(400,230,dodge,2)

    count = 0
    count1 = 0
    count2 = 0
    mcount = 0
    
    pressed = False

    while True:
        check()
        surf.fill((45,45,45))
        panel.draw(surf)
        p.draw(surf)
        e.draw(surf)

        key = pygame.key.get_pressed()

        count += 1

        if count%15 == 0:#cooldown for primary
            count1 += 1

        if count%20 == 0:
            mcount += 1

        if count%60 == 0:#cooldown for secondary
            count2 += 1

        if mcount != 0 and pressed == False:
            d.draw(surf)
        
        if mcount != 0:
            if key[K_d]:
                mcount = 0
                pressed = True

        if count%30 == 0:
            mcount = 0
            if pressed == True:
                pressed = False
            else:
                damage = r.randint(1,e.strength)
                p.hurt1(damage)

        if count1 >= 1:#player primary attack, having it wait at least 1/2 a second between attacks
            if e.action():
                count1 = 0
                e.hurt1()

        if count2 >= 1:#player secondary attack
            if e.action2():
                count2 = 0
                damage = r.randint(15,30)
                e.hurt2(damage)

        if e.alive == False:#checking if enemy has any hp
            del e#removes enemy from class
            fbC7()

        if p.alive == False:#checking if player has any hp
            pygame.mixer.music.unload()
            final = True
            final_boss = False
            fbS6()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        mainClock.tick(30)
        pygame.display.update()

def fbC7():
    global p,final_boss,frog_death,final
    panel1 = pygame.image.load("Images/combat/combat_bottom.png")#not made by me
    enemy1 = pygame.image.load("Images/enemies/frog5.png")
    dodge = pygame.image.load("Images/other/dodge.png")

    e = b.enemy(820,340,300,20,enemy1,7.5)
    panel = b.images(0,560,panel1,1.5)
    d = b.images(400,230,dodge,2)

    count = 0
    count1 = 0
    count2 = 0
    mcount = 0
    
    pressed = False

    while True:
        check()
        surf.fill((45,45,45))
        panel.draw(surf)
        p.draw(surf)
        e.draw(surf)

        key = pygame.key.get_pressed()

        count += 1

        if count%15 == 0:#cooldown for primary
            count1 += 1

        if count%20 == 0:
            mcount += 1

        if count%60 == 0:#cooldown for secondary
            count2 += 1

        if mcount != 0 and pressed == False:
            d.draw(surf)
        
        if mcount != 0:
            if key[K_d]:
                mcount = 0
                pressed = True

        if count%30 == 0:
            mcount = 0
            if pressed == True:
                pressed = False
            else:
                damage = r.randint(1,e.strength)
                p.hurt1(damage)

        if count1 >= 1:#player primary attack, having it wait at least 1/2 a second between attacks
            if e.action():
                count1 = 0
                e.hurt1()

        if count2 >= 1:#player secondary attack
            if e.action2():
                count2 = 0
                damage = r.randint(15,30)
                e.hurt2(damage)

        if e.alive == False:#checking if enemy has any hp
            del e#removes enemy from class
            pygame.mixer.music.unload()
            final_boss = False
            frog_death = True
            fbS7()

        if p.alive == False:#checking if player has any hp
            pygame.mixer.music.unload()
            final = True
            final_boss = False
            fbS6()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        mainClock.tick(30)
        pygame.display.update()

def fbS7():
    Txt1 = pygame.image.load("Images/textboxes/txt39.png")
    p1 = pygame.image.load("Images/characters/player_dark.png")
    m1 = pygame.image.load("Images/enemies/frog5.png")

    p = b.images(25,205,p1,10)
    m = b.images(580,160,m1,7.5)
    first = True
    count = 0

    while True:
        check()
        surf.fill((0,0,0))
        surf.blit(Txt1,(150,580))
        p.draw(surf)
        m.draw(surf)
        
        keys = pygame.key.get_pressed()
        
        if keys[K_RETURN] and count > 15:
            fbS8()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        first = False
        mainClock.tick(30)
        pygame.display.update()

def fbS8():
    Txt1 = pygame.image.load("Images/textboxes/txt40.png")
    p1 = pygame.image.load("Images/characters/player_dark.png")
    m1 = pygame.image.load("Images/enemies/frog5.png")

    p = b.images(25,205,p1,10)
    m = b.images(580,160,m1,7.5)
    first = True
    count = 0

    while True:
        check()
        surf.fill((0,0,0))
        surf.blit(Txt1,(150,580))
        p.draw(surf)
        m.draw(surf)
        
        keys = pygame.key.get_pressed()
        
        if keys[K_RETURN] and count > 15:
            fbS9()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        first = False
        mainClock.tick(30)
        pygame.display.update()

def fbS9():
    Txt1 = pygame.image.load("Images/textboxes/txt41.png")
    p1 = pygame.image.load("Images/characters/player_dark.png")
    m1 = pygame.image.load("Images/enemies/frog5.png")

    p = b.images(25,205,p1,10)
    m = b.images(580,160,m1,7.5)
    first = True
    count = 0

    while True:
        check()
        surf.fill((0,0,0))
        surf.blit(Txt1,(150,580))
        p.draw(surf)
        m.draw(surf)
        
        keys = pygame.key.get_pressed()
        
        if keys[K_RETURN] and count > 15:
            fbS10()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        first = False
        mainClock.tick(30)
        pygame.display.update()

def fbS10():
    Txt1 = pygame.image.load("Images/textboxes/txt42.png")
    p1 = pygame.image.load("Images/characters/player.png")
    m1 = pygame.image.load("Images/enemies/frog5.png")

    p = b.images(25,205,p1,10)
    m = b.images(580,160,m1,7.5)
    first = True
    count = 0

    while True:
        check()
        surf.fill((0,0,0))
        surf.blit(Txt1,(150,580))
        p.draw(surf)
        m.draw(surf)
        
        keys = pygame.key.get_pressed()
        
        if keys[K_RETURN] and count > 15:
            fbS11()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        first = False
        mainClock.tick(30)
        pygame.display.update()

def fbS11():
    Txt1 = pygame.image.load("Images/textboxes/txt43.png")
    p1 = pygame.image.load("Images/characters/player.png")
    m1 = pygame.image.load("Images/enemies/frog5.png")

    p = b.images(25,205,p1,10)
    m = b.images(580,160,m1,7.5)
    first = True
    count = 0

    while True:
        check()
        surf.fill((0,0,0))
        surf.blit(Txt1,(150,580))
        p.draw(surf)
        m.draw(surf)
        
        keys = pygame.key.get_pressed()
        
        if keys[K_RETURN] and count > 15:
            fbS12()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        first = False
        mainClock.tick(30)
        pygame.display.update()

def fbS12():
    Txt1 = pygame.image.load("Images/textboxes/txt44.png")
    p1 = pygame.image.load("Images/characters/player_dark.png")
    m1 = pygame.image.load("Images/enemies/frog5.png")

    p = b.images(25,205,p1,10)
    m = b.images(580,160,m1,7.5)
    first = True
    count = 0

    while True:
        check()
        surf.fill((0,0,0))
        surf.blit(Txt1,(150,580))
        p.draw(surf)
        m.draw(surf)
        
        keys = pygame.key.get_pressed()
        
        if keys[K_RETURN] and count > 15:
            fbS13()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        first = False
        mainClock.tick(30)
        pygame.display.update()

def fbS13():
    Txt1 = pygame.image.load("Images/textboxes/txt45.png")
    p1 = pygame.image.load("Images/characters/player_dark.png")
    m1 = pygame.image.load("Images/enemies/frog5.png")

    p = b.images(25,205,p1,10)
    m = b.images(580,160,m1,7.5)
    first = True
    count = 0

    while True:
        check()
        surf.fill((0,0,0))
        surf.blit(Txt1,(150,580))
        p.draw(surf)
        m.draw(surf)
        
        keys = pygame.key.get_pressed()
        
        if keys[K_RETURN] and count > 15:
            fbS14()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        first = False
        mainClock.tick(30)
        pygame.display.update()

def fbS14():
    Txt1 = pygame.image.load("Images/textboxes/txt46.png")
    p1 = pygame.image.load("Images/characters/player.png")
    m1 = pygame.image.load("Images/enemies/frog5.png")

    p = b.images(25,205,p1,10)
    m = b.images(580,160,m1,7.5)
    first = True
    count = 0

    while True:
        check()
        surf.fill((0,0,0))
        surf.blit(Txt1,(150,580))
        p.draw(surf)
        m.draw(surf)
        
        keys = pygame.key.get_pressed()
        
        if keys[K_RETURN] and count > 15:
            fbS15()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        first = False
        mainClock.tick(30)
        pygame.display.update()

def fbS15():
    global frog_death,Victory
    Txt1 = pygame.image.load("Images/textboxes/txt47.png")
    p1 = pygame.image.load("Images/characters/player_dark.png")
    m1 = pygame.image.load("Images/enemies/frog5.png")

    p = b.images(25,205,p1,10)
    m = b.images(580,160,m1,7.5)
    first = True
    count = 0

    while True:
        check()
        surf.fill((0,0,0))
        surf.blit(Txt1,(150,580))
        p.draw(surf)
        m.draw(surf)
        
        keys = pygame.key.get_pressed()
        
        if keys[K_RETURN] and count > 15:
            pygame.mixer.music.unload()
            frog_death = False
            Victory = True
            victory()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        count += 1
        first = False
        mainClock.tick(30)
        pygame.display.update()

def victory():
    bg1 = pygame.image.load("Images/backgrounds/victory.png")
    bg = b.images(0,0,bg1,1)
    
    while True:
        check()
        bg.draw(surf)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    main_menu()

        first = False
        mainClock.tick(30)
        pygame.display.update()


def death1():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)

    text = font.render("You have perished >:(",1,red)
    text1 = font.render("You done a stupid and didn't check for traps",1,red)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text1,(175,620))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    main_menu()

        first = False
        mainClock.tick(30)
        pygame.display.update()

def death2():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)

    text = font.render("You have perished >:(",1,red)
    text1 = font.render("You done a stupid and didn't check for traps",1,red)
    text2 = font.render("You have a giant spike through your body",1,red)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text1,(175,620))
        surf.blit(text2,(175,650))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    main_menu()

        first = False
        mainClock.tick(30)
        pygame.display.update()

def death3():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)

    text = font.render("You have perished >:(",1,red)
    text1 = font.render("You done a stupid and didn't check for traps",1,red)
    text2 = font.render("You set yourself on fire",1,red)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text1,(175,620))
        surf.blit(text2,(175,650))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    main_menu()

        first = False
        mainClock.tick(30)
        pygame.display.update()


def i1():
    bg1 = pygame.image.load("Images/backgrounds/1.jpg")#not made by me
    txtb1 = pygame.image.load("Images/textboxes/blank.png")
    font = pygame.font.SysFont("comicsans",30,True)
    base_font = pygame.font.Font(None,45)

    text = font.render("You done a stupid and tried to pick up a trap",1,red)
    text1 = font.render("You have a spike through your hand",1,red)
    text2 = font.render("You have 20% less health, 25% reduced damage",1,red)

    bg = b.images(80,0,bg1,0.55)
    txtb = b.images(150,580,txtb1,1)

    first = True
    
    while True:
        bg.draw(surf)
        txtb.draw(surf)
        surf.blit(text,(175,590))
        surf.blit(text1,(175,620))
        surf.blit(text2,(175,650))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    gp9b()

        first = False
        mainClock.tick(30)
        pygame.display.update()


def coming_soon():
    bg1 = pygame.image.load("Images/backgrounds/coming_soon.png")

    bg = b.images(0,0,bg1,1)
    
    while True:
        bg.draw(surf)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    main_menu()

        first = False
        mainClock.tick(30)
        pygame.display.update()


def mapp(a):
    bg1 = pygame.image.load("Images/other/map.jpg")
    bg = b.images(190,93,bg1,0.4)
    first = True

    while True:
        if first == True:
            surf.fill((0,0,0))
            
        bg.draw(surf)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if K_RETURN:
                    pygame.mouse.set_visible(False)
                    surf.fill((0,0,0))
                    a()#calls the previous function but its stored as a variable

        first = False
        mainClock.tick(30)
        pygame.display.update()


def running_options_menu(a):
    global music,sound_effect,mini_me
    pygame.mouse.set_visible(True)
    first = True

    #loading images
    bg = pygame.image.load('Images/backgrounds/OptionsBG.png').convert()
    bg2 = pygame.image.load("Images/backgrounds/Options2BG.png").convert()
    img1 = pygame.image.load("Images/normal/Music_toggle.png").convert()
    img2 = pygame.image.load("Images/normal/Sound_effect_toggle.png").convert()
    img3 = pygame.image.load("Images/normal/Mini_me_toggle.png").convert()
    img4 = pygame.image.load("Images/normal/Options_back.png").convert()
    img5 = pygame.image.load("Images/other/on.png").convert()
    img6 = pygame.image.load("Images/other/off.png").convert()

    #making images buttons
    music_toggle = b.buttons(200,215,img1,1)
    sound_effect_toggle = b.buttons(200,365,img2,1)
    mini_me_toggle = b.buttons(200,515,img3,1)
    back = b.buttons(60,675,img4,1)
    while True:
        check()
        #putting the images on screen
        surf.blit(bg,(0,0))
        surf.blit(bg2,(150,150))

        #code that makes the images next to the toggle red or green
        if music == True:
            surf.blit(img5,(850,215))
        elif music == False:
            surf.blit(img6,(850,215))
        if sound_effect == True:
            surf.blit(img5,(850,365))
        elif sound_effect == False:
            surf.blit(img6,(850,365))
        if mini_me == True:
            surf.blit(img5,(850,515))
        elif mini_me == False:
            surf.blit(img6,(850,515))

        #logic behind the toggles and settings
        if music_toggle.draw(surf) and first == False:
            if music == True:
                music = False
            elif music == False:
                music = True

        if sound_effect_toggle.draw(surf) and first == False:
            if sound_effect == True:
                sound_effect = False
            elif sound_effect == False:
                sound_effect = True

        if mini_me_toggle.draw(surf) and first == False:
            if mini_me == True:
                mini_me = False
            elif mini_me == False:
                mini_me = True

        if back.draw(surf) and first == False:
            surf.fill((0,0,0))
            pygame.mouse.set_visible(False)
            a()

        #makes it so the game quits when the "x" is pressed
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        #first makes sure that the buttons can only be pressed from the second frame of each function
        first = False
        mainClock.tick(30)#frame rate
        pygame.display.update()#updates the screen with any changes


    

settings()
main_menu()
#quit_menu()
#play_menu()
#options_menu()
#load_menu()
#new_file()
#scene1()
#scene23()
#scene24()
#scene26()
#scene27()
#scene28()
#scene33()
#gp0()
#gp1()
#gp2()
#gp3a1()
#gp3d()
#gp4C0()
#gp4C()#first combat
#gp6()
#gp6bC()#chest room combat
#gp6dC()#ice room combat
#gp5b()#this is trap 1 area
#gp5c()#left from trap 1 area
#gp5()
#gp7()#carry on from trap area
#gp7a()
#gp7a1()
#gp7a2()
#gp7a3()
#gp8()
#gp8a()
#gp8a1()
#gp9a()
#gp9b()
#gp9b1()
#gp9b2()
#gp10()
#gp10C()
#gp10b()
#gp11c()
#gp12b()
#gp13()#maze
#gp13a6()
#gp13a10()
#gp13a14()
#gp12b2()
#gp15()#funciton leading to BR
#gp17()#start of BR
#gp17C()
#fb1()#after unlocking door
#fbS1()
#fbS3()
#fbS4()
#fbS6()
#fbS7()
#death1()






#NEED TO MAKE IT SO OPTIONS ARE ACCESSABLE FROM ALL AREAS OF THE GAME, NOT JUST THE MAIN MENU
#CHANGE THE COLOUR OF THE USER TEXTBOXES TO BE A GREY RATHER THAN A BLUE









