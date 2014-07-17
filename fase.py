# -*- coding: utf-8 -*-

from __future__ import unicode_literals


class Fase():
    def __init__(self):
        self._obstaculos = []

    def adicionar_obstaculo(self, *obstaculos):
        self._obstaculos.extend(obstaculos)