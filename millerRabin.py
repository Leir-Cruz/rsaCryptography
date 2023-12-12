import random
from utils import Utils
class MillerRabin:

  def isPrime(number, rounds=40):
    if number == 2:
      return True

    if number % 2 == 0:
      return False
    
    r = 0
    s = number - 1

    while(s % 2 == 0):
      r+= 1
      s //= 2
    for _ in range(rounds):
      a = random.randrange(2, number - 1)
      x = pow(a, s, number)
      if x == 1 or x == number - 1:
        continue
      for _ in range(r - 1):
        x = pow(x, 2, number)
        if x == number - 1:
          break
      else:
        return False
    return True
  
  def randomOddValue():
    number = random.randint(2 ** (1023 -1), 2 ** 1024 -1)
    if number % 2 == 0:
      number += 1
    return number
    

  def generatePrime():
    print("Gerando número primo de 1024 bits... isso pode demorar um pouco")
    randomNumber = MillerRabin.randomOddValue()
    while MillerRabin.isPrime(randomNumber) == False:
      randomNumber += 2
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
      print(".")
      e = random.randint(2, totientNumber)
      if(Utils.isMutuallyPrime(totientNumber, e)):
        print(f"coPrimo para chave pública encontrado!")
        print(f"{e}\n")
        return e  
  
  
  def findPublicKeyAndTotient(primeA, primeB):
    [n, totientNumber] = MillerRabin.totientFunction(primeA, primeB)
    e = MillerRabin.findTotientE(totientNumber)
    return [n, e, totientNumber]
  

  def findPrivateKey(totientNumber, totientE):
    totientD = pow(totientE, -1, totientNumber)
    return totientD
