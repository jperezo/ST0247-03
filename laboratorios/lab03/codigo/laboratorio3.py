def Reinas(solucion,etapa,n):
	if etapa>=n:                    
		return False
	#solucion.append(0)
	exito = False                   
	
	while True:
            if (solucion[etapa] < n):                      
                solucion[etapa] = solucion[etapa] + 1       

            if (Valido(solucion,etapa)):                    

                if etapa != n-1:                            
                    exito = Reinas(solucion, etapa+1,n)
                    if exito==False:
                        solucion[etapa+1] = 0

                else:
                    print solucion                        
                    for x in range(n):
                        for i in range(n):
                            if solucion[x] == i+1:
                                print "X",
                            else:
                                print "- ",

                        print "\n"
                    exito = True
            if (solucion[etapa]==n or exito==True):         
                break
	return exito


def Valido(solucion,etapa):
	for i in range(etapa):
		if(solucion[i] == solucion[etapa]) or (ValAbs(solucion[i],solucion[etapa])==ValAbs(i,etapa)):
			return False

	return True

def ValAbs(x,y):
	if x>y:
		return x - y
	else:
		return y - x	

print "Introduce el numero de reinas:\n"
n = input()
solucion = []
for i in range(n):
	solucion.append(0)
etapa = 0
print Reinas(solucion, etapa, n)