def username(uName, uLastname):

    Nombre_anterior = uName.split(" ")
    Apellido_anterior = uLastname.split(" ")
    Nombre = Nombre_anterior[0]
    Apellido = Apellido_anterior[0]
    return Nombre+" "+Apellido
