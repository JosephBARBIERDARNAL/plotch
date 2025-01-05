from matplotlib.axes import Axes
from .main import _add_axes, _truediv_axes
from .config import Params

# Monkey-patch our Axes class so + and / do special things
Axes.__add__ = _add_axes
Axes.__truediv__ = _truediv_axes

__all__ = ["Params"]
