# coding=utf-8

class Edad():

    def __init__(self):
        self.evaluacion_edad = ""

    def evaluar_edad(self, num1):
        num1 = int(num1)
        if num1 < 0:
            self.evaluacion_edad = u'No existes'
        elif num1 == 0:
            self.evaluacion_edad = u'Eres un bebe'
        elif num1 <= 13:
            self.evaluacion_edad = u'Eres un nino'
        elif num1 <= 18:
            self.evaluacion_edad = u'Eres un adolescente'
        elif num1 <= 65:
            self.evaluacion_edad = u'Eres un adulto'
        elif num1 <= 120:
            self.evaluacion_edad = u'Eres un adulto mayor'
        else:
            self.evaluacion_edad = u'Eres Mumm-Ra'

    def get_evaluacion_edad(self):
        return self.evaluacion_edad
