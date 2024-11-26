from matplotlib.axes import Axes
from .main import _add_axes, _divide_axes

Axes.__add__ = _add_axes
Axes.__truediv__ = _divide_axes
