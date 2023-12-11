import random

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
    e = 0 #//todo
    return e
  
  def findTotientD(totientE):
    d = 0
    return d
  
  def findPublicKey(primeA, primeB):
    [n, totientNumber] = MillerRabin.totientFunction(primeA, primeB)
    e = MillerRabin.findTotientE(totientNumber)
    publicKey = [n, e]
    return publicKey
  
  def findPrivateKey(publicKey):
    [n, totientE] = publicKey
    totientD = MillerRabin.findTotientD(totientE)
    privateKey = [n, totientD]
    return privateKey


    