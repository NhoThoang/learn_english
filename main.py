from source.main import toppic
from source.main2 import toppic2
class select:
    def __init__(self) -> None:
        pass

    def selec():
        a= int(input('enter a = '))
        if a==1:
            topic=toppic("./background/theam1.jpg","./background/white.png","./button_images/animal/","./text/animal.txt")
            topic.topic()
        if a==2:
            topic=toppic("./background/theam2.jpg","./background/white.png","../button_images/number/","./text/number.txt")
            topic.topic()
if __name__=="__main__":
    # select.selec()
    topic=toppic2("./background/theam1.jpg","./background/white.png","./button_images/toppic/")
    topic.topic()
   