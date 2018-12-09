#!/usr/bin/env python

from Rota import Rota

class Populacao:
    def __init__(self, gerenciadorRota, tamanhoPopulacao, inicializar):
        self.rotas = []
        for i in range(0, tamanhoPopulacao):
            self.rotas.append(None)

        if inicializar:
            for i in range(0, tamanhoPopulacao):
                novaRota = Rota(gerenciadorRota)
                novaRota.gerarIndividup()
                self.saveRota(i, novaRota)

    def __setitem__(self, key, value):
        self.rotas[key] = value

    def __getitem__(self, index):
        return self.rotas[index]

    def saveRota(self, index, rota):
        self.rotas[index] = rota

    def getRota(self, index):
        return self.rotas[index]

    def getMaisApto(self):
        maisApto = self.rotas[0]
        for i in range(0, self.tamanhoPopulacao()):
            if maisApto.getFitness() <= self.getRota(i).getFitness():
                maisApto = self.getRota(i)
        return maisApto

    def tamanhoPopulacao(self):
        return len(self.rotas)
