## Inicia la sesión personalizada. Se le solicita al usuario su nombre. 
## Diccionario vacío, para que guarde temporalmente usuarios.

usuarios_registrados = {}
usuarioregistrado = 000

def iniciar_sesion():
    usuario = input("Ingrese su nombre de usuario: ")
    if usuario in usuarios_registrados:
        contraseña = input("Ingrese su contraseña: ")
        if usuarios_registrados[usuario] == contraseña:
            print("¡Inicio de sesión exitoso!")
        else:
            print("Contraseña incorrecta.")
    else:
        print("Usuario no registrado.")
        registrar_usuario()

def registrar_usuario():
    global usuarioregistrado
    usuario = input("Ingrese un nombre de usuario nuevo: ")
    if usuario in usuarios_registrados:
        print("Este nombre de usuario ya está registrado.")
    else:
        contraseña = input("Ingrese una contraseña: ")
        usuarios_registrados[usuario] = contraseña
        print("¡Registro exitoso!")

# Si el usuario responde como no debe
print("Bienvenido a la agencia NNNNN la mejor opción para ti y tu familia.")
while True:
    opcion = input("¿Desea iniciar sesión (I) o registrarse (R)? ").upper()
    if opcion == "I":
        iniciar_sesion()
        break
    elif opcion == "R":
        registrar_usuario()
        break
    else:
        print("Opción inválida. Por favor, seleccione 'I' para iniciar sesión o 'R' para registrarse.")