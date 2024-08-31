# Facturación para que los usuarios tengan un número para poder consultar su solicitud
facturas = {}
numero_factura = 100000  

def registrar_paquete():
    global numero_factura
    nombre_completo = input("Ingrese su nombre completo: ")
    telefono = input("Ingrese su número de teléfono: ")
    cedula = input("Ingrese su cédula: ")
    
    # Aquí 
    preciopaquete = input("El valor de paquete es:  ")   ##AQUÍ DEBEMOS AGREGAR LOS PRECIOS !!!! REVISAR OJO!
    # Crear una factura con los datos del usuario y los detalles de la compra
    factura = {
        'nombre_completo': nombre_completo,
        'telefono': telefono,
        'cedula': cedula,
        'total_compra': preciopaquete,
        'numero_factura': numero_factura
    }
    
    # Guardar la factura en el diccionario de facturas
    facturas[numero_factura] = factura
    
    # Mostrar la factura al usuario
    print(f"\nFactura generada:")
    print(f"Número de factura: {numero_factura}")
    print(f"Nombre completo: {nombre_completo}")
    print(f"Teléfono: {telefono}")
    print(f"Cédula: {cedula}")
    print(f"Total de la compra: {preciopaquete}\n")
    
    # Incrementar el número de factura para la próxima compra
    numero_factura += 1

# Ejecución del programa
print("Bienvenido a la agencia que hará feliz tu corazón y a tu familia")
registrar_paquete()