import math
from utils import Utils
class Oaep:
  def calculateK(totientModulus: int):
    k = math.ceil(totientModulus.bit_length() / 8)
    return k 

  def generatePaddingString(k, bytesMessageSize, hashLength):
    paddingSize = k - bytesMessageSize - 2 * hashLength - 2
    paddingString = b'\x00' * paddingSize
    return paddingString

  def oaepEncode(bytesMessage, n, label):
    [generatedHash, generatedHashSize] = Utils.hashLabel(label)
    k = Oaep.calculateK(n)
    seed = Utils.generateRandomSeed(generatedHashSize)
    paddingString = Oaep.generatePaddingString(k,len(bytesMessage),generatedHashSize)
   
    dataBlock = generatedHash + paddingString + b'\x01' + bytesMessage
    dataBlockMask = Utils.mgf1(seed, k - generatedHashSize - 1)
    maskedDataBlock = Utils.xor(dataBlock, dataBlockMask)
   
    seedMask = Utils.mgf1(maskedDataBlock, generatedHashSize)
    maskedSeed = Utils.xor(seed, seedMask)
    encoded = b'\x00' + maskedSeed + maskedDataBlock
    return [encoded, dataBlockMask, seedMask]

  def oaepDecode(encodedDataBlock, dataBlockMask, seedMask,encodedMessageSize,label):
    encodedDataBlockBytes = encodedDataBlock.to_bytes(encodedMessageSize, byteorder= 'big')
    [generatedHash, generatedHashSize] = Utils.hashLabel(label)
    maskedSeed = encodedDataBlockBytes[1: generatedHashSize] 
    maskedDataBlock = encodedDataBlockBytes[generatedHashSize + 1 :]

    seed = Utils.xor(maskedSeed, seedMask)
    dataBlock = Utils.xor(maskedDataBlock, dataBlockMask)

    blockHash = dataBlock[:generatedHashSize]
    assert blockHash == generatedHash
    i = generatedHashSize
    while i < len(dataBlock):
        if dataBlock[i] == 0:
            i += 1
            continue
        elif dataBlock[i] == 1:
            i += 1
            break
        else:
            raise Exception()
    message = dataBlock[i:]
    return message
    

    


