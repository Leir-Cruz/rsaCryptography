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
  

  def oaepCipher(strFile, publicKey, label=b""):
    [n,e] = publicKey
    bytesMessage = strFile.encode()
    [encodedMessage, dataBlockMask, seedMask] = Oaep.oaepEncode(bytesMessage, n, label)
    print(f"Arquivo pós oaep: {encodedMessage}")
    convertedMessage = int.from_bytes(encodedMessage, byteorder='big')
    print(f"Arquivo original em inteiros: {convertedMessage}")
    encryptedFile = pow(convertedMessage, e, n)
    return [encryptedFile,dataBlockMask, seedMask, len(encodedMessage)]
  
  def oaepDecrypt(cipherText, n, privateKey,dataBlockMask, seedMask,encodedMessageSize ,label=b""):
    decrypted = pow(cipherText, privateKey, n)
    print(f"Arquivo decifrado em inteiros: {decrypted}")
    message = Oaep.oaepDecode(decrypted, dataBlockMask, seedMask, encodedMessageSize ,label)
    return message
