from millerRabin import MillerRabin
from rsaCryptography import RsaCryptography
from signatureFunctions import Signature

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

  signature = Signature.genSignature(hashMessage, privateKey, n)
  print(f"assinatura: {signature}\n")

  rec = Signature.getOriginalMessage(signature, e, n, len(hashMessage))
  print(f"original: {rec}")
