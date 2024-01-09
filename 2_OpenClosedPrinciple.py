"""
Classe que não está respeitando o princípio do aberto/fechado
"""

class PersonModel:

    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

persons = [
    PersonModel('Pedro'),
    PersonModel('Letícia'),
    PersonModel('Tesla')
]

def person_sound(persons: list):
    for person in persons:

        if person.name == 'Pedro':
            print('Eu sou um desenvolvedor, quero codar...')

        if person.name == 'Letícia':
            print('Eu sou enfermeira, cadê o paciente...')

        elif person.name == 'Tesla':
            print('Papai, Mamãe, quero assistir o dinossauro...')

person_sound(persons)

""" -------------------------------------------------------------------------------------------------- """

"""
Classe que está respeitando o princípio do aberto/fechado
"""

class PersonModel:

    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

    def make_sound(self):
        pass

class DevModel(PersonModel):
    def make_sound(self):
        return 'Eu sou um desenvolvedor, quero codar...'
    
class NurseModel(PersonModel):
    def make_sound(self):
        return 'Eu sou enfermeira, cadê o paciente...'
    
class SonModel(PersonModel):
    def make_sound(self):
        return 'Papai, quero assistir o dinossauro.'
    
def person_sound(persons: list):
    for person in persons:
        print(person.make_sound())       

person_sound(persons)