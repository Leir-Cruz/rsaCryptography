from millerRabin import MillerRabin
from rsaCryptography import RsaCryptography
from signature import Signature

if __name__ == "__main__":
  file = open("test.txt", "r")
  message = file.read()
  print(f"Arquivo: {message}")
  hashMessage = Signature.hashMessage(message)
  print(f"Arquivo hash: {hashMessage}")

  primeA = MillerRabin.generatePrime()
  primeB = MillerRabin.generatePrime()

  [n, e, totientNumber] = MillerRabin.findPublicKeyAndTotient(primeA, primeB);
  publicKey = [n, e]
  print(f"par chave pública: {publicKey}\n")

  privateKey = MillerRabin.findPrivateKey(totientNumber, e)
  print(f"chave privada: {privateKey}\n")

  signature = Signature.genSignature(message, privateKey, n)
  print(f"assinatura: {signature}")

  signatureBytes = Signature.getSignatureBytes(signature)

  [cipherText, dataBlockMask, seedMask, encodedMessageSize] = RsaCryptography.oaepCipherWithSignature(signatureBytes, publicKey)
  print(f"Arquivo cifrado: {cipherText}\n")

  if((privateKey * e) % totientNumber):
    originalText = RsaCryptography.oaepDecrypt(cipherText, n, privateKey, dataBlockMask, seedMask, encodedMessageSize)
    print(f"Arquivo decifrado: {originalText}\n")
  else:
    print("erro ao encontrar chave privada!")





  #rec = Signature.getOriginalMessage(signature, e, n, len(hashMessage))
  #print(f"original: {rec}")
