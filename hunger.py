import threading

class Hunger:
    def __init__(self,hunger):
        self.hunger=hunger
        self.decay_hunger()

    def decay_hunger(self):
        threading.Timer(1.0,self.decay_hunger).start()
        if self.hunger>10 :
            self.hunger*=0.96

    def add_hunger(self, increment):
        self.hunger+=increment

    def throw_hunger_message(self):
        if (self.hunger > 100):
            return "I'm starving (＠◇＠)"
        elif (self.hunger > 80):
            return "I'm hungry | •́ ◇ •̀ |"
        elif (self.hunger > 60):
            return "You may feed me if you want to! ⸜₍๑•⌔•๑ ₎⸝"
        elif (self.hunger > 40):
            return "I am okay, thank you! ꜀( ˊ̠˂˃ˋ̠ )꜆"
        elif (self.hunger > 20):
            return "I am so full ＜(´ ՞)ਊ( ՞ )＞"
        else:  
            return "I can starve for the rest of my life ＜(´ ՞)ਊ( ՞ )＞"