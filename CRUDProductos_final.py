import os

#Lista de productos
productos = []

#Define funcion de Agregar un producto
def añadir_producto():
    nombre = input("Ingrese nombre del producto: ")
    
    try:
        precio = float(input("Ingrese el precio: "))
        cantidad = int(input("Ingrese la cantidad: "))        
    except ValueError:
        print("Precio o cantidad no validos, ingrese datos correctos...")
        return
    
    #Crear Diccionario de datos del producto
    producto = {"nombre":nombre, "precio":precio, "cantidad":cantidad}
    productos.append(producto)
    print("Producto aniadido...")

#Listando productos
def ver_productos():
    if not productos:
        print("No hay productos en el inventario")
    else:
        print("Lista de productos")
        print("------------------")
        for i, producto in enumerate(productos, start=1):
            print(f"{i}. Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    
#Define el metodo de actualizar un producto
def actualizar_producto():
    ver_productos()
    
    nombre = input("Nombre del producto a actualizar: ")
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            print("Producto encontrado. Introduce los nuevos datos.")
            producto["nombre"] = input("Nuevo nombre del producto: ")
            producto["precio"] = float(input("Nuevo precio del producto: "))
            producto["cantidad"] = int(input("Nueva cantidad del producto: "))
            print("Producto actualizado correctamente.")
            return
    print("Producto no encontrado.")
    
#Metodo eliminar producto
def eliminar_producto():
    ver_productos()
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower():
            productos.remove(producto)
            print("Producto eliminado correctamente")
            return
    #El producto no existe
    print("Producto no encontrado")

#Metodo que guarda los datos
def guardar_datos():
    """Guarda los datos de productos en un archivo."""
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            linea = f"{producto['nombre']}, {producto['precio']}, {producto['cantidad']}\n"
            archivo.write(linea)
    print("Datos guardados correctamente.")
2
#Metodo de carga de datos
def cargar_datos():
    global productos
    
    try:
        with open('productos.txt', 'r') as archivo:
        
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(",")
                
                productos.append({
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad                
                }                                
                )
        print("Datos cargados desde productos.txt ...")
    except FileNotFoundError:
        print("El archivo productos.txt no existen, no se han cargado los productos")
        return productos

def menu():
    cargar_datos()
    while True:
        print("\n--- Sistema de Gestión de Productos ---")
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")
            
menu()