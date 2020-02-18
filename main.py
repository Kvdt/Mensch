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
        return (
                'Hallo, mein Name ist ' + self.name +
                ' ich bin ' + str(self.age) +
                ' Jahre alt, und bin ' + str(self.height/100) +
                ' meter Groß.'
                )

class load_mensch:
    def __init__(self, path: str):
        '''
        :param path: The path to the existing json
        '''
        self.path = path
        with open(self.path + '.json') as file:
            self.data = json.load(file)
