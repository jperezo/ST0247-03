from collections import defaultdict
potatoes=defaultdict(list)
pathfile = "dataset.txt"
proceced=[]
actualNode=0

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

def closestneighbor(node):
    a=potatoes.get(node)
    node=node-1
    a.pop(node)
    a.insert(node,10000)
    index=a.index(min(a))+1
    return index
def main(initialNode):
    makemap()
    actualNode=initialNode
    i=0
    while i <= len(potatoes):
        proceced.append(actualNode)
        if actualNode not in proceced:
            procecedNode=actualNode
            actualNode=potatoes.pop(closestneighbor(procecedNode), None)
        i=i+1


main(1)
print(potatoes)



