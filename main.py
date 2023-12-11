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

  cipherText = RsaCryptography.cipher(message, publicKey)
  print(f"Arquivo cifrado: {cipherText}\n")


"""   privateKey = MillerRabin.findPrivateKey(totientNumber, e)
  print(f"chave privada: {privateKey}\n")

  originalText = RsaCryptography.decrypt(cipherText, privateKey)
  print(f"Arquivo decifrado: {originalText}\n") """
