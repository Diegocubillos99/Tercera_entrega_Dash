import dash #importa dash
import dash_bootstrap_components as dbc #importa los componentes bootstrap de das como dbc
from dash.dependencies import Input, Output #de dash.dependencies se importa input y output
import math #se importa math

#Se importa frontend
from frontend.main import layout
from backend.backend import pesoTotal

app=dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
#crea la variable app y agrega __name__ y los estilos con bootstrap

app.layout = layout #se asigna el layout en la variable layout de app

@app.callback(#llama de app
    Output('resultado', 'children'), #llama en output la salidaCirculo como children
    Input('tamiz_1_1d2', 'value',), #llama en input el valor del usuario como value
    Input('tamiz_1', 'value',), #llama en input el valor del usuario como value
    Input('tamiz_3d4', 'value',), #llama en input el valor del usuario como value
    Input('tamiz_3d8', 'value',), #llama en input el valor del usuario como value
    Input('tamiz_N4', 'value',), #llama en input el valor del usuario como value
    Input('tamiz_N10', 'value',), #llama en input el valor del usuario como value
    Input('tamiz_N20', 'value',), #llama en input el valor del usuario como value
    Input('tamiz_N40', 'value',), #llama en input el valor del usuario como value
    Input('tamiz_N60', 'value',), #llama en input el valor del usuario como value
    Input('tamiz_N100', 'value',), #llama en input el valor del usuario como value
    Input('tamiz_N200', 'value',), #llama en input el valor del usuario como value
    Input('limLiquido', 'value',), #llama en input el valor del usuario como value
    Input('indicePlasticidad', 'value',), #llama en input el valor del usuario como value
)



def resultado(tamiz_1_1d2, tamiz_1, tamiz_3d4, tamiz_3d8, tamiz_N4, tamiz_N10, tamiz_N20,
               tamiz_N40, tamiz_N60, tamiz_N100, tamiz_N200):#crea la función areaCirculo con dato de entrada entradaCirculo
    resultado = pesoTotal(tamiz_1_1d2, tamiz_1, tamiz_3d4, tamiz_3d8, tamiz_N4, tamiz_N10, tamiz_N20,
               tamiz_N40, tamiz_N60, tamiz_N100, tamiz_N200) #Hace la operación y la guarda en la variable areaCalculadaCirculo
    return 'El resultado es: ' + str(resultado) #retorna la respuesta con el resultado

if __name__ == '__main__': #si __name__ y __main__ son iguales
    app.run_server(debug=True) #Ejecuta la app