# coding=utf-8

class Edad():

    def __init__(self):
        self.evaluacion_edad = ""

    def evaluar_edad(self, num1):
        edad = int(num1)
        if edad < 0:
            self.evaluacion_edad = u'No existes'
        elif edad == 0:
            self.evaluacion_edad = u'Eres un bebe'
        elif edad <= 13:
            self.evaluacion_edad = u'Eres un nino'
        elif edad <= 18:
            self.evaluacion_edad = u'Eres un adolescente'
        elif edad <= 65:
            self.evaluacion_edad = u'Eres un adulto'
        elif edad <= 120:
            self.evaluacion_edad = u'Eres un adulto mayor'
        else:
            self.evaluacion_edad = u'Eres Mumm-Ra'

    def get_evaluacion_edad(self):
        return self.evaluacion_edad
