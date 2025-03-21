productos = {}

options = [
    "Agregar producto",
    "Eliminar producto",
    "Mostrar inventario",
    "Salir"
]

user_input = int(0)

while(user_input != 3):
    print("Menú de usuario\n ................")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
        print("................")

    while True:
        try:
            user_input = int(input("Ingrese el número de opción deseada: ")) - 1
            if user_input < 0 or user_input > 3:
                raise ValueError
            break  # Sale del bucle si el input es válido
        except ValueError:
            print("Ingrese un número válido.")

    print("")

    if(user_input == 0):
        nombreProd = input("Ingrese el nombre del producto: ")
        stockProd = int(input("Ingrese el stock del producto "+ nombreProd + ": "))
        if nombreProd in productos:
            productos[nombreProd] += stockProd
        else:
            productos[nombreProd] = stockProd
    
    elif(user_input == 1):
        prodAEliminar = input("Ingrese el nombre del producto a eliminar: ")
        print("................")
        if prodAEliminar in productos:
            productos.pop(prodAEliminar)
            print(f"El producto {prodAEliminar} fue eliminado con éxito")
        else:
            print(f"El producto {prodAEliminar} no se encontró en la lista")

    elif(user_input == 2):
        print("Listado del inventario \n ................")
        for nombreProd, stockProd in productos.items():
            print(f" -> {nombreProd}: {stockProd}")
    
    elif(user_input == 3):
        print("Programa cerrado con exito")
    
    print("................")


#Implementar utilizando diccionarios, reestructurar la lista
#productos = [nombreProd = stockProd]
#Ejemplo diccionario -> https://www.w3schools.com/python/python_dictionaries.asp