# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 22:39:37 2020

@author: Daniel
"""


# --------------------
def tasa_efe(tasa_1, n_1, n_2):
    """ Convierte entre tasas efectivas
    
    Parameters
    ----------
    tasa_1 : float
        tasa efectiva original.
    n_1 : float
        periodicidad de la tasa efectiva original (tasa_1).
    n_2 : float
        tasa efectiva con periodicidad "n_2".

    Returns
    -------
    tasa_2 : float
        tasa efectiva con periodicidad "n_2".

    """
    tasa_2 = (1 + tasa_1)**(n_1 / n_2) - 1 
    return tasa_2


# --------------------
def tasa_efe_nom(tasa_1, n_1, n_2):
    """ convierte tasa efectiva a nominal
    
    Parameters
    ----------
    tasa_1 : float
        tasa efectiva original.
    n_1 : float
        periodicidad de la tasa efectiva original (tasa_1).
    n_2 : float
        periodicidad de la nueva tasa nominal.

    Returns
    -------
    tasa_2 : TYPE
        DESCRIPTION.

    """
    tasa_2 = tasa_efe(tasa_1, n_1, n_2) * n_2
    return tasa_2


# --------------------
# convierte tasa nominal a efectiva
def tasa_nom_efe(tasa_1, n_1, n_2):
    """ convierte tasa nominal a efectiva
    
    Parameters
    ----------
    tasa_1 : float
        tasa nominal original.
    n_1 : float
        periodicidad de la tasa nominal original (tasa_1).
    n_2 : float
        periodicidad de la nueva tasa efectiva.

    Returns
    -------
    tasa_2 : TYPE
        DESCRIPTION.

    """
    tasa_1 = tasa_1 / n_1
    tasa_2 = tasa_efe(tasa_1, n_1, n_2)
    return tasa_2


# --------------------
# convierte entre tasas nominales
def tasa_nom(tasa_1, n_1, n_2):
    """
    Parametros:
        tasa_1 = tasa nominal original
        n_1 = periodicidad de la tasa nominal original (tasa_1)
        n_2 = periodicidad de la nueva tasa nominal
    Return:
        tasa_2 = tasa nominal con periodicidad "n_2"
    """
    tasa_1 = tasa_nom_efe(tasa_1, n_1, n_2)
    tasa_2 = tasa_efe_nom(tasa_1, n_2, n_2)    
    return tasa_2


# --------------------
# convierte tasa efectiva a continua
def tasa_efe_con(tasa_1, n_1 = 1, n_2 = 1):
    """
    Parametros:
        tasa_1 = tasa efectiva original
        n_1 = periodicidad de la tasa efectiva original (tasa_1)
        n_2 = periodicidad de la nueva tasa continua
    Return:
        tasa_2 = tasa continua con periodicidad "n_2"
    """
    from math import log 
    tasa_2 = log(1 + tasa_1) * (n_1 / n_2)    
    return tasa_2


# --------------------
# convierte tasa continua a efectiva
def tasa_con_efe(tasa_1, n_1 = 1, n_2 = 1):
    """
    Parametros:
        tasa_1 = tasa continua original
        n_1 = periodicidad de la tasa continua original (tasa_1)
        n_2 = periodicidad de la nueva tasa efectiva
    Return:
        tasa_2 = tasa efectiva con periodicidad "n_2"
    """
    from math import exp
    tasa_2 = exp(tasa_1 * n_1 / n_2) - 1
    return tasa_2


# --------------------
# convierte tasa nominal a continua
def tasa_nom_con(tasa_1, n_1, n_2):
    """
    Parametros:
        tasa_1 = tasa nominal original
        n_1 = periodicidad de la tasa nominal original (tasa_1)
        n_2 = periodicidad de la nueva tasa continua
    Return:
        tasa_2 = tasa continua con periodicidad "n_2"
    """
    tasa_1 = tasa_nom_efe(tasa_1, n_1, n_2)
    tasa_2 = tasa_efe_con(tasa_1)
    return tasa_2


# --------------------
# convierte tasa continua a nominal
def tasa_con_nom(tasa_1, n_1, n_2):
    """
    Parametros:
        tasa_1 = tasa continua original
        n_1 = periodicidad de la tasa continua original (tasa_1)
        n_2 = periodicidad de la nueva tasa nominal
    Return:
        tasa_2 = tasa nominal con periodicidad "n_2"
    """
    tasa_1 = tasa_con_efe(tasa_1)
    tasa_2 = tasa_efe_nom(tasa_1, n_1, n_2)
    return tasa_2


# --------------------


# tasa_efe_nom(0.05, 1, 2)
# tasa_nom_efe(0.04939015319191986, 2, 1)
# tasa_nom(4.939015319191986/100, 2, 4)*100
# tasa_efe_con(0.05, 1, 2)
# tasa_con_efe(0.02439508208471602, 2, 1)

# tasa_efe_con(0.05, 1, 4)
# tasa_nom_con(0.04939015319191986, 2, 4)
# tasa_con_nom(0.012197541042358082, 4, 2)
# tasa_con_efe(0.012197541042358082, 4, 1)
