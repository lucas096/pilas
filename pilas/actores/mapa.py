# -*- encoding: utf-8 -*-
# Pilas engine - A video game framework.
#
# Copyright 2010 - Hugo Ruscitti
# License: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# Website - http://www.pilas-engine.com.ar

import pilas
from pilas.actores import Actor


class Mapa(Actor):
    """Representa mapas creados a partir de imagenes mas pequeñas.

    Este actor te permite crear escenarios tipo ``tiles``, una técnica
    de contrucción de escenarios muy popular en los videojuegos.
    
    Puedes crear un actor a partir de una grilla, e indicando cada
    uno los bloques o simplemente usando un programa externo llamado
    **tiled** (ver http://www.mapeditor.org).

    Por ejemplo, para crear un mapa desde un archivo del programa
    **tiled** puedes escribir:

        >>> mapa = pilas.actores.Mapa('untitled2.tmx')
    """

    def __init__(self, grilla_o_mapa, x=0, y=0, restitucion=0.56):
        Actor.__init__(self, 'invisible.png', x, y)
        self.restitucion = restitucion
        self.figuras = []
        self.bloques = []

        if isinstance(grilla_o_mapa, str):
            self._cargar_mapa(grilla_o_mapa)
        else:
            self.grilla = grilla_o_mapa
            self._ancho_cuadro = grilla_o_mapa.cuadro_ancho
            self._alto_cuadro = grilla_o_mapa.cuadro_alto

    def _cargar_mapa(self, archivo):
        "Carga el escenario desde un archivo .tmz (del programa tiled)."

        # Carga los nodos principales.
        nodo = pilas.utils.xmlreader.makeRootNode(archivo)
        nodo_mapa = nodo.getChild('map')
        nodo_tileset = nodo_mapa.getChild('tileset')

        # Cantidad de bloques en el mapa.
        self.columnas = int(nodo_mapa.getAttributeValue('width'))
        self.filas = int(nodo_mapa.getAttributeValue('height'))

        # Atributos de la imagen asociada al mapa.
        self._ruta = nodo_tileset.getChild('image').getAttributeValue('source')
        self._ancho_imagen = int(nodo_tileset.getChild('image').getAttributeValue('width'))
        self._alto_imagen = int(nodo_tileset.getChild('image').getAttributeValue('height'))
        self._ancho_cuadro = int(nodo_tileset.getAttributeValue('tilewidth'))
        self._alto_cuadro = int(nodo_tileset.getAttributeValue('tileheight'))

        # Carga la grilla de imagenes desde el mapa.
        self.grilla = pilas.imagenes.cargar_grilla(self._ruta, 
                self._ancho_imagen / self._ancho_cuadro, 
                self._alto_imagen / self._alto_cuadro)

        # Carga las capas del mapa.
        layers = nodo.getChild('map').getChildren('layer')

        if len(layers) == 0:
            raise Exception("Debe tener al menos una capa (layer).")

        # La capa 0 (inferior) define los bloques no-solidos.
        self._crear_bloques(layers[0], solidos=False)

        # El resto de las capas definen bloques solidos
        for layer in layers[1:]:
            self._crear_bloques(layer, solidos=True)

    def _crear_bloques(self, capa, solidos):
        "Genera actores que representan los bloques del escenario."
        datos = capa.getChild('data').getData()

        # Convierte todo el mapa en una matriz de numeros.
        bloques = [[int(x) for x in x.split(',') if x] for x in datos.split()]

        for (y, fila) in enumerate(bloques[::-1]):
            for (x, bloque) in enumerate(fila):
                if bloque:
                    self.pintar_bloque(y, x, bloque -1, solidos)

    def pintar_bloque(self, fila, columna, indice, es_bloque_solido=False):
        nuevo_bloque = pilas.actores.Actor('invisible.png')
        self.grilla.definir_cuadro(indice)
        self.grilla.asignar(nuevo_bloque)
        nuevo_bloque.izquierda = columna * self._ancho_cuadro - 320
        nuevo_bloque.arriba = fila * self._alto_cuadro - (240 - self._alto_cuadro)
        self.bloques.append(nuevo_bloque)

        if es_bloque_solido:
            figura = pilas.fisica.Rectangulo(nuevo_bloque.izquierda + self._ancho_cuadro / 2, 
                    nuevo_bloque.arriba - self._alto_cuadro / 2,
                    self._ancho_cuadro, self._alto_cuadro, dinamica=False, 
                    restitucion=self.restitucion)
            self.figuras.append(figura)

