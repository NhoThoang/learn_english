import pygame
import threading
lock = threading.Lock()
class show_text1:
    def __init__(self,pathfile1,screen2,i) -> None:
        self.screen =screen2
        self.pathfile1=pathfile1
        self.i=i
    def txt_list(self):
        with open(self.pathfile1) as file:
            i = "".join(str(j)for j in file).replace('\n', ',')
        return i.split(',')
    def txt_dict(self):
        with open(self.pathfile1) as file:
            s = "".join(str(j)for j in file).replace('\n', ',')
            d = dict(enumerate(s.split(",")))
            return d
    def show_text1(self):
        # with lock:
        d= self.txt_dict()
        font = pygame.font.SysFont('Comic Sans MS', 50)
        text_surface = font.render(d[self.i], True, (255,0,0))
        self.screen.blit(text_surface, (470,50))


# pygame.init()
# screen = pygame.display.set_mode((1000, 700))

# show_text1('./text/animal.txt',screen,2).show_text1()

# while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 exit()
#         pygame.display.update()
        # self.screen.blit(text_surface, (470,50))
    
# with open('./text/animal.txt') as file:
#     i = "".join(str(j)for j in file).replace('\n', ',')
#     print (i.split(','))
# d={}
# with open('./text/animal.txt') as file:
#     s = file.read()
#     d = dict(enumerate(s.split(",")))
# print(d)


# with open('./text/animal.txt') as file:
#     s = "".join(str(j)for j in file).replace('\n', ',')
#     d = dict(enumerate(s.split(",")))
    
# print(d)


    #     (key,val)= line.split()
    #     d[int(key)]=val
    # print(d)