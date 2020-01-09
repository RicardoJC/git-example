import re
import io

regexPalabra = re.compile(r'(\w+(ir|er[oa]s?)\b)')

with io.open("quijote.txt","r",encoding = "utf-8") as entrada:
    textoQuijote = entrada.read()

if regexPalabra.findall(textoQuijote):
    print('Si encuentra con findall')
    pattern = regexPalabra.findall(textoQuijote)
    print(pattern)
    # Las siguientes lineas permiten escribir los resultados en un txt.
    #for resultado in pattern:
        #with io.open("salidaRegex.txt","a", encoding="utf-8") as salida:
            #salida.write(resultado[0] + ' : ' + resultado[1] + '\n')

