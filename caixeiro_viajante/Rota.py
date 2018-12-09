#!/usr/bin/env python

import random

class Rota:
    def __init__(self, gerenciadorRota, rota=None):
        self.gerenciadorRota = gerenciadorRota
        self.rota = []
        self.fitness = 0.0
        self.distancia = 0
        if rota is not None:
            self.rota = rota
        else:
            for i in range(0, self.gerenciadorRota.numeroDeCidades()):
                self.rota.append(None)

    def __len__(self):
        return len(self.rota)

    def __getitem__(self, index):
        return self.rota[index]

    def __setitem__(self, key, value):
        self.rota[key] = value

    def __repr__(self):
        cordaGeneString = "|"
        for i in range(0, self.tamanhoRota()):
            cordaGeneString += str(self.getCidade(i)) + "|"
        return cordaGeneString

    def gerarIndividup(self):
        for indexCidade in range(0, self.gerenciadorRota.numeroDeCidades()):
            self.setCidade(indexCidade, self.gerenciadorRota.getCidade(indexCidade))
        random.shuffle(self.rota)

    def getCidade(self, posicaoRota):
        return self.rota[posicaoRota]

    def setCidade(self, posicaoRota, cidade):
        self.rota[posicaoRota] = cidade
        self.fitness = 0.0
        self.distancia = 0

    def getFitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.getDistancia())
        return self.fitness

    def getDistancia(self):
        if self.distancia == 0:
            distanciaRota = 0
            for indexCidade in range(0, self.tamanhoRota()):
                daCidade = self.getCidade(indexCidade)
                destinoDaCidade = None
                if indexCidade + 1 < self.tamanhoRota():
                    destinoDaCidade = self.getCidade(indexCidade + 1)
                else:
                    destinoDaCidade = self.getCidade(0)
                distanciaRota += daCidade.distanceTo(destinoDaCidade)
            self.distancia = distanciaRota
        return self.distancia

    def tamanhoRota(self):
        return len(self.rota)

    def contemCidade(self, cidade):
        return cidade in self.rota