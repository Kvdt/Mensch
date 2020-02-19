import json

class new_mensch:
    def __init__(self, name: str, height: int, age: int, weight: float, eyecolor: str, is_male: bool):
        '''
        :param name: Name des Menschen
        :param height: Größe des Menschen in cm
        :param age: Alter des Menschen in gazen Jahren
        :param weight: Gewicht des Menschen in Kg
        :param eyecolor: Farbe der Augen
        :param isMale: ob der Mensch männlich ist
        '''
        self.verify = 'W9Dg9b#ZrqBa@Uzb'
        self.name = name
        self.height = height
        self.age = age
        self.weight = weight
        self.eyecolor = eyecolor
        self.is_male = is_male

    def export_json(self):
        with open(self.name + '.json', 'w') as file:
            json.dump(self.__dict__, file)

    def say_hello(self):
        msg = 'Hallo, mein Name ist {} ich bin {} Jahre alt, und bin {} meter Groß.'
        return msg.format(self.name, self.age, self.height/100)


class load_mensch:
    def __init__(self, path: str):
        '''
        :param path: The path to the existing json
        '''
        self.path = path
        with open(self.path) as file:
            self.data = json.load(file)
        try:
            if self.data['verify'] == 'W9Dg9b#ZrqBa@Uzb':
                self.name = self.data['name']
                self.height = self.data['height']
                self.age = self.data['age']
                self.weight = self.data['weight']
                self.eyecolor = self.data['eyecolor']
                self.is_male = self.data['is_male']

        except KeyError: print("Bitte geben sie eine JSON im korrekten Format an")


Kolja = new_mensch('Kolja', 181, 15, 59, 'brown', True)
print(Kolja.say_hello())

