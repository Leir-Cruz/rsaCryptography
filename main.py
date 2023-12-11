from rsaCryptography import RsaCryptography

if __name__ == "__main__":
  file = open("test.txt", "r")
  message = file.read()
  print(f"Arquivo: {message}\n")

  cipherText = RsaCryptography.cipher(message,)
  print(f"Arquivo cifrado: {cipherText}\n")

  originalText = RsaCryptography.decrypt(cipherText)
  print(f"Arquivo decifrado: {originalText}\n")

