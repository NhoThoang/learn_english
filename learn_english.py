import pygame
import os
import pyttsx4
import threading
lock = threading.Lock()
def EN_voice(text):
    with lock:
        engine = pyttsx4.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id) # change index to change voice
        engine.setProperty('rate', 120)
        engine.say(text)
        engine.runAndWait()
    
def white_screen():
    whitescreen  = pygame.Rect(200,0 ,600, 100)
    pygame.draw.rect(screen, (255, 255, 255), whitescreen)
    return whitescreen

def background(file):
    background_image = pygame.image.load(file)
    screen.blit(background_image, (0, 0))
    return(screen)

def show_text(text):
    with lock:
        screen1 = white_screen()
        font = pygame.font.SysFont('Comic Sans MS', 50)
        text_surface = font.render(text, True, (255,0,0))
        text_width, text_height = text_surface.get_size()
        white_screen_x = screen1.x + screen1.width / 2
        white_screen_y = screen1.y + screen1.height / 2
        screen.blit(text_surface, (white_screen_x - text_width / 2, white_screen_y - text_height / 2))

def load_images(path_to_directory):
    image_dict = {}
    for filename in os.listdir(path_to_directory):
        if filename.endswith('.png')or filename.endswith('.jpg'):
            path = os.path.join(path_to_directory, filename)
            key = filename[:-4]
            image_dict[key] = pygame.image.load(path).convert_alpha()
    return image_dict

def button(background1, imagebutton):
    background(background1)
    white_screen()
    images = load_images(imagebutton)
    for filename in range(10):
        current_image = int(filename)
        images[str(current_image + 1)] = images[str(current_image + 1)].convert_alpha()
        screen.blit(images[str(current_image + 1)], (current_image * 100, 150))
    for i,filename in enumerate(range(10,20)):
        current_image = int(filename)
        images[str(current_image + 1)] = images[str(current_image + 1)].convert_alpha()
        screen.blit(images[str(current_image + 1)], (i* 100, 250))

def txt_list():
    with open('./text/animal.txt','r') as file:
        i = "".join(str(j)for j in file).replace('\n', ',')
    return i.split(',')

def loop_event(file):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(10):
                    if event.button == 1 and i <= event.pos[0] // 100 < i+1 and \
                    150 <= event.pos[1] <= pygame.image.load(f'{file}{i+1}.png').get_height()+150: 
                        threading.Thread(target=show_text, args=(txt_list()[i],)).start()
                        threading.Thread(target=EN_voice, args=(txt_list()[i],)).start()
                for i,j in enumerate(range(10,20)):
                    if event.button == 1 and i <= event.pos[0] // 100 < i+1 and \
                    250 <= event.pos[1] <= pygame.image.load(f'{file}{j+1}.png').get_height()+250:
                        threading.Thread(target=show_text, args=(txt_list()[j],)).start()
                        threading.Thread(target=EN_voice, args=(txt_list()[j],)).start()                                      
        pygame.display.update()
if __name__=="__main__":
    pygame.init()
    screen = pygame.display.set_mode((1000, 700))
    button("./background/theam1.jpg","./button_images/animal/")
    loop_event('./button_images/animal/')
    
    