"""
Digamos que você seja um gerente e tenha algumas pessoas como funcionário, 
algumas das quais são desenvolvedores, outras são designers gráficos e o resto são testadores.

"""

class Manager(object):
    def __init__(self):
        self.developers=[]
        self.designers=[]
        self.testers=[]
  
    def addDeveloper(self,dev):
        self.developers.append(dev)
          
    def addDesigners(self,design):
        self.designers.append(design)
          
    def addTesters(self,testers):
        self.testers.append(testers)
  
      
class Developer(object):
    def __init__(self):
        print("Desenvolvedor.")
      
class Designer(object):
    def __init__(self):
        print("Designer.")
      
class Testers(object):
    def __init__(self):
        print("Testador.")
      
if __name__ == "__main__":
    a=Manager()
    a.addDeveloper(Developer())
    a.addDesigners(Designer())

""" -------------------------------------------------------------------------------------------------- """

"""
Digamos que você seja um gerente e tenha algumas pessoas como funcionário, 
algumas das quais são desenvolvedores, outras são designers gráficos e o resto são testadores.

"""

class Employee(object):
    def Work():
        pass
      
class Manager():
    def __init__(self):
        self.employees=[]
    def addEmployee(self,a):
        self.employees.append(a)
   
class Developer(Employee):
    def __init__(self):
        print("Desenvolvedor")
    def Work():
        print("Quero mais café...")
          
class Designer(Employee):
    def __init__(self):
        print("Designer")
    def Work():
        print("Esse layout está lindo demais...")
          
class Testers(Employee):
    def __init__(self):
        print("Testador")
    def Work():
        print("Vamos achar algum bug hoje...")

class ProductOwner(Employee):
    def __init__(self):
        print("PO")
    def Work():
        print("Meu cliente está esperando...")

if __name__ == "__main__":
    a=Manager()
    a.addEmployee(Developer())
    a.addEmployee(Designer())
    a.addEmployee(ProductOwner())