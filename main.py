class Mensch:
    def __init__(self, name:str, height:int, age:int, weight:float, eyecolor:str, isMale:bool):
        '''
        :param name: Name des Menschen
        :param height: Größe des Menschen in cm
        :param age: Alter des Menschen in gazen Jahren
        :param weight: Gewicht des Menschen in Kg
        :param eyecolor: Farbe der Augen
        :param isMale: ob der Mensch männlich ist
        '''
        self.name = name
        self.height = height
        self.age = age
        self.weight = weight
        self.eyecolor = eyecolor
        self.isMale = isMale

    def sayHello(self):
        return (
                'Hallo, mein Name ist ' + self.name +
                ' ich bin ' + str(self.age) +
                ' Jahre alt, und bin ' + str(self.height/100) +
                ' meter Groß.'
                )

Kolja = Mensch('Kolja', 179, 15, 59.08, 'Braun', True)
print(Kolja.sayHello())