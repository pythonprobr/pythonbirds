from oo.carro.motor import Motor


def test_motor_deve_possuir_velocidade_zero_apos_ser_instanciado():
    motor = Motor()
    assert motor.velocidade == 0

def test_motor_deve_possuir_velocidade_incrementada_em_uma_unidade_apos_acelerar():
    motor = Motor()
    velocidade_original = motor.velocidade
    motor.acelerar()
    assert motor.velocidade == (velocidade_original + 1)
