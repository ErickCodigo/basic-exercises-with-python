"""Convertir una frase larga en su acrónimo"""


def split(s):
    xs = s.split(" ", len(s) - 1)
    acronym = ""
    for chunk in xs:
        acronym += chunk[0].upper() + "."
    return acronym


"""Invertir cadena"""


def revert(s):
    return s[::-1]


"""Escriba una función para determinar si una lista es una sublista de otra lista."""


def is_includes(xs, x):
    return x in xs
