from matplotlib.axes import Axes
from .main import _add_axes, _truediv_axes

Axes.__add__ = _add_axes
Axes.__truediv__ = _truediv_axes
