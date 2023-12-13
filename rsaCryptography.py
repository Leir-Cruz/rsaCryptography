from oaepFunctions import Oaep
class RsaCryptography:
  
  def cipherBytes(strFile, publicKey):
    [n,e] = publicKey
    encodedMessage = strFile.encode()
    lenBytes = len(encodedMessage)
    convertedMessage = int.from_bytes(encodedMessage, byteorder='big')
    print(f"Arquivo original em inteiros: {convertedMessage}")
    encryptedFile = pow(convertedMessage, e, n)
    return [encryptedFile, lenBytes]
  
  def decryptBytes(cipherText,n ,privateKey, lenBytes):
    decrypted = pow(cipherText, privateKey, n)
    print(f"Arquivo decifrado em inteiros: {decrypted}")
    decoded = decrypted.to_bytes(lenBytes, byteorder='big').decode()
    return decoded
  

  def oaepCipher(strFile, publicKey):
    [n,e] = publicKey
    bytesMessage = strFile.encode()
    encodedMessage = Oaep.oaepEncode(bytesMessage, n)
    print(f"Arquivo pós oaep: {encodedMessage}")
