def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")

def unidades_categoria(categoria, productos, stock):
    total = 0
    cat_buscar = categoria.strip().lower()
    for cod, datos in productos.items():
        if datos[1].lower() == cat_buscar:
            if cod in stock:
                total += stock[cod][1]
    print(f"El total de unidades disponibles es: {total}")

def busqueda_precio(p_min, p_max, productos, stock):
    resultados = []
    for cod, datos_stock in stock.items():
        precio = datos_stock[0]
        unidades = datos_stock[1]
        if p_min <= precio <= p_max and unidades > 0:
            if cod in productos:
                nombre = productos[cod][0]
                resultados.append(f"{nombre}--{cod}")
    
    if resultados:
        resultados.sort()
        print(f"Los productos encontrados son: {resultados}")
    else:
        print("No hay productos en ese rango de precios.")

def buscar_codigo(codigo, productos):
    return codigo.upper() in productos

def actualizar_precio(codigo, nuevo_precio, productos, stock):
    cod_upper = codigo.upper()
    if buscar_codigo(cod_upper, productos):
        if cod_upper in stock:
            stock[cod_upper][0] = nuevo_precio
            return True
    return False

def validar_codigo_vacio(codigo):
    return len(codigo.strip()) > 0

def validar_nombre(nombre):
    return len(nombre.strip()) > 0

def validar_categoria(categoria):
    return len(categoria.strip()) > 0

def validar_marca(marca):
    return len(marca.strip()) > 0

def validar_peso(peso_str):
    try:
        peso = float(peso_str)
        return peso > 0
    except ValueError:
        return False

def validar_es_importado(resp):
    return resp.strip().lower() in ['s', 'n']

def validar_es_para_cachorro(resp):
    return resp.strip().lower() in ['s', 'n']

def validar_precio(precio_str):
    try:
        precio = int(precio_str)
        return precio > 0
    except ValueError:
        return False

def validar_unidades(unidades_str):
    try:
        unidades = int(unidades_str)
        return unidades >= 0
    except ValueError:
        return False

def agregar_producto(codigo, nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro, precio, unidades, productos, stock):
    cod_upper = codigo.upper()
    if buscar_codigo(cod_upper, productos):
        return False
    
    imp_bool = True if es_importado.lower() == 's' else False
    cach_bool = True if es_para_cachorro.lower() == 's' else False
    
    productos[cod_upper] = [nombre, categoria, marca, float(peso_kg), imp_bool, cach_bool]
    stock[cod_upper] = [int(precio), int(unidades)]
    return True

def eliminar_producto(codigo, productos, stock):
    cod_upper = codigo.upper()
    if buscar_codigo(cod_upper, productos):
        if cod_upper in productos:
            del productos[cod_upper]
        if cod_upper in stock:
            del stock[cod_upper]
        return True
    return False

def main():
    productos = {
        'M001': ['Alimento Premium', 'comida', 'DogPlus', 10.0, True, False],
        'M002': ['Arena Aglomerante', 'higiene', 'CatClean', 8.0, False, False],
        'M003': ['Snack Dental', 'snack', 'BiteJoy', 1.0, True, True],
        'M004': ['Shampoo Suave', 'higiene', 'PetCare', 0.5, False, True],
        'M005': ['Correa Nylon', 'accesorio', 'WalkPro', 0.3, True, False],
        'M006': ['Cama Mediana', 'accesorio', 'CozyPet', 2.0, False, False]
    }

    stock = {
        'M001': [32990, 12],
        'M002': [9990, 0],
        'M003': [5490, 25],
        'M004': [7990, 5],
        'M005': [11990, 7],
        'M006': [24990, 3]
    }

    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Unidades por categoría")
        print("2. Búsqueda de productos por rango de precio")
        print("3. Actualizar precio de producto")
        print("4. Agregar producto")
        print("5. Eliminar producto")
        print("6. Salir")
        print("=====================================")
        
        opcion = leer_opcion()
        
        if opcion == 1:
            categoria = input("Ingrese categoría a consultar: ")
            unidades_categoria(categoria, productos, stock)
            
        elif opcion == 2:
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                        break
                    else:
                        print("Debe ingresar valores enteros válidos (mínimo menor o igual al máximo y mayores a cero)")
                except ValueError:
                    print("Debe ingresar valores enteros")
            busqueda_precio(p_min, p_max, productos, stock)
            
        elif opcion == 3:
            while True:
                codigo = input("Ingrese código del producto: ")
                nuevo_precio_str = input("Ingrese nuevo precio: ")
                
                if validar_precio(nuevo_precio_str):
                    nuevo_precio = int(nuevo_precio_str)
                    if actualizar_precio(codigo, nuevo_precio, productos, stock):
                        print("Precio actualizado")
                    else:
                        print("El código no existe")
                else:
                    print("El precio debe ser un valor entero positivo")
                    
                resp = input("¿Desea actualizar otro precio (s/n)?: ")
                if resp.strip().lower() == 'n':
                    break
                    
        elif opcion == 4:
            codigo = input("Ingrese código del producto: ")
            nombre = input("Ingrese nombre: ")
            categoria = input("Ingrese categoría: ")
            marca = input("Ingrese marca: ")
            peso_str = input("Ingrese peso (kg): ")
            es_importado = input("¿Es importado? (s/n): ")
            es_para_cachorro = input("¿Es para cachorro? (s/n): ")
            precio_str = input("Ingrese precio: ")
            unidades_str = input("Ingrese unidades: ")
            
            if buscar_codigo(codigo, productos):
                print("El código ya existe")
                continue
                
            valido = True
            if not validar_codigo_vacio(codigo):
                valido = False
            if not validar_nombre(nombre):
                valido = False
            if not validar_categoria(categoria):
                valido = False
            if not validar_marca(marca):
                valido = False
            if not validar_peso(peso_str):
                valido = False
            if not validar_es_importado(es_importado):
                valido = False
            if not validar_es_para_cachorro(es_para_cachorro):
                valido = False
            if not validar_precio(precio_str):
                valido = False
            if not validar_unidades(unidades_str):
                valido = False
                
            if valido:
                if agregar_producto(codigo, nombre, categoria, marca, peso_str, es_importado, es_para_cachorro, precio_str, unidades_str, productos, stock):
                    print("Producto agregado")
                else:
                    print("El código ya existe")
            else:
                print("Error: Uno o más datos ingresados no cumplen con las condiciones de validación.")
                
        elif opcion == 5:
            codigo = input("Ingrese código del producto a eliminar: ")
            if eliminar_producto(codigo, productos, stock):
                print("Producto eliminado")
            else:
                print("El código no existe")
                
        elif opcion == 6:
            print("Programa finalizado.")
            break

if __name__ == "__main__":
    main()