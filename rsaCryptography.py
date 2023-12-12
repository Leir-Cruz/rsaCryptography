from utils import Utils
class RsaCryptography:
  def cipher(strFile, publicKey):
    [n,e] = publicKey 
    convertedFile = Utils.convertFileToNumber(strFile)
    cryptedFile = [pow(ch, e, n) for ch in convertedFile]
    return cryptedFile
  
  def decrypt(intCipherText,n ,privateKey ):
    encodedMessage = [pow(ch, privateKey, n) for ch in intCipherText]
    print(encodedMessage)
    decryptedMessage =  "".join(chr(ch) for ch in encodedMessage)
    return decryptedMessage