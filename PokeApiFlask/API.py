from os import name
import re
from flask import Flask, json,request
from flask.helpers import flash
from numpy import array
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

@app.route('/pokemon/ingresar',methods=['GET','POST'])
def ingresar_pokemon():
    pokemon=cargar_datos(ruta)
    n=pokemon.shape[0]
    identidad=int(request.args.get('Id'))
    nombre=request.args.get('Pokemon_nombre')
    tipo=array(request.args.get('Types').split(','))
    pokemon.loc[n]=[identidad,nombre,tipo]
    pokemon.to_json(r'pokedex.json')
    return 'Exito'

if __name__=="__main__":
    ruta='pokedex.json'
    app.run(port=9000,debug=True)