
imagelist = []
i = 0 
def list(x):
    global imagelist    
    imagelist.append(x)
    print (imagelist)
    print (len(imagelist))

def show():
    item = "kalimera"
    list(item)
    
show()
show()