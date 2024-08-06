import json

def abrirArchivo():
    miJSON=[]
    with open('info.json','r') as openfile:
        miJSON= json.load(openfile)
    return miJSON

def guardarArchivo(miData):
    with open("info.json","w") as outfile:
        json.dump(miData,outfile)


print("\n1.ventas \n2.compras \n3.informes ")
x=int(input("elije una opcion"))
miInfo=[]
 
if(x==1):
    nuevo_producto = {}
    nuevo_producto["fecha_venta"] = input("fecha de venta: ")
    nuevo_producto["nombre_cliente"] = input("Nombre del cliente: ")
    nuevo_producto["nombre_vendedor"] = input("nombre del vendedor: ")
    nuevo_producto["producto"] = (input("producto: "))
    
    miInfo = abrirArchivo()
    miInfo[0]["ventas"].append(nuevo_producto)
    guardarArchivo(miInfo)
    print("producto agregado.")

elif(x==2):
       miInfo=abrirArchivo()
       for i in miInfo[0]["ventas"]:
        print("################")
        print("")
        print("fecha de venta:",i["fecha_venta"])
        print("Nombre del cliente:",i["nombre_cliente"])
        print("nombre del vendedor:",i["nombre_vendedor"])
        print("producto:",i["producto"])
       



