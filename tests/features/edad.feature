Feature: Evaluación de edad
	Como usuario del evaluador de edad
	deseo ingresar mi edad en número
	para obtener mi evaluación de edad

	Scenario: Cuando tengo -5 años
		Dado que ingreso mi edad
		cuando escribo un "-5"
		entonces el evaluador de edad me dice "No existes"

    Scenario: Cuando tengo 0 años
		Dado que ingreso mi edad
		cuando escribo un "0"
		entonces el evaluador de edad me dice "Eres un bebe"

    Scenario: Cuando tengo 10 años
		Dado que ingreso mi edad
		cuando escribo un "10"
		entonces el evaluador de edad me dice "Eres un nino"

    Scenario: Cuando tengo 16 años
		Dado que ingreso mi edad
		cuando escribo un "16"
		entonces el evaluador de edad me dice "Eres un adolescente"

    Scenario: Cuando tengo 50 años
		Dado que ingreso mi edad
		cuando escribo un "50"
		entonces el evaluador de edad me dice "Eres un adulto"

    Scenario: Cuando tengo 98 años
		Dado que ingreso mi edad
		cuando escribo un "98"
		entonces el evaluador de edad me dice "Eres un adulto mayor"

    Scenario: Cuando tengo 2000 años
		Dado que ingreso mi edad
		cuando escribo un "2000"
		entonces el evaluador de edad me dice "Eres Mumm-Ra"
