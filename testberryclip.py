#!/usr/bin/python
#--------------------------------------
#    ___                   ________
#   / _ )___ __________ __/ ___/ (_)__
#  / _  / -_) __/ __/ // / /__/ / / _ \
# /____/\__/_/ /_/  \_, /\___/_/_/ .__/
#                  /___/        /_/
#
#       BerryClip - 6 LED Board
#
# Graphical testing program
#
# This pygame based program can
# interactively test the berryclip.
#
# Author : Graham Taylor
# Date   : 06/12/2012
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------
import RPi.GPIO as GPIO
import os, pygame
from pygame.locals import *

OUTPUTS = { 'led1':4,'led2':17,'led3':22,'led4':10,'led5':9,'led6':11,'buzzer':8 }
BUTTON_PIN = 7
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()
for pin in OUTPUTS.values():
    GPIO.setup(pin, GPIO.OUT)

GPIO.setup(BUTTON_PIN, GPIO.IN)

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    image = image.convert()
    if colorkey is -1:
        colorkey = image.get_at((0,0))
    return image, image.get_rect()

TRANSPARENT = (255,0,255)
BUTTON_SIZE = 50

class Button():
    def __init__(self, topleft):
        self.surf = pygame.Surface((BUTTON_SIZE,BUTTON_SIZE))
        self.surf.fill(TRANSPARENT)
        self.surf.set_colorkey(TRANSPARENT)
        self.surf.set_alpha(100)
        self.rect = pygame.Rect(topleft[0],topleft[1],BUTTON_SIZE,BUTTON_SIZE)
        self.toggle(0)

    def toggle(self,state):
        if state:
            self.surf.fill(TRANSPARENT)
            pygame.draw.rect(self.surf, (50,200,20),
                             (0,0,BUTTON_SIZE,BUTTON_SIZE), 0)
        else:
            self.surf.fill(TRANSPARENT)
            pygame.draw.rect(self.surf, (0,230,230),
                             (0,0,BUTTON_SIZE,BUTTON_SIZE), 4)

class BoardInput():
    """A class to place the rectangle for clicking by the mouse and send
    relevant signal to the berryclip. It will also store the status of the led
    and visually indicate when lit"""
    def __init__(self,center,name,rad):
        self.state = 1  # gets toggled in a mo
        self.name = name
        self.rad = rad
        self.surf = pygame.Surface((self.rad*2,self.rad*2))
        self.surf.fill(TRANSPARENT)
        self.surf.set_colorkey(TRANSPARENT)
        self.surf.set_alpha(100)
        self.rect = pygame.Rect(center[0]-self.rad,center[1]-self.rad,self.rad*2,self.rad*2)
        self.toggle()
        
    def toggle(self):
        screen = pygame.display.get_surface()
        if self.state:
            self.state = 0
            self.surf.fill(TRANSPARENT)
            pygame.draw.circle(self.surf, (50,200,20), (self.rad,self.rad),
                               self.rad, 4)
        else:
            self.state =1
            self.surf.fill(TRANSPARENT)
            pygame.draw.circle(self.surf, (230,230,0), (self.rad,self.rad),
                               self.rad, 0)
        GPIO.output(OUTPUTS[self.name],self.state)

def main():
    pygame.init()
    screen = pygame.display.set_mode((500,375))

    bkgImage, bkgImageRect = load_image('berryClip.JPG', -1 )
    size = (width, height) = bkgImage.get_size()

    pygame.display.set_caption('BerryClip testing')

    if pygame.font:
        font = pygame.font.Font(None, 36)
        text = font.render("Click each part of the board to test it out...", 1,
                           (10,10,10))
        textpos = text.get_rect(centerx=width/2)
        bkgImage.blit(text, textpos)

        font = pygame.font.Font(None, 20)
        text = font.render("press <ESC> to exit.", 1,
                           (10,10,10))
        textpos = text.get_rect(bottomright=(width-10,height-10))
        bkgImage.blit(text, textpos)

    screen.blit(bkgImage, bkgImageRect)

    widgets = []
    #Create the led objects
    led_locations = ((271,78),(282,101),(291,130),(308,162),(319,189),(334,219))
    i = 1
    for center in led_locations:
        widgets.append( BoardInput(center, 'led' + `i`, 11 ))
        i = i + 1

    #Create the buzzer object
    widgets.append( BoardInput( (160,132), 'buzzer', 28) )

    #show the objects
    for widget in widgets:
        screen.blit(widget.surf,widget.rect)

    #Create button object
    button = Button((170,240))
    button_state = 0
    screen.blit(button.surf,button.rect)

    pygame.display.flip()

    clock = pygame.time.Clock()
    while 1:
        clock.tick(60)  #max framerate of loop is 60/sec
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return
                elif event.key > 48 and event.key < 55:
                    led = widgets[event.key-49]
                    led.toggle()
                    screen.blit(bkgImage, led.rect, led.rect)
                    screen.blit(led.surf,led.rect)
                    pygame.display.flip()
                elif event.key == K_b:
                    buzzer = widgets[6]
                    buzzer.toggle()
                    screen.blit(bkgImage, buzzer.rect, buzzer.rect)
                    screen.blit(buzzer.surf,buzzer.rect)
                    pygame.display.flip()
            elif event.type == MOUSEBUTTONDOWN:
                widgets_clicked = [widget for widget in widgets if widget.rect.collidepoint(pygame.mouse.get_pos())]
                for widget in widgets_clicked:
                    widget.toggle()
                    screen.blit(bkgImage, widget.rect, widget.rect)
                    screen.blit(widget.surf,widget.rect)
                pygame.display.flip()
        if GPIO.input(BUTTON_PIN) == 1:
            button_state = 1
            button.toggle(1)
            screen.blit(bkgImage, button.rect, button.rect)
            screen.blit(button.surf, button.rect)
            pygame.display.flip()
        elif button_state == 1:
            button_state = 0
            button.toggle(0)
            screen.blit(bkgImage, button.rect, button.rect)
            screen.blit(button.surf, button.rect)
            pygame.display.flip()

if __name__ == '__main__': 
    main()
    #turn off widgets
    for pin in OUTPUTS.values():
        GPIO.output(pin,False)

