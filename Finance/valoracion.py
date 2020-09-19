# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 18:46:10 2020

@author: Daniel
"""

# --------------------
def descuento(flujo, tasa, time):
    """
    """
    vp = flujo/(1+tasa)**time
    return vp


# --------------------
def precio_perpetuidad_teorico(tasa_y, tasa_c):
    """
    Calculo del precio teorico de un perpetuidad.
    Parametros:
        tasa_y = tasa yield
        tasa_c = tasa cupon
    Return:
        vp = precio de una perpetuidad
    """
    vp = (tasa_c/tasa_y)
    return vp


# --------------------
def precio_anualidad_teorico(tasa_c, tasa_y, n):
    """
    Calculo del precio teorico de un anualidad.
    Parametros:
        tasa_y = tasa yield
        tasa_c = tasa cupon
        n = numero de veces que se repite una anualidad
    Return
        vp = precio de una anualidad
    """
    vp = (tasa_c/tasa_y) * (1 - 1/(1+tasa_y)**n)
    return vp


# --------------------
def precio_bono_teorico(tasa_y, tasa_c, n, m):
    """
    Calculo del precio teorico de un bono
    Parametros:
        tasa_y = tasa yield
        tasa_c = tasa cupon
        n = periodos de tiempo al vencimiento del bono
        m = periodicidad de pago de cupo durante cada "n"
    Return:
        vp = precio del bono    
    """
    vp = (tasa_c/tasa_y) * (1 - 1/(1+tasa_y/m)**(n*m)) + 1/(1+tasa_y/m)**(n*m)
    return vp





a = precio_bono_teorico(0.05, 0.05, 2, 10)
b = precio_bono_teorico(0.06, 0.05, 2, 10)
c = precio_bono_teorico(0.04, 0.05, 2, 10)
