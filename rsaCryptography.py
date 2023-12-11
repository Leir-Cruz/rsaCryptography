from utils import Utils
class RsaCryptography:
  def cipher(strFile, publicKey):
    [n,e] = publicKey 
    convertedFile = Utils.convertFileToNumber(strFile)
    convertedFileSize = len(convertedFile)
    for i in range(convertedFileSize):
      newLetter = (convertedFile[i] ** e % n)
      convertedFile[i] = newLetter
    return convertedFile
  
  def decrypt(cipherText, privateKey):
    [n, d] = privateKey
    cipherTextSize = len(cipherText)
    for i in range(cipherTextSize):
      newLetter = (cipherText[i] ** d % n)
      cipherText[i] = newLetter
    return cipherText