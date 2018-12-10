#!/usr/bin/python3
# coding: utf-8

import functools
import tkinter as t
import matplotlib.pyplot as plt
from GerenciadorRota import GerenciadorRota
from Cidade import Cidade
from Populacao import Populacao
from AlgoritmoGenetico import AlgoritmoGenetico

root = t.Tk()
root.title("Grafo 2.0")
root.resizable(0, 0)

f = plt.figure(figsize=(10, 5))
a = f.add_subplot(111)
plt.axis('off')

gerenciadorRota = GerenciadorRota()
pop = None
ag = None
cidades = []
index = 0
tPopulacao = 100
tMutacao = 0.5
tCruzamento = 60
iteracoes = 50
mostrar = 5
tGeracoes = 10

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

class TelaPrincipal(t.Frame):
    def __init__(self, parent):
        t.Frame.__init__(self, parent)

        ### Widgets - Principal ###
        t.Label(self, text="MENU PRINCIPAL").pack()
        self._tela = "principal"

    def getTela(self):
        return self._tela


class InserirCidade(t.Frame):
    def __init__(self, parent):
        t.Frame.__init__(self, parent)
        self.eixoX = None
        self.eixoY = None

        ### Widgets - Principal ###
        t.Label(self, text="INSERIR CIDADE").pack()
        self._tela = "inserircidade"

        t.Label(self, text="Digite as coordenadas da cidade").pack()
        t.Label(self, text="Nome cidade").pack()
        self.cidade = t.Entry(self)
        self.cidade.bind("<Return>", self.salvarVertice)
        self.cidade.pack()

        t.Label(self, text="Valor do eixo X").pack()
        self.eixoX = t.Entry(self)
        self.eixoX.bind("<Return>", self.salvarVertice)
        self.eixoX.pack()

        t.Label(self, text="Valor do eixo Y").pack()
        self.eixoY = t.Entry(self)

        self.eixoY.bind("<Return>", self.salvarVertice)
        self.eixoY.pack()

        t.Button(self, text='Salvar', command=self.salvarVertice).pack()

    def getTela(self):
        return self._tela

    def salvarVertice(self):
        nome = self.cidade.get()
        x = int(self.eixoX.get())
        y = int(self.eixoY.get())

        podeInserirCidade = True

        for cid in cidades:
            if cid.getNome() == nome:
                print(" " + nome + ". Cidade já cadastrada")
                podeInserirCidade = False
                break

        if podeInserirCidade:
            global index
            print(index)
            cidades.append(Cidade(nome, x, y))
            gerenciadorRota.addCidade(cidades[index])
            index = index + 1


class RemoverCidade(t.Frame):
    def __init__(self, parent):
        t.Frame.__init__(self, parent)

        ### Widgets - Principal ###
        t.Label(self, text="REMOVER CIDADE").pack()
        self._tela = "removercidade"

        t.Label(self, text="Digite o nome da cidade").pack()
        self.cidade = t.Entry(self)
        self.cidade.bind("<Return>", self.salvarVertice)
        self.cidade.pack()

        t.Button(self, text='Salvar', command=self.salvarVertice).pack()

    def getTela(self):
        return self._tela

    def salvarVertice(self):
        nome = self.cidade.get()
        indice = 0
        global index
        for cid in cidades:
            if cid.getNome() == nome:
                print(" " + nome + ". Removendo cidade")
                cidades.remove(cid)
                gerenciadorRota.removerCidade(cid)
                index = index - 1



class CarregarInformacoes(t.Frame):
    def __init__(self, parent):
        t.Frame.__init__(self, parent)
        self.tamanhoPopulacao = None
        self.taxaMutacao = None
        self.taxaCruzamento = None
        self.iteracoes = None
        self.mostrar = None

        ### Widgets - Principal ###
        t.Label(self, text="Carregar informções").pack()
        self._tela = "carregarinformacoes"

        t.Label(self, text="Tamanho da população mínimo de 100 indivíduos").pack()
        self.tamanhoPopulacao = t.Entry(self)
        self.tamanhoPopulacao.bind("<Return>", self.salvarVertice)
        self.tamanhoPopulacao.pack()

        t.Label(self, text="Taxa Mutação faixa de 0.5% - 1%.").pack()
        self.taxaMutacao = t.Entry(self)
        self.taxaMutacao.bind("<Return>", self.salvarVertice)
        self.taxaMutacao.pack()

        t.Label(self, text="Taxa Cruzamento faixa de 60%-80%.").pack()
        self.taxaCruzamento = t.Entry(self)
        self.taxaCruzamento.bind("<Return>", self.salvarVertice)
        self.taxaCruzamento.pack()

        t.Label(self, text="Nº de gerações – mínimo de 10 gerações.").pack()
        self.nGeracoes = t.Entry(self)
        self.nGeracoes.bind("<Return>", self.salvarVertice)
        self.nGeracoes.pack()

        t.Label(self, text="Quantidade de iterações aconselhado no mínimo 100").pack()
        self.iteracoes = t.Entry(self)
        self.iteracoes.bind("<Return>", self.salvarVertice)
        self.iteracoes.pack()

        t.Label(self, text="Quantidade de iterações para Mostrar").pack()
        self.mostrar = t.Entry(self)
        self.mostrar.bind("<Return>", self.salvarVertice)
        self.mostrar.pack()

        t.Button(self, text='Salvar', command=self.salvarVertice).pack()

    def getTela(self):
        return self._tela

    def salvarVertice(self):
        global tPopulacao
        global tMutacao
        global tCruzamento
        global iteracoes
        global mostrar
        global tGeracoes

        tPopulacao = int(self.tamanhoPopulacao.get())
        tMutacao = float(self.taxaMutacao.get())
        tCruzamento = float(self.taxaCruzamento.get())
        tGeracoes = int(self.nGeracoes.get())
        iteracoes = int(self.iteracoes.get())
        mostrar = int(self.mostrar.get())


class ExecutarAlgoritmo(t.Frame):
    def __init__(self, parent):
        t.Frame.__init__(self, parent)

        ### Widgets - Principal ###
        t.Label(self, text="Executando").pack()
        self._tela = "executar"

        t.Button(self, text='Executar', command=self.salvarVertice).pack()

    def getTela(self):
        return self._tela

    def salvarVertice(self):
        global pop
        global tPopulacao
        global tMutacao
        global tCruzamento
        global iteracoes
        global mostrar
        global tGeracoes

        # Inicializa classe da população
        pop = Populacao(gerenciadorRota)

        # Insere tamanho da população
        pop.setTamanhoPopulacao(tPopulacao, True)

        print("Distância inicial: " + str(pop.getMaisApto().getDistancia()))
        print("Solução inicial: \n" + str(pop.getMaisApto()))


        # inicializa classe algoritmo genetico
        ag = AlgoritmoGenetico(gerenciadorRota)

        # Insere taxa mutação
        ag.setTaxaMutacao(tMutacao)

        ag.setNumeroGeracoes(tGeracoes)

        # Insere taxa de cruzamento
        ag.setTaxaCruzamento(tCruzamento)

        # Inicializa população
        pop = ag.evolucaoDaPopulacao(pop)

        # Mostrar plano inicial
        mostrarPlanoCartesiano(pop.getMaisApto(), "Plano inicial")

        contador = mostrar
        for i in range(0, iteracoes):
            if i == contador:
                mostrarPlanoCartesiano(pop.getMaisApto(), "Plano em processamento")
                contador = contador + mostrar
            pop = ag.evolucaoDaPopulacao(pop)

        mostrarPlanoCartesiano(pop.getMaisApto(), "Plano final")
        print("Finalizado")
        print("Distância Final: " + str(pop.getMaisApto().getDistancia()))
        print("solução:")
        print(pop.getMaisApto())

    
class Menu(t.Frame):
    def __init__(self, parent, *subtelas):
        t.Frame.__init__(self, parent)
        self.current_frame = self
        ### Widgets - Principal ###
        t.Label(self, text="MENU PRINCIPAL").pack()
        self._telaPrincipal = None
        self._telaInserirCidade = None
        self._telaRemoverCidade = None
        self._telaCarregarInformacoes = None
        self._telaExecutarAlgoritmo = None

        for subtela in subtelas:
            ### Widgets - Menu principal botões###
            t.Button(subtela, text='Voltar', command=functools.partial(self.muda_tela, self)).pack()
            if subtela.getTela() == "principal":
                self._telaPrincipal = subtela
            elif subtela.getTela() == "inserircidade":
                self._telaInserirCidade = subtela
            elif subtela.getTela() == "removercidade":
                self._telaRemoverCidade = subtela
            elif subtela.getTela() == "carregarinformacoes":
                self._telaCarregarInformacoes = subtela
            elif subtela.getTela() == "executar":
                self._telaExecutarAlgoritmo = subtela

        t.Button(self, text="Inserir Cidade", command=functools.partial(self.muda_tela, self._telaInserirCidade)).pack()
        t.Button(self, text="Remover Cidade", command=functools.partial(self.muda_tela, self._telaRemoverCidade)).pack()
        t.Button(self, text="Carregar Informações", command=functools.partial(self.muda_tela, self._telaCarregarInformacoes)).pack()
        t.Button(self, text="Executar", command=functools.partial(self.muda_tela, self._telaExecutarAlgoritmo)).pack()

    def muda_tela(self, qual):
        self.current_frame.pack_forget()
        qual.pack()
        self.current_frame = qual

if __name__ == '__main__':

    telaPrincipal = TelaPrincipal(root)
    inserirCidade = InserirCidade(root)
    removerCidade = RemoverCidade(root)
    carregarInformacoes = CarregarInformacoes(root)
    executarAlgoritmo = ExecutarAlgoritmo(root)

    menuPrincipal = Menu(root, telaPrincipal, inserirCidade, removerCidade, carregarInformacoes,
                         executarAlgoritmo)

    root.geometry("1024x700+0+0")
    menuPrincipal.pack()

    root.mainloop()