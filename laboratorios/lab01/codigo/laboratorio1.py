from collections import defaultdict
potatoes=defaultdict(list)
pathfile = "dataset.txt"

def makemap():

    f = open(pathfile,"r")
    i=0
    for l in f :
        i=i+1
        if "Costo" in l:    
            break
    f.close()
    f = open(pathfile,"r")
    for line in f.readlines()[i:]:
        if not line.isspace():
            linelist=line.split()
            adArc(linelist[0],linelist[1],linelist[2])


def adArc (source, destination, weight):
    s=int(source)
    d=int(destination)
    w=int(weight)
    potatoes[s].insert(d,w)

makemap()
print(potatoes)