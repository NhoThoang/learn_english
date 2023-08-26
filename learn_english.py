import pygame
import os
import pyttsx4
import threading

def EN_voice(text):
    engine = pyttsx4.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id) # change index to change voice
    engine.setProperty('rate', 120) # change value to change speed
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
    for filename in os.listdir(imagebutton):
        if filename.endswith('.png'):
            current_image = int(filename[:-4]) - 1
            images[str(current_image + 1)] = images[str(current_image + 1)].convert_alpha()
            screen.blit(images[str(current_image + 1)], (current_image * 100, 150))
def txt_list():
    with open('./text/animal.txt','r') as file:
        i = "".join(str(j)for j in file).replace('\n', ',')
    return i.split(',')

def loop_event():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(os.listdir('./button_images/animal/'))):
                    if event.button == 1 and i <= event.pos[0] // 100 < i+1 and \
                    150 <= event.pos[1] <= pygame.image.load(f'./button_images/animal/{i+1}.png').get_height()+150:
                        # show_text(txt_list()[i])
                        # EN_voice(txt_list()[i])                  
                        threading.Thread(target=show_text(txt_list()[i])).start()
                        threading.Thread(target=EN_voice(txt_list()[i])).start()
                                          
        pygame.display.update()
  
if __name__=="__main__":
    pygame.init()
    screen = pygame.display.set_mode((1000, 700))
    button("./background/theam1.jpg","./button_images/animal/")
    loop_event()
    
    