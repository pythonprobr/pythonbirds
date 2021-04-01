from unittest import TestCase

from carro import Motor


class CarroTest(TestCase):
    def test_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(first=0, second=motor.velocidade)

    def test_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)
