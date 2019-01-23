


class dog:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs

    def catcher(self):
        print("Hahaha, I've caught " + self.name)

dog1 = dog("Scotty", 3)
dog1.catcher()

