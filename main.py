from rsaCryptography import RsaCryptography
from millerRabin import MillerRabin

if __name__ == "__main__":
  file = open("test.txt", "r")
  message = file.read()
  print(f"Arquivo: {message}\n")

  primeA = MillerRabin.generatePrime()
  primeB = MillerRabin.generatePrime()

"""   cipherText = RsaCryptography.cipher(message,)
  print(f"Arquivo cifrado: {cipherText}\n")

  originalText = RsaCryptography.decrypt(cipherText)
  print(f"Arquivo decifrado: {originalText}\n")
 """
