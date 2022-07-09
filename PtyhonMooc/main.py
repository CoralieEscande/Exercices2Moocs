def mon_decorateur(func):
  def inner(*args, **kwargs):
    #print('Nombre de manchots:', p.total())
    #print('Nombre de manchots:', func.__name__)
    func(*args, **kwargs)
    print('Nombre de manchots:', p.TOTAL)
    return
  #return inner

class Penguins:
  TOTAL = 2
  TOTAL = TOTAL + 1  
  #@classmethod
  #def total(self):
    #print('methode total', self.TOTAL)
    #return self.TOTAL
    
  @mon_decorateur
  def add(self):
    print('methode add', self.TOTAL)
    self.TOTAL = self.TOTAL +1
    print('methode add fin', self.TOTAL)
  @mon_decorateur
  def remove(self):
    print('methode remove', self.TOTAL)
    self.TOTAL -= 1
    print('methode remove fin', self.TOTAL)
    
if __name__ == "__main__":
  p = Penguins()
  p.add()
  p.remove()
  #print(Penguins.total())
