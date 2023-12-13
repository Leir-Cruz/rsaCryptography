import hashlib

class Signature:
  def hashMessage(message):
    message = message.encode()
    hasher = hashlib.sha3_256()
    hasher.update(message)
    updatedHash = hasher.digest()
    return updatedHash

  def genSignature(encodedMessage, privateKey, n):
    convertedMessage = int.from_bytes(encodedMessage, byteorder='big')
    encryptedFile = pow(convertedMessage, privateKey, n)
    signature = encryptedFile
    return signature
  
  def getSignatureBytes(signature, lenBytes=256):
    signature = signature.to_bytes(lenBytes, byteorder='big')
    return signature

  
  def getOriginalMessage(encodedSignature, e, n, lenBytes):
    decrypted = pow(encodedSignature, e, n)
    signature = decrypted.to_bytes(lenBytes, byteorder='big')
    return signature