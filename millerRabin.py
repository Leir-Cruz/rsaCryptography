import random
from utils import Utils
class MillerRabin:

  def isPrime(number, rounds=40):
    if number == 2 or number == 3:
      return True

    if number % 2 == 0:
      return False
    
    u = number -1
    k = 0

    while(u % 2 == 0):
      u //= 2
      k+= 1
    for _ in range(rounds):
      a = random.randint(2, number - 2)
      b = pow(a, u, number)
      if a == 1 or a == number - 1:
        continue
      for _ in range(k - 1):
        b = pow(b, 2, number)
        if b == number - 1:
          break
        else:
          return False
    return True
    

  def generatePrime():
    print("Gerando número primo de 1024 bits... isso pode demorar um pouco")
    while True:
      randomNumber = random.getrandbits(1024)
      if(MillerRabin.isPrime(randomNumber)):
        print("Número primo gerado com sucesso!")
        print(f"{randomNumber}\n")
        return randomNumber
  
  def totientFunction(a, b):
    n = a * b
    totientNumber = (a - 1)* (b -1)
    return [n, totientNumber]
  
  def findTotientE(totientNumber):
    print("Gerando coPrimo da chave pública... isso pode demorar um pouco")
    while True:
      e = random.randint(2, totientNumber)
      if(Utils.isMutuallyPrime(totientNumber, e)):
        print(f"coPrimo para chave pública encontrado!")
        print(f"{e}\n")
        return e  
  
  
  def findPublicKeyAndTotient(primeA, primeB):
    [n, totientNumber] = MillerRabin.totientFunction(primeA, primeB)
    e = MillerRabin.findTotientE(totientNumber)
    publicKey = [n, e, totientNumber]
    return publicKey
  

  
"""   def findPrivateKey(totientNumber, totientE):
    print("Gerando chave privada... isso pode demorar um pouco ")
    totientD = 0
    while(((totientD * totientE) % totientNumber)!=1):
      totientD += 1
    return totientD """


    