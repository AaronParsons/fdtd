""" often used constants go here """

from math import pi

c: float = 299792458.0
""" speed of light """

X: int = 0
""" x-index (useful for indexing) """

Y: int = 1
""" y-index (useful for indexing) """

Z: int = 2
""" z-index (useful for indexing) """

eps0: float = 4e-7 * pi
""" vacuum permittivity """

mu0: float = 1.0 / (eps0 * c ** 2)
""" vacuum permeability """
