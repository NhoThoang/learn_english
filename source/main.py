import pygame
import sys
import os
import threading
from .backgrd import Background
from .show_text import show_text1
from .textspeed import textspeed

class toppic:
    def __init__(self,theam, white, button, text) -> None:
        self.theam=theam
        self.white=white
        self.button=button
        self.text=text
    def topic(self):
        pygame.init()
        screen = pygame.display.set_mode((1000, 700))
        bgr = Background(self.theam,self.white,self.button,screen)
        # bgr()
        # bgr = Background("../background/theam1.jpg","../background/white.png","../button_images/animal/",screen)
        bgr.background()
        bgr.white_screen()
        bgr.button()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    num_images = len([f for f in os.listdir(self.button) if f.endswith('.png')])
                    for i in range(num_images):     
                        # voice = textspeed(text)
                        if 200 + (i // 6) * 100 <= event.pos[1] <= 200 + (i // 6 + 1) * 100 and \
                                i % 6 * 150+100 <= event.pos[0] < (i % 6 + 1) * 150+100:
                            voice = textspeed(self.text,i)
                            text =show_text1(self.text,screen,i)
                            threading.Thread(target=bgr.white_screen(),args=text.show_text1()).start()
                            threading.Thread(target=voice.EN_voice).start()
            pygame.display.update() 
    # @classmethod
    # def topic2(self):
    #     pygame.init()
    #     screen = pygame.display.set_mode((1000, 700))
    #     bgr = Background(self.theam,self.white,self.button,screen)
    #     # bgr = Background("../background/theam1.jpg","../background/white.png","../button_images/animal/",screen)
    #     bgr.background()
    #     bgr.button()
    #     while True:
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 pygame.quit()
    #                 sys.exit()
    #             elif event.type == pygame.MOUSEBUTTONDOWN:
    #                 num_images = len([f for f in os.listdir(self.button) if f.endswith('.png')])
    #                 for i in range(num_images):     
    #                     # voice = textspeed(text)
    #                     if 200 + (i // 6) * 100 <= event.pos[1] <= 200 + (i // 6 + 1) * 100 and \
    #                             i % 6 * 150+100 <= event.pos[0] < (i % 6 + 1) * 150+100:
    #                         print('ok')
    #                         # voice = textspeed(self.text,i)
    #                         # text =show_text1(self.text,screen,i)
    #                         # threading.Thread(target=bgr.white_screen(),args=text.show_text1()).start()
    #                         # threading.Thread(target=voice.EN_voice).start()
    #         pygame.display.update() 


# if __name__=="__main__":
#     a= int(input('enter a = '))
#     if a==1:
#         topic=toppic("../background/theam1.jpg","../background/white.png","../button_images/animal/","../text/animal.txt")
#         topic.topic()
#     if a==2:
#         topic=toppic("../background/theam1.jpg","../background/white.png","../button_images/number/","../text/number.txt")
#         topic.topic()

   