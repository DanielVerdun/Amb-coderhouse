# agrego test users fijos para poder probrar busqueda, baja y modificación.

base_de_datos = {
    "daniel7833": {
        'nombre': 'Daniel',
        'edad': '12',
        'password': '###'
    },
    "carolina87": {
        'nombre': 'Carolina',
        'edad': '12',
        'password': 'pw?'
    }
}

"""
imprimo lista comandos, se puede poner dentro del while,
pero para no inundar la pantalla con esto solo lo imprimo
al comienzo.
"""
print("los comandos que puede realizar son: ")
print("alta")
print("baja")
print("modificar")
print("buscar")
print("salir")

while True:
    comando = input("Ingrese comando: ")

    # convierto comando a lower, para evitar que falle si ingresa mayusculas
    comando = comando.lower()

    if comando == "alta":
        # Cargo formulario

        form_es_valido = True
        nombre_usuario = input("ingrese Usuario: ")
        nombre = input("ingrese Nombre: ")
        edad = input("Ingrese edad: ")
        password = input("ingrese password: ")
        repetir_password = input("vuelva a ingresar el password: ")

        # Valido campos
        if nombre_usuario[0].isnumeric():
            print("error: usuario no puede empezar con un número.")
            form_es_valido = False

        if nombre_usuario in base_de_datos:
            print("error: usuario ya existe.")
            form_es_valido = False

        if len(nombre) < 4:
            print("error: nombre tiene que ser mayor a tres caracteres")
            form_es_valido = False

        # si el string que se ingresa tiene un punto ya sabemos que no es entero
        # si el string que se ingresa no es numerico, ya sabemos que no es un entero
        if "." in edad or not edad.isnumeric():
            print("error: Edad tiene que ser un valor numérico entero")
            form_es_valido = False

        if len(password) != 3:
            print("error: Password tiene que ser igual a tres caracteres")
            form_es_valido = False

        """
        convierto a lista el string y pregunto si el caracter especial no esta dentro.
        password = "pw#"
        si hago  list(password) -> ["p","w","#"]
        entonces
        "#" in list(password) ->  True

        pero como estoy validando si no esta, uso el `not in`
        "#" not in list(password) -> False

        """
        if "?" not in list(password) and "#" not in list(password):
            print("error: Password tiene que tener almenos uno de estos caracteres ?, #")
            form_es_valido = False

        if password != repetir_password:
            print("Error: Passwords y repetir password no son iguales.")
            form_es_valido = False

        # Valido formulario

        if form_es_valido:
            info = {"nombre": nombre, "edad": edad, "password": password}
            base_de_datos[nombre_usuario] = info
            print(f"Se agregó con éxito el usuario: {nombre_usuario}")
            print(info)
        else:
            print("Formulario no es valido")


    elif comando == "baja":

        # busco el usuario en la base de datos

        buscar_usuario = input("ingrese Usuario: ")

        if buscar_usuario in base_de_datos:
            del base_de_datos[buscar_usuario]
            print(f"se borro con éxito el usuario {buscar_usuario}")
        else:
            print(f"Usuario ingresado {buscar_usuario} no existe")


    elif comando == "modificar":

        # busco el usuario en la base de datos

        buscar_usuario = input("ingrese Usuario: ")

        if buscar_usuario in base_de_datos:
            print("Usuario existe se puede modificar.")
        else:
            print(f"Usuario ingresado {buscar_usuario} no existe")
            continue


        # NO altero el nombre de usuario, solo modifico los campos.

        form_es_valido = True
        nombre = input("ingrese Nombre: ")
        edad = input("Ingrese edad: ")
        password = input("ingrese password: ")
        repetir_password = input("vuelva a ingresar el password: ")

        # valido campos del form

        if len(nombre) < 4:
            print("error: nombre tiene que ser mayor a tres caracteres")
            form_es_valido = False

        if "." in edad or not edad.isnumeric():
            print("error: Edad tiene que ser un valor numérico entero")
            form_es_valido = False

        if len(password) != 3:
            print("error: Password tiene que ser igual a tres caracteres")
            form_es_valido = False

        if "?" not in list(password) and "#" not in list(password):
            print("error: Password tiene que tener almenos uno de estos caracteres ?, #")
            form_es_valido = False

        if password != repetir_password:
            print("Error: Passwords y repetir password no son iguales.")
            form_es_valido = False

        # valido el formulario

        if form_es_valido:
            info = {"nombre": nombre, "edad": edad, "password": password}
            base_de_datos[nombre_usuario] = info
            print(f"Se modificó con éxito el usuario: {nombre_usuario}")
            print(info)
        else:
            print("Formulario no es valido")


    elif comando == "buscar":
        dato = input("Ingrese usuario:")
        if dato in base_de_datos:
            print(base_de_datos[dato])
        else:
            print(f"NO se encuentra {dato}")

    elif comando == "salir":
        break
    else:
        print("no entiendo el comando")