from unittest import TestCase
from bolos import Bolos
from errorDeFormato import *


class TestPerson(TestCase):
    def test_creacion_partida_vacia(self):
        partida = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        bolos = Bolos(partida)
        self.assertEqual(partida, bolos.partida)

    def test_creacion_partida_con_puntos(self):
        partida = [[0, 0], [3, 0], [2, 0], [0, 0], [7, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        bolos = Bolos(partida)
        self.assertEqual(partida, bolos.partida)

    def test_puntaje_partida_vacia(self):
        partida = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        bolos = Bolos(partida)
        self.assertEqual(0, bolos.puntaje())

    def test_puntaje_partida_con_puntos(self):
        partida = [[1, 0], [2, 0], [3, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        bolos = Bolos(partida)
        self.assertEqual(6, bolos.puntaje())

    def test_puntaje_partida_1_strike(self):
        partida = [["X"], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        bolos = Bolos(partida)
        self.assertEqual(10, bolos.puntaje())

    def test_puntaje_partida_1_strike_seguido_puntos(self):
        partida = [["X"], [3, 4], [2, 1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        bolos = Bolos(partida)
        self.assertEqual(27, bolos.puntaje())

    def test_puntaje_partida_2_strikes_seguidos(self):
        partida = [["X"], ["X"], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        bolos = Bolos(partida)
        self.assertEqual(30, bolos.puntaje())

    def test_puntaje_partida_3_strikes_seguidos(self):
        partida = [["X"], ["X"], ["X"], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        bolos = Bolos(partida)
        self.assertEqual(60, bolos.puntaje())

    def test_puntaje_partida_1_spare(self):
        partida = [[1, "/"], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        bolos = Bolos(partida)
        self.assertEqual(10, bolos.puntaje())

    def test_puntaje_partida_1_spare_y_puntos(self):
        partida = [[1, "/"], [2, 3], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        bolos = Bolos(partida)
        self.assertEqual(17, bolos.puntaje())

    def test_puntaje_partida_1_spare_y_strike(self):
        partida = [[1, "/"], ["X"], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        bolos = Bolos(partida)
        self.assertEqual(30, bolos.puntaje())

    def test_puntaje_partida_1_strike_y_spare(self):
        partida = [["X"], [1, "/"], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        bolos = Bolos(partida)
        self.assertEqual(30, bolos.puntaje())

    def test_puntaje_ultima_ronda_3_strikes(self):
        partida = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], ["X"], ["X", "X"]]
        bolos = Bolos(partida)
        self.assertEqual(30, bolos.puntaje())

    def test_puntaje_ultima_ronda_strike_spare(self):
        partida = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], ["X"], [1, "/"]]
        bolos = Bolos(partida)
        self.assertEqual(20, bolos.puntaje())

    def test_puntaje_ultima_ronda_strike_y_puntos(self):
        partida = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], ["X"], [1, 2]]
        bolos = Bolos(partida)
        self.assertEqual(13, bolos.puntaje())

    def test_puntaje_partida_perfecta_menos_ultimo_spare(self):
        partida = [["X"], ["X"], ["X"], ["X"], ["X"], ["X"], ["X"], ["X"], ["X"], ["X"], [1, "/"]]
        bolos = Bolos(partida)
        self.assertEqual(281, bolos.puntaje())

    def test_puntaje_strike_en_9_seguido_de_spare(self):
        partida = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], ["X"], [1, "/"], [0]]
        bolos = Bolos(partida)
        self.assertEqual(30, bolos.puntaje())

    def test_x_minuscula(self):
        partida = [["X"], ["X"], ["x"], ["X"], ["X"], ["X"], ["X"], ["X"], ["X"], ["X"], ["x", "x"]]
        bolos = Bolos(partida)
        self.assertEqual(300, bolos.puntaje())

    def test_string_en_lugar_de_numero(self):
        partida = [["uno", 2], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        with self.assertRaises(ErrorBolos):
            bolos = Bolos(partida)

    def test_otro_tipo_de_dato(self):
        partida = [[0, [1]], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        with self.assertRaises(ErrorTipoDeDato):
            bolos = Bolos(partida)

    def test_partida_incompleta(self):
        partida = [["X"], ["X"], ["x"], ["X"], ["X"], ["X"], ["X"], ["X"], ["X"], ["x", "x"]]
        with self.assertRaises(ErrorDeRonda):
            bolos = Bolos(partida)

    def test_partida_mas_de_10_rondas(self):
        partida = [["X"], ["X"], ["x"], ["X"], ["X"], ["X"], ["X"], ["X"], ["X"], ["X"], ["X"], ["x", "x"]]
        with self.assertRaises(ErrorDeFormato):
            bolos = Bolos(partida)

    def test_ronda_no_strike_o_spare_1_sola_tirada(self):
        partida = [[0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        with self.assertRaises(ErrorDeRonda):
            bolos = Bolos(partida)

    def test_ronda_no_strike_o_spare_3_tiradas(self):
        partida = [[0, 0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        with self.assertRaises(ErrorDeRonda):
            bolos = Bolos(partida)

    def test_ultima_ronda_incompleta(self):
        partida = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1]]
        with self.assertRaises(ErrorDeRonda):
            bolos = Bolos(partida)

    def test_ultima_ronda_invalida_larga(self):
        partida = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [2, 3]]
        with self.assertRaises(ErrorDeRondaExtra):
            bolos = Bolos(partida)

    def test_ronda_invalida_strike_y_puntos(self):
        partida = [["X", 2], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        with self.assertRaises(ErrorDeRonda):
            bolos = Bolos(partida)

    def test_ronda_spare_invalido(self):
        partida = [["/", 2], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        with self.assertRaises(ErrorDeRonda):
            bolos = Bolos(partida)

    def test_puntos_negativos(self):
        partida = [[-3, 2], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        with self.assertRaises(ErrorDeRonda):
            bolos = Bolos(partida)

    def test_puntos_negativos_ultima_ronda(self):
        partida = [[0, 2], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0,0], [-1, 0]]
        with self.assertRaises(ErrorDeRondaExtra):
            bolos = Bolos(partida)

    def test_ronda_spare_invalido_ultima_ronda(self):
        partida = [[3, 2], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], ["X"], ["/", 0]]
        with self.assertRaises(ErrorDeRondaExtra):
            bolos = Bolos(partida)

    def test_ronda_invalida_mas_de_10_puntos(self):
        partida = [[9, 2], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        with self.assertRaises(ErrorDeRonda):
            bolos = Bolos(partida)

    def test_ultima_ronda_2_tiradas_mas_de_10_puntos(self):
        partida = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [5, 6]]
        with self.assertRaises(ErrorDeRonda):
            bolos = Bolos(partida)

    def test_tirada_mas_de_9_puntos_no_x(self):
        partida = [[10, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        with self.assertRaises(ErrorDeRonda):
            bolos = Bolos(partida)

    def test_tirada_mas_de_9_puntos_no_x_ultima_ronda(self):
        partida = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [10, 0]]
        with self.assertRaises(ErrorDeRondaExtra):
            bolos = Bolos(partida)

