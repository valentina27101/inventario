from colorama import Fore, Back, Style, init
init () #Inicializa colorama
print(Fore.MAGENTA + "----------------------------")
#Mensaje de bienvenida 
print(Fore.MAGENTA+ "Bienvenido a el inventario")
print(Fore.MAGENTA + "----------------------------")
print(Fore.MAGENTA)

#Solicitar nombre del producto
while True:
   nombre = input("ingrese el nombre del producto: ")

   if nombre.isalpha():
       print("nombre válido.")
       break
   else:
       print("Error: solo se permiten letras.")

#Validar precio 
while True:
    try:
        precio_unitario = float(input("ingrese el precio del producto: "))
        break
    except ValueError:
        print("Error: debe ingresar un precio válido.")
#Validar cantidad
while True:
    try:
        cantidad = int(input("ingrese la cantidad de productos: "))
        break
    except ValueError:
        print("Error: debe ingresar un número válido para la cantidad.")

#Validar costo
costo_total = (precio_unitario * cantidad)

#Datos fianles
print(Fore.MAGENTA + "----------------------------")
print(Fore.MAGENTA+ "factura")
print(Fore.MAGENTA + "----------------------------")
print("nombre del producto:", nombre) 
print("precio unitario:", precio_unitario)
print("cantidad:", cantidad)
print("costo total:", costo_total)
