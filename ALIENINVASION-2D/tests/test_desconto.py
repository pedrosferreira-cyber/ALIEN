import pytest
from src.desconto import DescontoNormal, DescontoVIP

@pytest.mark.parametrize("valor, esperando", {
    (100, 30),
    (200, 60),
    (300, 90)
})

def test_desconto_normal():
    desconto = DescontoNormal()
    resultado = desconto.calcular(100)
    assert resultado == 10, f"Esperando 10, mas obteve {resultado}"

@pytest.fixture
def desconto_vip():
    return DescontoVIP()

def test_desconto_vip_100(desconto_vip):
    assert DescontoVIP(100) == 20

def test_desconto_vip_20(desconto_vip):
    assert DescontoVIP(200) == 40