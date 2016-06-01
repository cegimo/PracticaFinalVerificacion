# -*- coding: utf-8 -*-
import redis


class Game:
    def __init__(self, mock=None):
        # conexion con la base de datos Redis
        if mock is None:
            pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
            self.redis = redis.Redis(connection_pool=pool)
        else:
            self.redis = mock

    # Crea el jugador en la BD de redis y le asigna una puntuacion por por defecto es 0
    def createPLayer(self, name, score):
        player = self.redis.get(name)
        if player is not None:
            print "El jugador ya existe en la base de datos"
            # raise Exception
        else:
            self.redis.set(name, score)
            return True

    def seeScore(self, name):
        if name is None:
            print "No existe el usuario"
            # raise Exception
            return False
        else:
            puntosjugador = self.redis.get(name)
            print
            print "El jugador "
            print name
            print " tiene "
            print puntosjugador
            print " puntos"
            return True

    def quizGameWord(self):
        print "Adivinanza: " \
              "En rincones y entre ramas " \
              "mis redes voy construyendo," \
              "para que moscas incautas," \
              "en ellas vayan cayendo." \
              "" \
              "En alto vive, en alto mora," \
              "en alto teje, la tejedora." \
              "" \
              "Teje con manya" \
              "caza con sania."
        print "Escriba su respuesta:"
        # Se obtiene por teclado
        respuesta = raw_input()
        # La pasamos a minusculas
        respuesta = respuesta.lower()
        return respuesta

    def solutionQuizGameWord(self, respuesta):
        respuestaCorrecta1 = self.redis.get("quizGameWord")
        respuestaCorrecta2 = self.redis.get("quizGameWord1")

        if respuesta is respuestaCorrecta1 or respuestaCorrecta2:
            print "Respuesta correcta"
            return True
        else:
            print "Respuesta fallida"
            raise Exception

    def quizGameNumber(self):
        print "Cuanto es 2 + 2?:"
        # Se obtiene por teclado
        respuesta = input()

        return respuesta

    def solutionQuizNumber(self, respuesta):
        if respuesta is 4:
            print "Respuesta correcta"
            return True
        else:
            print "Respuesta incorrecta"
            # raise Exception

    def quizGameColor(self):
        print "De que color es el caballo blanco de Santiago?, escriba la respuesta:"

        # Se obtiene por teclado
        respuesta = raw_input()
        respuesta = respuesta.lower()

        return respuesta

    def solutionQuizGameColor(self, respuesta):
        if respuesta == "blanco":
            print "Respuesta correcta"
            return True
        else:
            print "Respuesta incorrecta"
            # raise Exception


if __name__ == "__main__":
    game = Game()

    # Borramos todo el contenido de la base de datos Redis
    game.redis.flushall()

    # Precargamos las respuestas del juego
    game.redis.set("quizGameWord", "la araña")
    game.redis.set("quizGameWord1", "araña")
    game.redis.set("quizGameNumber", 4)
    game.redis.set("Adivinanza3", "blanco")

    # Creamos un jugador y le asignamos una puntuacion, por defecto es 0
    jugador = game.createPLayer("nombre", 0)

    scoreJugador = game.seeScore("nombre")

    quizGameWord = game.quizGameWord()

    solutionQuizGameWord = game.solutionQuizGameWord(quizGameWord)

    quizGameNumber = game.quizGameNumber()

    solutionQuizGameNumber = game.solutionQuizNumber(quizGameNumber)

    quizGameColor = game.quizGameColor()

    solutionQuizGameColor = game.solutionQuizGameColor(quizGameColor)

    print "Juego terminado!"
