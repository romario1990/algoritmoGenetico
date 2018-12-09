#!/usr/bin/env python

from GerenciadorRota import GerenciadorRota
from Cidade import Cidade
from Populacao import Populacao
from AlgoritmoGenetico import AlgoritmoGenetico

if __name__ == '__main__':

    gerenciadorRota = GerenciadorRota()

    cidade = Cidade(60, 200)
    gerenciadorRota.addCidade(cidade)
    cidade2 = Cidade(180, 200)
    gerenciadorRota.addCidade(cidade2)
    cidade3 = Cidade(80, 180)
    gerenciadorRota.addCidade(cidade3)
    cidade4 = Cidade(140, 180)
    gerenciadorRota.addCidade(cidade4)
    cidade5 = Cidade(20, 160)
    gerenciadorRota.addCidade(cidade5)
    cidade6 = Cidade(100, 160)
    gerenciadorRota.addCidade(cidade6)
    cidade7 = Cidade(200, 160)
    gerenciadorRota.addCidade(cidade7)
    cidade8 = Cidade(140, 140)
    gerenciadorRota.addCidade(cidade8)
    cidade9 = Cidade(40, 120)
    gerenciadorRota.addCidade(cidade9)
    cidade10 = Cidade(100, 120)
    gerenciadorRota.addCidade(cidade10)
    cidade11 = Cidade(180, 100)
    gerenciadorRota.addCidade(cidade11)
    cidade12 = Cidade(60, 80)
    gerenciadorRota.addCidade(cidade12)
    cidade13 = Cidade(120, 80)
    gerenciadorRota.addCidade(cidade13)
    cidade14 = Cidade(180, 60)
    gerenciadorRota.addCidade(cidade14)
    cidade15 = Cidade(20, 40)
    gerenciadorRota.addCidade(cidade15)
    cidade16 = Cidade(100, 40)
    gerenciadorRota.addCidade(cidade16)
    cidade17 = Cidade(200, 40)
    gerenciadorRota.addCidade(cidade17)
    cidade18 = Cidade(20, 20)
    gerenciadorRota.addCidade(cidade18)
    cidade19 = Cidade(60, 20)
    gerenciadorRota.addCidade(cidade19)
    cidade20 = Cidade(160, 20)
    gerenciadorRota.addCidade(cidade20)

    # Inicializa classe da população
    pop = Populacao(gerenciadorRota)
    # Insere tamanho da população
    pop.setTamanhoPopulacao(50, True)



    print("Distância inicial: " + str(pop.getMaisApto().getDistancia()))


    ag = AlgoritmoGenetico(gerenciadorRota)
    # Insere taxa mutação
    ag.setTaxaMutacao(0.8)
    # Insere taxa de cruzamento
    #ag.setTaxaCruzamento(60)

    pop = ag.evolucaoDaPopulacao(pop)

    for i in range(0, 200):
        # print(pop.getMaisApto())
        pop = ag.evolucaoDaPopulacao(pop)


    print("Finalizado")
    print("Distância Final: " + str(pop.getMaisApto().getDistancia()))
    print("solução:")
    print(pop.getMaisApto())
