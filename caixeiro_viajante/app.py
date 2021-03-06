#!/usr/bin/env python

from GerenciadorRota import GerenciadorRota
from Cidade import Cidade
from Populacao import Populacao
from AlgoritmoGenetico import AlgoritmoGenetico
import matplotlib.pyplot as plt

def mostrarPlanoCartesiano(distancia, nome):

    x = []
    y = []

    for posicao in distancia:
        x.append(posicao.getX())
        y.append(posicao.getY())

    x.append(x[0])
    y.append(y[0])

    plt.figure()
    plt.plot(x, y)
    plt.plot(x, y, 'ks')
    plt.title(nome)
    plt.xlabel("X")
    plt.ylabel("Y")

    plt.show()


if __name__ == '__main__':

    gerenciadorRota = GerenciadorRota()

    cidade = Cidade("A", 60, 200)
    gerenciadorRota.addCidade(cidade)
    cidade2 = Cidade("B", 180, 200)
    gerenciadorRota.addCidade(cidade2)
    cidade3 = Cidade("C", 80, 180)
    gerenciadorRota.addCidade(cidade3)
    cidade4 = Cidade("D", 140, 180)
    gerenciadorRota.addCidade(cidade4)
    cidade5 = Cidade("E", 20, 160)
    gerenciadorRota.addCidade(cidade5)
    cidade6 = Cidade("F", 100, 160)
    gerenciadorRota.addCidade(cidade6)
    cidade7 = Cidade("G", 200, 160)
    gerenciadorRota.addCidade(cidade7)
    cidade8 = Cidade("H", 140, 140)
    gerenciadorRota.addCidade(cidade8)
    cidade9 = Cidade("I", 40, 120)
    gerenciadorRota.addCidade(cidade9)
    cidade10 = Cidade("J", 100, 120)
    gerenciadorRota.addCidade(cidade10)
    cidade11 = Cidade("K", 180, 100)
    gerenciadorRota.addCidade(cidade11)
    cidade12 = Cidade("L", 60, 80)
    gerenciadorRota.addCidade(cidade12)
    cidade13 = Cidade("M", 120, 80)
    gerenciadorRota.addCidade(cidade13)
    cidade14 = Cidade("N", 180, 60)
    gerenciadorRota.addCidade(cidade14)
    cidade15 = Cidade("O", 20, 40)
    gerenciadorRota.addCidade(cidade15)
    cidade16 = Cidade("P", 100, 40)
    gerenciadorRota.addCidade(cidade16)
    cidade17 = Cidade("Q", 200, 40)
    gerenciadorRota.addCidade(cidade17)
    cidade18 = Cidade("R", 20, 20)
    gerenciadorRota.addCidade(cidade18)
    cidade19 = Cidade("S", 60, 20)
    gerenciadorRota.addCidade(cidade19)
    cidade20 = Cidade("T", 160, 20)
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
    ag.setTaxaCruzamento(60)


    pop = ag.evolucaoDaPopulacao(pop)

    mostrarPlanoCartesiano(pop.getMaisApto(), "Plano inicial")

    mostrar = 5
    for i in range(0, 50):
        if i == mostrar:
            mostrarPlanoCartesiano(pop.getMaisApto(), "Plano inicial")
            mostrar = mostrar + 10
        pop = ag.evolucaoDaPopulacao(pop)

    mostrarPlanoCartesiano(pop.getMaisApto(), "Plano Final")
    print("Finalizado")
    print("Distância Final: " + str(pop.getMaisApto().getDistancia()))
    print("solução:")
    print(pop.getMaisApto())
