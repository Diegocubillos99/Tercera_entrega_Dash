import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
#importa las librerías necesarias

centro=dbc.Container([#crea la variable derecho y en ella un Container
    html.H1('Datos del Proyecto', style={'color':'#17242d'}),#crea un titulo 1 y define el color del texto
    html.Hr(),#añade un espacio
    html.Div([#crea una división
        html.Label('Ingrese la granulometría', style={'color':'#17242d'}), 
        #Se crea una etiqueta (texto) y define el color
        html.Br(),#añade un espacio
        html.Label('Pasa Tamiz 1 1/2: ', style={'color':'#17242d'}),
        #Se crea una etiqueta (texto) y define el color
        dcc.Input(id='tamiz_1_1d2', value="100", type='number'), 
        #se crea un Input con identificador, valor por defecto y tipo numero
        html.Br(),#añade un espacio
        html.Label('Pasa Tamiz 1:     ', style={'color':'#17242d'}),
        #Se crea una etiqueta (texto) y define el color
        dcc.Input(id='tamiz_1', value="100", type='number'), 
        #se crea un Input con identificador, valor por defecto y tipo numero
        html.Br(),#añade un espacio
        html.Label('Pasa Tamiz 3/4:   ', style={'color':'#17242d'}),
        #Se crea una etiqueta (texto) y define el color
        dcc.Input(id='tamiz_3d4', value="100", type='number'), 
        #se crea un Input con identificador, valor por defecto y tipo numero
        html.Br(),#añade un espacio
        html.Label('Pasa Tamiz 3/8:   ', style={'color':'#17242d'}),
        #Se crea una etiqueta (texto) y define el color
        dcc.Input(id='tamiz_3d8', value="100", type='number'), 
        #se crea un Input con identificador, valor por defecto y tipo numero
        html.Br(),#añade un espacio
        html.Label('Pasa Tamiz No.4:  ', style={'color':'#17242d'}),
        #Se crea una etiqueta (texto) y define el color
        dcc.Input(id='tamiz_N4', value="100", type='number'), 
        #se crea un Input con identificador, valor por defecto y tipo numero
        html.Br(),#añade un espacio
        html.Label('Pasa Tamiz No.10:  ', style={'color':'#17242d'}),
        #Se crea una etiqueta (texto) y define el color
        dcc.Input(id='tamiz_N10', value="100", type='number'), 
        #se crea un Input con identificador, valor por defecto y tipo numero
        html.Br(),#añade un espacio
        html.Label('Pasa Tamiz No.20:  ', style={'color':'#17242d'}),
        #Se crea una etiqueta (texto) y define el color
        dcc.Input(id='tamiz_N20', value="100", type='number'), 
        #se crea un Input con identificador, valor por defecto y tipo numero
        html.Br(),#añade un espacio
        html.Label('Pasa Tamiz No.40:  ', style={'color':'#17242d'}),
        #Se crea una etiqueta (texto) y define el color
        dcc.Input(id='tamiz_N40', value="100", type='number'), 
        #se crea un Input con identificador, valor por defecto y tipo numero
        html.Br(),#añade un espacio
        html.Label('Pasa Tamiz No.60:  ', style={'color':'#17242d'}),
        #Se crea una etiqueta (texto) y define el color
        dcc.Input(id='tamiz_N60', value="100", type='number'), 
        #se crea un Input con identificador, valor por defecto y tipo numero
        html.Br(),#añade un espacio
        html.Label('Pasa Tamiz No.100:  ', style={'color':'#17242d'}),
        #Se crea una etiqueta (texto) y define el color
        dcc.Input(id='tamiz_N100', value="100", type='number'), 
        #se crea un Input con identificador, valor por defecto y tipo numero
        html.Br(),#añade un espacio
        html.Label('Pasa Tamiz No.200:  ', style={'color':'#17242d'}),
        #Se crea una etiqueta (texto) y define el color
        dcc.Input(id='tamiz_N200', value="100", type='number'), 
        #se crea un Input con identificador, valor por defecto y tipo numero
        html.Br(),#añade un espacio
        html.Label(id='resultado'), #se crea una etiqueta (texto) con identificador
    ])
])