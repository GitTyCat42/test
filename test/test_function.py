from library.demofunc import *
import random

def test_demofunc():
  assert demofunc() == 42

def test_demomul():
  assert demomul(2,3) == 6
  assert demomul(3,3) >= 9
  assert demomul(3,3) < 10
  assert demomul(0,1) == 0

def test_demopi():
    # Testen ob Pi auf den ersten 10 Stellen gleich 3.1415926535 ist, also im Intervall [3.1415926535, 3.1415926536)
    assert demopi() < 3.1415926536
    assert demopi() >= 3.1415926535

def test_demofailmul():
    assert demofailmul(6,7) == 42

def test_demomul2():
    # 1. teste kleines 1 mal 1
    for i in range(1,10):
        for j in range(1,10):
            assert demomul2(i,j) == i*j
    # 2. teste 10 zufaellige Zahlenpaare von 1 bis 1000
    for i in range(1,10):
        a = random.randint(0,1000)
        b = random.randint(0,1000)
        assert demomul2(a,b) == a*b
