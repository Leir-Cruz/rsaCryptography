import math
import hashlib
import os

class Utils:
  def convertToNumber(character):
    return(ord(character))
  
  def convertFileToNumber(strFile):
    convertedFile = [Utils.convertToNumber(ch) for ch in strFile]
    print(f"arquivo convertido utilizando tabelas Ascii: {convertedFile}\n" )
    return convertedFile

  def isMutuallyPrime(primeNumber, randomNumber):
    if math.gcd(primeNumber, randomNumber) == 1:
      return True
    return False
  
  def hashLabel(label=b""):
    hasher = hashlib.sha1()
    hasher.update(label)
    updatedHash =  hasher.digest()
    hashSize = len(updatedHash)
    return [updatedHash, hashSize]
  
  def generateRandomSeed(seedSize):
    seed = os.urandom(seedSize)
    return seed

  def mgf1(seed, maskSize):
    mask = b''
    counter = 0
    while len(mask) < maskSize:
        counterBytes = counter.to_bytes(4, 'big')
        data = seed + counterBytes
        [hash_output, _] = Utils.hashLabel(data)
        mask += hash_output
        counter += 1
    return mask[:maskSize]
  

  def xor(list1, list2):
    masked = b''
    list1Size = len(list1)
    list2Size = len(list2)
    for i in range(max(list1Size, list2Size)):
        if i < list1Size and i < list2Size:
            masked += (list1[i] ^ list2[i]).to_bytes(1, byteorder='big')
        elif i < list1Size:
            masked += list1[i].to_bytes(1, byteorder='big')
        else:
            break
    return masked
