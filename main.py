# Marcio Vinicius de Souza da Rocha
# documentação no arquivo README
# este VENV do replit está hospedado em 
# um [repositório do github](https://github.com/MarciovsRocha/Maquina_Estados_Finito)

# code...

ACCEPTED_CHARS = ['a','b']

# valida se uma string passada por parâmetro é válida ou não
def StringValida(s: str):
    valida=True
    index=0
    while len(s) > index:
        valida = (valida and (s[index] in ACCEPTED_CHARS))
        valida = (valida and ('b' == s[index+1]) and ('b' == s[index+2])) if 'a' == s[index] else valida
        index+=1
    return valida

def LoadFile(FilePath: str):
    FileLines = open(FilePath, 'r').readlines()
    return [lines.replace('\n','') for lines in FileLines]

def VerificaArquivo(FilePath: str, expor_result: bool = True):
    FileLines = LoadFile(FilePath)
    index = 1
    result=[]
    while (int(FileLines[0])+1) > index:
        result.append('{}: {}\n'.format(
            FileLines[index],
            'pertence' if StringValida(FileLines[index]) else 'não pertence')
        )
        index+=1
    SaveResult(FilePath, result)
    return result

# exporta 
def SaveResult(FileName: str, Lines):
    FileName = FileName.split('.')
    FileName = FileName[0]+'_RESULT.'+FileName[1]
    File = open(FileName, 'w')
    File.writelines(Lines)
    File.close()

validacao_arquivo1 = VerificaArquivo('arquivo1.txt')
