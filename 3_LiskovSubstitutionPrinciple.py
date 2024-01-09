"""
Classe que não está respeitando o princípio da substituição de liskov.

Princípio da Substituição de Liskov

Uma subclasse deve ser substituível por sua superclasse. O objetivo disto
princípio é verificar se uma subclasse pode assumir o lugar de sua
superclasse sem gerar erros. 

Vamos usar nosso exemplo de pessoa.

"""

def person_my_size(persons: list):
    for person in persons:
        if isinstance(person, DevModel):
            print(dev_my_size(person))
        elif isinstance(person, NurseModel):
            print(nurse_my_size(person))
        elif isinstance(person, SonModel):
            print(son_my_size(person))

person_my_size(persons)

""" -------------------------------------------------------------------------------------------------- """

"""
Vamos corrigir isso de acordo com o princípio.

A função person_my_size se importa menos com o tipo de Pessoa passado, apenas
chama o método my_size. Tudo o que sabe é que o parâmetro deve ser de um
Tipo de pessoa, ou seja, a classe PersonModel ou sua subclasse.

A classe PersonModel agora precisa implementar/definir um método my_size. E os suas
subclasses precisam implementar o método my_size:

"""
def person_my_size(persons: list):
    for person in persons:       
        print(person.my_size(person))       

person_my_size(persons)

class PersonModel:
    def my_size(self):
        pass

class DevModel(PersonModel):
    def my_size(self):
        pass