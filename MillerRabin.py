import random

class MillerRabin:

  def generatePrime():
    print("Gerando dois números primos... isso pode demorar um pouco\n")
    while True:
      randomNumber = random.getrandbits(1024)

    return 0 #//todo
  
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


    