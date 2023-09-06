from source.main import toppic
class select:
    def __init__(self,k) -> None:
        self.k = k

    def selec(self): 
        if self.k==1:
            topic=toppic("./background/theam1.jpg","./background/white.png","./button_images/animal/","./text/animal.txt")
            topic.topic()
        if self.k==2:
            topic=toppic("./background/theam2.jpg","./background/white.png","./button_images/number/","./text/number.txt")
            topic.topic()
