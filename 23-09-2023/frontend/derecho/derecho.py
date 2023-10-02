import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
#importa las librerías necesarias

derecho=dbc.Container([#crea la variable derecho y en ella un Container
    html.Div([#crea una división
        html.Br(),html.Br(),html.Br(),html.Br(),#añade 4 espacios
        html.Label('Ingrese Datos Adicionales', style={'color':'#17242d'}), 
        #Se crea una etiqueta (texto) y define el color
        html.Br(),#añade un espacio
        html.Label('Límite Líquido: ', style={'color':'#17242d'}),
        #Se crea una etiqueta (texto) y define el color
        dcc.Input(id='limLiquido', value="40", type='number', min=15, max=60),
        #se crea un Input con identificador, valor por defecto, tipo numero, rango
        html.Br(),#añade un espacio
        html.Label('Índice de Plasticidad: ', style={'color':'#17242d'}),
        #Se crea una etiqueta (texto) y define el color
        dcc.Input(id='indicePlasticidad', value="10", type='number', min=7, max=17), 
        #se crea un Input con identificador, valor por defecto, tipo numero y rango
        html.Br(),#añade un espacio
    ])
])