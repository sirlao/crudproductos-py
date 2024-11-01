import os

productos = []

def añadir_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = input("Ingrese el precio del producto: ")  
    cantidad = input("Ingrese la cantidad disponible: ") 
    
    
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    productos.append(producto)
    print("Producto añadido.")  

def ver_productos():
    if not productos:
        print("No hay productos en el inventario.")
    else:
        print("Lista de productos:")
        for i, producto in enumerate(productos):  
            
            print(f"{i+1}. Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

def actualizar_producto():
    ver_productos()
    indice = input("Seleccione el número del producto que desea actualizar: ")  
    try:
        producto = productos[int(indice) - 1] 
    except (IndexError, ValueError):
        print("Producto no encontrado.")  
        return
    
    
    nuevo_nombre = input("Ingrese el nuevo nombre del producto (o presione Enter para mantener el actual): ")
    if nuevo_nombre:
        producto['nombre'] = nuevo_nombre

    nuevo_precio = input("Ingrese el nuevo precio del producto (o presione Enter para mantener el actual): ")
    if nuevo_precio:
        producto['precio'] = nuevo_precio  
    
    nueva_cantidad = input("Ingrese la nueva cantidad del producto (o presione Enter para mantener el actual): ")
    if nueva_cantidad:
        producto['cantidad'] = nueva_cantidad 
    
    print("Producto actualizado.")  

def eliminar_producto():
    ver_productos()
    nombre = input("Ingrese el nombre del producto que desea eliminar: ")
    global productos
    
    productos = [p for p in productos if p["nombre"] != nombre]
    print("Producto eliminado.")  

def guardar_datos():
    try:
        
        with open("productos.txt", "w") as archivo:
            for producto in productos:
                archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
        print("Datos guardados en archivo.")  
    except Exception as e:
        print("Error al guardar datos.")  

def cargar_datos():
    
    try:
        with open("productos.txt", "r") as archivo:
            for linea in archivo:
                
                nombre, precio, cantidad = linea.strip().split(",")
                productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
        print("Datos cargados desde archivo.")  
    except Exception:
        print("No se pudo cargar los datos.") 

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
