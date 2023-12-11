import math
class Utils:
  def convertToNumber(character):
    return(ord(character))
  
  def convertFileToNumber(strFile):
    convertedFile = []
    strFileSize = len(strFile)
    for i in range(strFileSize):
      convertedFile.append(Utils.convertToNumber(strFile[i]))
    print(f"arquivo convertido utilizando tabelas Ascii: {convertedFile}\n" )
    return convertedFile

  def isMutuallyPrime(primeNumber, randomNumber):
    if math.gcd(primeNumber, randomNumber) == 1:
      return True
    return False