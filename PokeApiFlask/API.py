from os import name
import re
from flask import Flask, json,request
from flask.helpers import flash
import pandas as pd

def cargar_datos(ruta):
    resultado=pd.read_json(ruta)
    print(ruta)
    return resultado

app=Flask(__name__,template_folder='Template')

@app.route('/', methods=['GET'])
def welcome():
    return 'Hola mundo'

@app.route('/pokemon/',methods=['GET'])
def obtener_pokemons():
    pokemon=cargar_datos(ruta)
    return json.loads(pokemon[['name','id']].to_json(orient='index'))

@app.route('/pokemon/<string:name>',methods=['GET'])
def obtener_pokemon(name):
    pokemon=cargar_datos(ruta)
    res=pokemon.loc[(pokemon['name']==name)]
    return json.loads(res.to_json(orient='index'))

if __name__=="__main__":
    ruta='pokedex.json'
    app.run(port=9000,debug=True)