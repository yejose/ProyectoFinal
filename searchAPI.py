from flask.templating import render_template
from difflib import get_close_matches
from flask import Flask, request
import db

def busqueda(busqueda_parametro):

    busqueda = busqueda_parametro
    platos = db.consultarTodosProductos()
    platos_nombres = []
    for i in platos:
        nombre = i[1]
        platos_nombres.append(nombre)

    print(platos_nombres)
    print(busqueda)
    resultados = get_close_matches(busqueda, platos_nombres, n=3, cutoff=0.4)
    print(resultados)
    #Traer informacion del plato obtenido
    return resultados