import pytest

from src.desconto import DescontoNormal, DescontoVIP

def test_desconto_normal():
    desconto = DescontoNormal()
    resultado = desconto.calcular(100)
    assert resultado == 10, f"Esperando 10, mas obteve {resultado}"

@pytest.fixture
def desconto_vip():
    return DescontoVIP()

def test_desconto_vip_100(desconto_vip):
    resultado = desconto_vip.calcular(100)
    assert resultado == 20, f"Esperando 20, mas obteve {resultado}"

def test_desconto_vip_200(desconto_vip):
    resultado = desconto_vip.calcular(200)
    assert resultado == 40, f"Esperando 40, mas obteve {resultado}"