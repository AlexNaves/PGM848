import numpy as np


def media(vetor):
    it = 0
    for el in vetor:
        it = it + el
    media = it / len(vetor)
    return media


def variancia(vetor):
    var = 0
    for gl in vetor:
        var = var + ((gl - (np.mean(vetor))) ** 2) / (len(vetor) - 1)
    return var

