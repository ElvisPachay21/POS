carrito = []
total = 0.0

def mostrar_menu():
    print("Bienvenido al POS")
    print("1. Agregar producto al carrito")
    print("2. Ver total del carrito")
    print("3. Pagar")
    print("4. Salir")
 
def agregar_producto():
    global total 
    
    producto = input("Ingrese el nombre del producto: ")
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            break
        except ValueError:
            print("Por favor, ingrese un valor numérico para el precio.")
    
    carrito.append({"producto": producto, "precio": precio})
    total += precio
    print(f"Has agregado {producto} al carrito por {precio:.2f}.")
    
def ver_total():
    print(f"El total de tu carrito es: {total:.2f}")

def pagar():
    global total, carrito 
    if total == 0:
        print("Tu carrito está vacío, no hay nada que pagar.")
    else: 
        print(f"El total a pagar es: {total:.2f}")
        while True:
            try:
                pago = float(input("Ingresa la cantidad con la que vas a pagar: "))
                break
            except ValueError:
                print("Por favor, ingresa un valor numérico para el pago.")
        
        if pago >= total:
            cambio = pago - total
            print(f"Pago realizado con éxito. Tu cambio es: {cambio:.2f}")
            
            carrito = []
            total = 0.0
        else:
            print("No tienes suficiente dinero para pagar.")
            
def ejecutar():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            ver_total()
        elif opcion == "3":
            pagar()
        elif opcion == "4":
            print("Gracias por usar el POS. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

ejecutar()
          


#return carrito
# producto, precio = agregar_producto()
#print(producto, precio)
#mostrar_menu()
