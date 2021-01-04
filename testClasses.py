import networkx as nx # type: ignore
import matplotlib.pyplot as plt # type: ignore
from sympy import symbols # type: ignore 
from sympy import Symbol # https://github.com/sympy/sympy/blob/master/sympy/core/symbol.py
from sympy import I # type: ignore
from typing import Optional

class Nodo:
    def __init__(self, name: str):
        self.name = name

class Orientation:
    def __init__(self, name: str):
        self.name = "positive"

class BasicComponent:
    def __init__(
        self,
        name: str, 
        nodo1: Nodo, 
        nodo2: Nodo, 
        value : Optional[float] = None, # If is Float can be int, here why: https://www.python.org/dev/peps/pep-0484/#the-numeric-tower
        orientation : Optional[Orientation] = None
        ):
            self.name : Symbol = symbols(name, positive=True) 
            self.nodo1 = nodo1 
            self.nodo2 = nodo2
            if (value is not None):
                if (value > 0):
                    self.value = value
                else:
                    raise ValueError("Sorry, value have to be greater than 0")
                    # ¿qué ocurre con selfValue si no lo defino en el init? es none? daría error? confuso.
            self.orientation = orientation

A = Nodo("V_1")
B = Nodo("V_2")
C = Orientation("A")

BasicComponent("L_1", A, B, -2)

