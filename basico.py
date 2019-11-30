import re #libreria de expreciones regulares

path = "orden.java"

try:
    archivo = open(path, 'r')
except:
    print ("El archivo que intentas abrir no existe")
    quit()

texto = " "
for linea in archivo:
         texto += linea
        
print (texto)

patron3=re.compile('[a-zA-Z][\w\d]*')
result3=patron3.findall(texto)
#print("\n Resultado de busqueda variables validas: ", result3)

for i in result3:
    if(i!="console" and i!="log"  and i!="shift" and i!="find" and i!="new" and i!="Set" and i!="println" and i!="void"  and i!="IOException"  and i!="double"
    and i!="of"  and i!="lenght"  and i!="this" and i!="delete"  and i!="includes" and i!="System" and i!="String" and i!="main" and i!="io" and i!="java" and i!="import"
    and i!="return" and i!="Array" and i!="break" and i!="case" and i!="catch" and i!="class" and i!="default" and i!="do" and i!="else" and i!="package" and i!="args"
    and i!="extends" and i!="for" and i!="function" and i!="if" and i!="implements" and i!="include" and i!="interface" and  i!="print" and i!="out"
    and i!="private" and i!="protected" and i!="public" and i!="require" and i!="static" and i!="switch" and i!="throws" and i!="try" and i!="use" and i!="while" and i!="true" and i!="false"):

        print("Variables validas: " +i )

patron = re.compile('[\d]+[.]?[\d]')
result = re.findall(patron,texto)

print("\n Resultado de busqueda, enteros y decimales: ", result)

patron2 = re.compile('[+-]|[\/]|[*]|[%]')
result2 = re.findall(patron2,texto)

print("\n Resultado de busqueda Operadores aritmeticos: ", result2)

#patron4 = re.compile('\w+={2}\w+|\w+<{1}\w+|\w+>{1}\w+|\w+<={1}\w+|\w+>={1}\w+|\w+!={1}\w+')
patron4 = re.compile('>[=]?|<[=]?|==|!=')
result4 = re.findall(patron4,texto)

print("\n Resultado de busqueda Operadores relacionales: ", result4)

patron5 = r"\bint|\babstract|\bassert|\bboolean|\bbreak|\bbyte|\bcase|\bcatch|\bchar|\bclass|\bconst|\bcontinue|\bdefault|\bdo|\bdouble|\belse|\benum|\bextends|\bfinal|\bfinally|\bfloat|\bfor|\bgoto|\bif|\bimplements|\bimport|\binstanceof|\binterface|\blong|\bnative|\bnew|\bpackage|\bprivate|\bprotected|\bpublic|\breturn|\bshort|\bstatic|\bstrictfp|\bsuper|\bswitch|\bsynchronized|\bthis|\bthrow|\bthrows|\btransient|\btry|\bvoid|\bvolatile|\bwhile"
result5 = re.findall(patron5,texto)

print("\n Resultado de busqueda palabras reservadas: ", result5)





#patron = "\n"
#result = re.split(patron, texto)

#print("\n Resultado de busqueda ", result)

#patron  = "Orden"
#result = re.sub(patron, "puerto Araña", texto)

#print("\n Resultado de busqueda", result)