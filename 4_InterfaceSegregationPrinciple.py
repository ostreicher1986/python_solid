"""
Princípio de segregação de interface

Crie interfaces refinadas que sejam específicas. Os clientes não devem ser
forçados a depender de interfaces que não usam. Este princípio trata
com as desvantagens de implementar grandes interfaces.

Vejamos a interface IPerson abaixo:

"""

class IPerson:
    def talk_about_dev(self):
        raise NotImplementedError
    
    def talk_about_nursing(self):
        raise NotImplementedError
    
    def talk_about_school(self):
        raise NotImplementedError

""" -------------------------------------------------------------------------------------------------- """

class DevModel(IPerson):
    def talk_about_dev(self):
        pass
    def talk_about_nursing(self):
        pass
    def talk_about_school(self):
        pass
    
class NurseModel(IPerson):
    def talk_about_dev(self):
        pass
    def talk_about_nursing(self):
        pass
    def talk_about_school(self):
        pass
    
class SonModel(IPerson):
    def talk_about_dev(self):
        pass
    def talk_about_nursing(self):
        pass
    def talk_about_school(self):
        pass

""" -------------------------------------------------------------------------------------------------- """

"""
Para fazer com que nossa interface IPerson esteja em conformidade com o princípio do ISP, segregamos os
ações para diferentes interfaces. Classes (Desenvolvedor, Enfermeira e Filho) podem apenas herdar da interface IPerson e implementar seu próprio 
comportamento.

"""

class IPerson:
    def talk_about(self):
        raise NotImplementedError

class DevModel(IPerson):
    def talk_about(self):
        pass

class NurseModel(IPerson):
    def talk_about(self):
        pass

class SonModel(IPerson):
    def talk_about(self):
        pass