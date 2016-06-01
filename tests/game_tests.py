# coding=utf-8
import unittest
from mock import Mock
from juego.game import Game

from mock import patch


class MyGameTestCase(unittest.TestCase):
    def setUp(self):
        pass

        # self.game = Game()
        # self.game.pool = redis.redis.ConnectionPool()
        # self.game.db = self.game.client[self.game.self.game.pool]

    # Test para crear un jugador
    def test_createPLayer(self):
        mock = Mock()
        mock.get = Mock(return_value=None)
        mock.set = Mock(return_value=True)
        game = Game(mock)
        self.assertEqual(game.createPLayer("nombre", 0), True)

    # Test para ver la puntuacion
    def test_seeScore(self):
        mock = Mock()
        game = Game(mock)
        self.assertTrue(game.seeScore("nombre"))

    # Test para comprobar la adivinanza
    def test_solutionQuizGameWord(self):
        mock = Mock()
        game = Game(mock)
        self.assertEqual(game.solutionQuizGameWord("araña"), True)

    # Test para comprobar el juego de la suma
    def test_solutionQuizNumber(self):
        mock = Mock()
        game = Game(mock)
        self.assertEqual(game.solutionQuizNumber(4), True)

    # Test para comprobar la segunda adivinanza
    def test_solutionQuizGameColor(self):
        mock = Mock()
        game = Game(mock)
        self.assertEqual(game.solutionQuizGameColor("blanco"), True)

    # Comprobar si se ha introducido un nombre con strings
    def test_input_createPLayer_just_ints(self):
        mock = Mock()
        game = Game(mock)
        self.assertRaises(Exception, game.createPLayer(3, 4))

    # Test sobrepaso numero de parametros
    def test_correct_params(self):
        mock = Mock()
        game = Game(mock)
        self.assertRaises(Exception, game.createPLayer("nomb", 1), 2)
        self.assertRaises(Exception, game.seeScore("nombere"), 1)
        self.assertRaises(Exception, game.solutionQuizGameWord("araña"), 1)
        self.assertRaises(Exception, game.solutionQuizNumber(3), 1)
        self.assertRaises(Exception, game.solutionQuizGameColor("verde"), 1)

    # Testeo para un socore negativo
    def test_ScoreAreSmallerThanCero(self):
        mock = Mock()
        game = Game(mock)
        self.assertRaises(Exception, game.createPLayer("nombre", -1))

    # Test para comprobar strings en la respuesta
    def test_String_input_in_solutionQuizGameNumber(self):
        mock = Mock()
        game = Game(mock)
        self.assertRaises(Exception, game.solutionQuizNumber("a"))

    # Test para comprobar ints en la respuesta
    def test_ints_input_in_solutionQuizGameWord(self):
        mock = Mock()
        game = Game(mock)
        self.assertRaises(Exception, game.solutionQuizGameWord(1))

    # Test para comprobar ints en la respuesta
    def test_ints_input_in_solutionQuizGameColor(self):
        mock = Mock()
        game = Game(mock)
        self.assertRaises(Exception, game.solutionQuizGameColor(2))


if __name__ == '__main__':
    unittest.main()
