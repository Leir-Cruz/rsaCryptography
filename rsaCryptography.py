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
  
  def cipherBytes(strFile, publicKey):
    [n,e] = publicKey
    encodedMessage = strFile.encode()
    convertedMessage = int.from_bytes(encodedMessage, byteorder='big')
    print(f"Arquivo original em inteiros: {convertedMessage}\n")
    encryptedFile = pow(convertedMessage, e, n)
    return encryptedFile
  
  def decryptBytes(cipherText,n ,privateKey):
    decrypted = pow(cipherText, privateKey, n)
    return decrypted