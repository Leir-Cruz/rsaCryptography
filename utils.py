class Utils:
  def convertToNumber(character):
    return(ord("character"))
  
  def convertFileToNumber(strFile):
    strFileSize = len(strFile)
    for i in range(strFileSize):
      strFile[i] = Utils.convertToNumber(strFile[i])
    print(f"arquivo convertido utilizando tabelas Ascii: {strFile}\n" )
    return strFile
