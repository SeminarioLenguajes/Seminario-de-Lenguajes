#!/usr/bin/env python
import pygame
import Malvavisco
import Chef
import Background
import threading
import time
from random import randint
import Fireball


class Nivel():

    def __init__(self, screenMenu, alto, ancho):
        self.threadFinalizado = False
        self.spritesPrincipales = pygame.sprite.Group()
        self.spriteBackground = pygame.sprite.Group()
<<<<<<< HEAD
        self.spritesDulces = pygame.sprite.Group()
        self.spritesFireball = pygame.sprite.Group()
=======
>>>>>>> edb0dcc10936c654e9d5d3a52a9e7ad84fecf0f3
        self.clock = pygame.time.Clock()
        self.screen = screenMenu
        self.alto = alto
        self.ancho = ancho
        self.fps = 60
        self.colores = { "RED" : (255,0,0), "BLACK" : (0,0,0) }
        self.iteradorParaTexto = 0
        self.textoPantallaDeCarga = "Cargando"
<<<<<<< HEAD
        self.cont = 0
        self.sonidoColisionFireball = pygame.mixer.Sound("Sonidos/colisionFireball.ogg")
=======
>>>>>>> edb0dcc10936c654e9d5d3a52a9e7ad84fecf0f3

    def iniciar(self):

        self.pantallaDeCarga()
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Marshmellow Survivor")
        ejecutandoNivel = True
<<<<<<< HEAD
        pygame.mixer.music.load("Sonidos/Alone.mp3")
        pygame.mixer.music.play(-1)
        listaDulces = []
        while ejecutandoNivel:


            numeroRandom = randint(1, 20)
            if numeroRandom > 19:
                nuevoDulce = Dulce.Dulce()
                self.spritesDulces.add(nuevoDulce)
                listaDulces.append(nuevoDulce)

            self.cont += 1
            if self.cont == 120:
                self.cont = 0
                fireball = Fireball.Fireball(500, 0, 200, 200,self.malvavisco.rect.x,self.malvavisco.rect.y)
                self.spritesFireball.add(fireball)


            #numeroRandom = randint(1, 20)
            #if numeroRandom > 19:
             #   nuevoDulce = Dulce.Dulce()
              #  self.spritesDulces.add(nuevoDulce)
               # listaDulces.append(nuevoDulce)


=======

        while ejecutandoNivel:

>>>>>>> edb0dcc10936c654e9d5d3a52a9e7ad84fecf0f3
            self.clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        ejecutandoNivel = False

            #hits = pygame.sprite.spritecollide(malvavisco, spritesDulces,False,pygame.sprite.collide_circle)
            #if hits:
                #print "Buen dia"
<<<<<<< HEAD
            colisionFireball = pygame.sprite.spritecollide(self.malvavisco,self.spritesFireball,True)
            if colisionFireball:
                self.sonidoColisionFireball.play()

=======
>>>>>>> edb0dcc10936c654e9d5d3a52a9e7ad84fecf0f3

            self.spriteBackground.draw(self.screen)
            self.spritesPrincipales.draw(self.screen)
            self.spritesFireball.draw(self.screen)
            self.spritesPrincipales.update()
<<<<<<< HEAD
            self.spritesDulces.update()
            self.spritesFireball.update()
            pygame.display.flip()



=======
            pygame.display.flip()

>>>>>>> edb0dcc10936c654e9d5d3a52a9e7ad84fecf0f3
    def cargaDeDatos(self):
        self.malvavisco = Malvavisco.Malvavisco(375,550,150,150)

        self.spritesPrincipales.add(self.malvavisco)
        self.chef = Chef.Chef(500,0,250,250)
        self.spritesPrincipales.add(self.chef)
<<<<<<< HEAD

        self.background = Background.Background(0,0,1360,760)

        self.spritesPrincipales.add(self.malvavisco)
        self.spritesPrincipales.add(self.chef)





        self.spriteBackground.add(self.background)

        self.threadFinalizado = True

    def drawText(self, surf, text, size, x, y):




=======
        self.background = Background.Background(0,0,1360,760)
        self.spriteBackground.add(self.background)
        self.threadFinalizado = True

    def drawText(self, surf, text, size, x, y):
>>>>>>> edb0dcc10936c654e9d5d3a52a9e7ad84fecf0f3
            font_name = pygame.font.match_font('arial')
            font = pygame.font.Font(font_name,size)
            text_surface = font.render(text, True, self.colores["RED"])
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x,y)
            surf.blit(text_surface,text_rect)

    def pantallaDeCarga(self):
        self.clock.tick(60)
        threadDeCarga = threading.Thread(target=self.cargaDeDatos)
        threadDeCarga.start()

        while not self.threadFinalizado:
            self.screen.fill(self.colores["BLACK"])
            self.actualizarCargando()
            self.drawText(self.screen , self.textoPantallaDeCarga, 18, self.alto/2, self.ancho/2)
            pygame.display.flip()
            time.sleep(1.5)

    def actualizarCargando(self):
        self.textoPantallaDeCarga = self.textoPantallaDeCarga + "."

        if (self.iteradorParaTexto > 2):
            self.textoPantallaDeCarga = "Cargando"
            self.iteradorParaTexto = 0
<<<<<<< HEAD

        self.iteradorParaTexto += 1
=======
>>>>>>> edb0dcc10936c654e9d5d3a52a9e7ad84fecf0f3

        self.iteradorParaTexto += 1
