#!/usr/bin/env python

from Populacao import Populacao
from Rota import Rota
import random

class AlgoritmoGenetico:
    def __init__(self, gerenciadorRota):
        self.gerenciadorRota = gerenciadorRota
        self.taxaMutacao = 0.015
        self.tamanhoTorneio = 5
        self.populacaoElite = True

    def evolvePopulation(self, pop):
        novaPopulacao = Populacao(self.gerenciadorRota, pop.tamanhoPopulacao(), False)
        populacaoEliteFora = 0
        if self.populacaoElite:
            novaPopulacao.saveRota(0, pop.getMaisApto())
            populacaoEliteFora = 1

        for i in range(populacaoEliteFora, novaPopulacao.tamanhoPopulacao()):
            parente1 = self.selecaoTorneio(pop)
            parente2 = self.selecaoTorneio(pop)
            filho = self.crossover(parente1, parente2)
            novaPopulacao.saveRota(i, filho)

        for i in range(populacaoEliteFora, novaPopulacao.tamanhoPopulacao()):
            self.mutate(novaPopulacao.getRota(i))

        return novaPopulacao

    def crossover(self, parente1, parente2):
        filho = Rota(self.gerenciadorRota)

        iniciarPos = int(random.random() * parente1.tamanhoRota())
        finalPos = int(random.random() * parente1.tamanhoRota())

        for i in range(0, filho.tamanhoRota()):
            if iniciarPos < finalPos and i > iniciarPos and i < finalPos:
                filho.setCidade(i, parente1.getCidade(i))
            elif iniciarPos > finalPos:
                if not (i < iniciarPos and i > finalPos):
                    filho.setCidade(i, parente1.getCidade(i))

        for i in range(0, parente2.tamanhoRota()):
            if not filho.contemCidade(parente2.getCidade(i)):
                for ii in range(0, filho.tamanhoRota()):
                    if filho.getCidade(ii) == None:
                        filho.setCidade(ii, parente2.getCidade(i))
                        break

        return filho

    def mutate(self, rota):
        for rotaPos1 in range(0, rota.tamanhoRota()):
            if random.random() < self.taxaMutacao:
                rotaPos2 = int(rota.tamanhoRota() * random.random())

                cidade1 = rota.getCidade(rotaPos1)
                cidade2 = rota.getCidade(rotaPos2)

                rota.setCidade(rotaPos2, cidade1)
                rota.setCidade(rotaPos1, cidade2)

    def selecaoTorneio(self, pop):
        torneio = Populacao(self.gerenciadorRota, self.tamanhoTorneio, False)
        for i in range(0, self.tamanhoTorneio):
            randomId = int(random.random() * pop.tamanhoPopulacao())
            torneio.saveRota(i, pop.getRota(randomId))
        maisApto = torneio.getMaisApto()
        return maisApto