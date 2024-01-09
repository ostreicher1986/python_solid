"""
Classe que não está respeitando o princípio da responsabilidade única
"""

class PersonModel:

    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

    def save(self, person: PersonModel):
        pass

""" -------------------------------------------------------------------------------------------------- """

"""
Classe que está respeitando o princípio da responsabilidade única - Classe modelo
"""

class PersonModel:

    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

""" -------------------------------------------------------------------------------------------------- """

"""
Classe que está respeitando o princípio da responsabilidade única - Classe de persistência
"""

class PersonRepository:

    def get_person(self, id) -> PersonModel:
        pass

    def save(self, person: PersonModel):
        pass