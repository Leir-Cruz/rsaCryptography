import math
class Utils:
  def convertToNumber(character):
    return(ord(character))
  
  def convertFileToNumber(strFile):
    convertedFile = [Utils.convertToNumber(ch) for ch in strFile]
    print(f"arquivo convertido utilizando tabelas Ascii: {convertedFile}\n" )
    return convertedFile

  def isMutuallyPrime(primeNumber, randomNumber):
    if math.gcd(primeNumber, randomNumber) == 1:
      return True
    return False