from utils import Utils
class RsaCryptography:
  def cipher(strFile, publicKey):
    [n,e] = publicKey 
    convertedFile = Utils.convertFileToNumber(strFile)
    convertedFileSize = len(convertedFile)
    for i in range(convertedFileSize):
      newLetter = pow(convertedFile[i],e,n)
      convertedFile[i] = newLetter
    return convertedFile
  
  def decrypt(intCipherText, privateKey):
    [n, d] = privateKey
    cipherTextSize = len(intCipherText)
    for i in range(cipherTextSize):
      newLetter = pow(intCipherText[i],d,n)
      intCipherText[i] = chr(newLetter)
    return intCipherText