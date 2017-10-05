# coding=utf-8
from lettuce import step, world
from edad import Edad

# -----------------------------------------------------------------------------
# ----------------------------------- Edad ------------------------------------
# -----------------------------------------------------------------------------
@step(u'Dado que ingreso mi edad')
def dado_que_ingreso_mi_edad(step):
    world.eval_edad = Edad()


@step(u'cuando escribo un "([^"]*)"')
def cuando_escribo_un_num1(step, num1):
    world.eval_edad.evaluar_edad(num1)


@step(u'entonces el evaluador de edad me dice "([^"]*)"')
def entonces_el_evaluador_de_edad_me_dice_evaluacion(step, esperado):
    obtenido = world.eval_edad.get_evaluacion_edad()
    assert esperado == obtenido, \
        'El resultado esperado es: ' + esperado + \
        " y el obtenido es: " + obtenido
