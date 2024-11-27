import matplotlib.pyplot as plt
from matplotlib.axes import Axes


def _copy_figure_properties(source_fig, target_fig):
    target_fig.set_facecolor(source_fig.get_facecolor())
    target_fig.set_edgecolor(source_fig.get_edgecolor())
    target_fig.set_dpi(source_fig.get_dpi())


def _add_axes(self, other):
    if not isinstance(other, Axes):
        return NotImplemented

    self.figure.set_facecolor(plt.gcf().get_facecolor())
    other.figure.set_facecolor(plt.gcf().get_facecolor())

    fig = plt.figure(figsize=(12, 7))
    _copy_figure_properties(self.figure, fig)

    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)

    self.figure.canvas.draw()
    other.figure.canvas.draw()

    ax1.imshow(self.figure.canvas.renderer.buffer_rgba(), interpolation="nearest")
    ax2.imshow(other.figure.canvas.renderer.buffer_rgba(), interpolation="nearest")

    for ax in [ax1, ax2]:
        ax.axis("off")

    fig.tight_layout()
    return ax1


def _divide_axes(self, other):
    if not isinstance(other, Axes):
        return NotImplemented

    self.figure.set_facecolor(plt.gcf().get_facecolor())
    other.figure.set_facecolor(plt.gcf().get_facecolor())

    fig = plt.figure(figsize=(7, 10))
    _copy_figure_properties(self.figure, fig)

    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)

    self.figure.canvas.draw()
    other.figure.canvas.draw()

    ax1.imshow(self.figure.canvas.renderer.buffer_rgba(), interpolation="nearest")
    ax2.imshow(other.figure.canvas.renderer.buffer_rgba(), interpolation="nearest")

    for ax in [ax1, ax2]:
        ax.axis("off")

    fig.tight_layout()
    return ax1


if __name__ == "__main__":
    from matplotlib.axes import Axes

    Axes.__add__ = _add_axes
    Axes.__truediv__ = _divide_axes

    _, ax1 = plt.subplots(dpi=300)
    ax1.set_facecolor("#fb4040")
    ax1.plot([1, 2, 3], [1, 2, 3])

    _, ax2 = plt.subplots(dpi=300)
    ax2.scatter([1, 2, 3], [3, 2, 1])

    _, ax3 = plt.subplots(dpi=300)
    ax3.bar(["Jo", "Mat", "Lo"], [1, 2, 3])

    (ax1 + ax2) / ax3

    fig = plt.gcf()
    fig.savefig("test.png", dpi=300)
