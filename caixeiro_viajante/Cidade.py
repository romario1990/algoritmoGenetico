#!/usr/bin/env python

import math
import random

class Cidade:
    def __init__(self, nome=None, eixoX=None, eixoY=None):
        self.nome = nome
        self.eixoX = None
        self.eixoY = None

        if eixoX is not None:
            self.eixoX = eixoX
        else:
            self.eixoX = int(random.random() * 200)
        if eixoY is not None:
            self.eixoY = eixoY
        else:
            self.eixoY = int(random.random() * 200)

    def getNome(self):
        return self.nome

    def getX(self):
        return self.eixoX

    def getY(self):
        return self.eixoY

    def distanceTo(self, cidade):
        distanciaX = abs(self.getX() - cidade.getX())
        distanciaY = abs(self.getY() - cidade.getY())
        distancia = math.sqrt((distanciaX * distanciaX) + (distanciaY * distanciaY))
        return distancia

    def __repr__(self):
        return str(self.getX()) + ", " + str(self.getY())