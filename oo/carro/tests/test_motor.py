from oo.carro.motor import Motor


def test_motor_deve_possuir_velocidade_zero_apos_ser_instanciado():
    # Dado um novo motor
    motor = Motor()

    # Deve possuir velocidade inicial zero
    assert motor.velocidade == 0


def test_motor_deve_possuir_velocidade_incrementada_em_uma_unidade_apos_acelerar():
    # Dado um novo motor, com velocidade inicial zero
    motor = Motor()
    velocidade_original = motor.velocidade

    # Após acelerar
    motor.acelerar()

    # Deve possuir velocidade incrementada em uma unidade
    assert motor.velocidade == (velocidade_original + 1)


def test_motor_deve_possuir_velocidade_decrementada_em_duas_unidades_apos_frear():
    # Dado um novo motor, com duas acelerações (velocidade alterada para 2)
    motor = Motor()
    motor.acelerar()
    motor.acelerar()

    # Quando frear
    motor.frear()

    # Deve possuir velocidade zero
    assert motor.velocidade == 0
