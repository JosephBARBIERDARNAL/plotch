import matplotlib.pyplot as plt
from matplotlib.axes import Axes


def _add_axes(self, other):
    """Horizontal composition of two axes"""
    if not isinstance(other, Axes):
        return NotImplemented

    fig = plt.figure(figsize=(12, 5))

    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)

    self.figure.canvas.draw()
    other.figure.canvas.draw()

    ax1.imshow(self.figure.canvas.renderer.buffer_rgba())
    ax2.imshow(other.figure.canvas.renderer.buffer_rgba())

    for ax in [ax1, ax2]:
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_visible(False)

    plt.tight_layout()

    return ax1


def _divide_axes(self, other):
    """Vertical composition of two axes"""
    if not isinstance(other, Axes):
        return NotImplemented

    fig = plt.figure(figsize=(6, 6))

    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)

    self.figure.canvas.draw()
    other.figure.canvas.draw()

    ax1.imshow(self.figure.canvas.renderer.buffer_rgba())
    ax2.imshow(other.figure.canvas.renderer.buffer_rgba())

    for ax in [ax1, ax2]:
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_visible(False)

    plt.tight_layout()

    return ax1
