from millerRabin import MillerRabin
from rsaCryptography import RsaCryptography

if __name__ == "__main__":
  file = open("test.txt", "r")
  message = file.read()
  print(f"Arquivo: {message}\n")

  primeA = MillerRabin.generatePrime()
  primeB = MillerRabin.generatePrime()

  [n, e, totientNumber] = MillerRabin.findPublicKeyAndTotient(primeA, primeB);
  publicKey = [n, e]
  print(f"par chave pública: {publicKey}\n")

  privateKey = MillerRabin.findPrivateKey(totientNumber, e)
  print(f"chave privada: {privateKey}\n")

  RsaCryptography.oaepCipher(message, publicKey)