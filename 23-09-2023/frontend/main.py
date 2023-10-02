import dash #importa dash
import dash_bootstrap_components as dbc #importa los componentes bootstrap de dash como dbc
from dash import html #De dash importa html

#importamos el frontend

from .navegador.navegador import navegador #importa container de navegador
from .derecho.derecho import derecho #importa container de derecho
from .centro.centro import centro #importa container de centro
from .izquierdo.izquierdo import izquierdo #importa container de izquierdo
from .inferior.inferior import inferior #importa container de inferior

imagen_fondo = 'url("https://geotecniaymecanicasuelosabc.com/wp-content/uploads/2021/05/TIPOS-DE-SUELOS.jpg")'
#crea variable con el url de la imagen de fondo

layout=dbc.Container([ #en la variable layout, crea container de toda la página web
    dbc.Row([ #crea una fila
        dbc.Col(navegador, md=12, style={'background-color': 'gray'}), 
        #crea columna con navegador espacio de 12 y color de fondo gris
        dbc.Col(izquierdo, md=1, style={'background-color': '#45ad7e'}),
        #crea columna con izquierdo espacio de 1 y color de fondo #45ad7e
        dbc.Col(centro, md=5, style={'background-image': imagen_fondo,  
        #crea columna con centro espacio de 5 y la imagen de fondo
                    'background-size': 'cover', # Ajusta el tamaño de la imagen
                    'background-repeat': 'no-repeat'}), # Evitar la repetición de la imagen
        dbc.Col(derecho, md=6, style={'background-image': imagen_fondo,  
        #crea columna con derecho espacio de 6 y la imagen de fondo
                    'background-size': 'cover', # Ajusta el tamaño de la imagen
                    'background-repeat': 'no-repeat'}), # Evitar la repetición de la imagen
        dbc.Col(inferior, md=12, style={'background-color': 'gray'}),
        #crea columna con inferior espacio de 12 y color de fondo gris
    ])
])