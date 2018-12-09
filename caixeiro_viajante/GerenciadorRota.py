#!/usr/bin/env python

class GerenciadorRota:
    cidadesDestino = []

    def addCidade(self, cidade):
        self.cidadesDestino.append(cidade)

    def getCidade(self, index):
        return self.cidadesDestino[index]

    def numeroDeCidades(self):
        return len(self.cidadesDestino)