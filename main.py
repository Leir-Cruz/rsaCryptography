from rsaCryptography import RsaCryptography
from millerRabin import MillerRabin

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

  cipherText = RsaCryptography.cipherBytes(message, publicKey)
  print(f"Arquivo cifrado: {cipherText}\n")


  if((privateKey * e) % totientNumber):
    originalText = RsaCryptography.decryptBytes(cipherText, n, privateKey)
    print(f"Arquivo decifrado: {originalText}\n")
  else:
    print("erro ao encontrar chave privada!")
