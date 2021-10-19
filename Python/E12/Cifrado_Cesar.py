import argparse, detectEnglish

def Cesar(message,clave):
    espacios = 1
    while espacios > 0:
        espacios = clave.count(' ')
        if clave.isalpha() == False:
            espacios += 1
    key = len(clave)
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    translated = ''
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex + key
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)
            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol
    print("Mensaje Crifrado: "+translated)

def Des_Cesar(message,clave):
    espacios = 1
    while espacios > 0:
        espacios = clave.count(' ')
        if clave.isalpha() == False:
            espacios += 1
    key = len(clave)
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    translated = ''
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)
            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol
    print("Mensaje descifrado: "+translated)

def Crackeo(message):
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    for key in range(len(SYMBOLS)):
        translated = ''
        for symbol in message:
            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                translatedIndex = symbolIndex - key
                if translatedIndex < 0:
                    translatedIndex = translatedIndex + len(SYMBOLS)
                translated = translated + SYMBOLS[translatedIndex]

            else:
                translated = translated + symbol
        if detectEnglish.isEnglish(translated):
            print()
            print("Possible encriptcion:")
            print("key %s: %s"%(key,translated[:100]))
            print("Enter D para salir o teclea para continuar: ")
            response=input(">")
            if response.strip().upper().startswith("D"):
                return translated
    return None


Opciones="""<------------------------ Cifrado Cesar ------------------------>
 Opcion    Descripcion                               Ejemplos   
-------- -------------- ------------------------------------------------------------------------
 [e]     Encriptar       python Vii.py  -name e -msg "Tu mensaje" -key ""Palabra clave a cifrar"
 [d]     Desencriptar    python Vii.py  -name d -msg "El mensaje" -key ""Calve para desencriptar"
 [c]     Crackear        python Vii.py  -name c -msg "El mensaje"
 """

parser=argparse.ArgumentParser(description="Encriptacion Cesar",
                                       epilog=Opciones, formatter_class=argparse.
                                       RawDescriptionHelpFormatter)

parser.add_argument("-name", metavar="Nombre", dest="Nombre", help="Nombre de la opcion", required=True)
parser.add_argument("-key", metavar="Clave", dest="Clave", help="Clave necesaria para cifrar")
parser.add_argument("-msg", metavar="Mensaje", dest="Mensaje", help="Mensaje",required=True)
params=parser.parse_args()
Name=params.Nombre.encode()
if Name.decode() == "e":
    mess=params.Mensaje.encode()
    key=params.Clave.encode()
    Cesar(mess.decode(),key.decode())
elif Name.decode()== "d":
    mess=params.Mensaje.encode()
    key=params.Clave.encode()
    Des_Cesar(mess.decode(),key.decode())
elif Name.decode()== "c":
    mess=params.Mensaje.encode()
    Crackeo(mess.decode())













    
