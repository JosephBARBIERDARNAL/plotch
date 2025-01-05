import matplotlib.pyplot as plt
from matplotlib.axes import Axes


def _fig2rgb_array(fig):
    fig.canvas.draw()
    buf = fig.canvas.renderer.buffer_rgba()
    return buf


def _add_axes(self, other):
    if not isinstance(other, Axes):
        return NotImplementedError

    self.figure.set_facecolor(plt.gcf().get_facecolor())
    other.figure.set_facecolor(plt.gcf().get_facecolor())

    fig = plt.figure(figsize=(10, 6))

    ax_left = fig.add_axes([0.0, 0.0, 0.5, 1.0])
    ax_right = fig.add_axes([0.5, 0.0, 0.5, 1.0])
    ax_left.axis("off")
    ax_right.axis("off")

    self.figure.canvas.draw()
    other.figure.canvas.draw()

    ax_left.imshow(_fig2rgb_array(self.get_figure()))
    ax_right.imshow(_fig2rgb_array(other.get_figure()))

    return ax_left


def _truediv_axes(self, other):
    """
    Defines what happens when we do: ax1 / ax2.
    Places them in a new figure, stacked vertically (top and bottom).
    """
    if not isinstance(other, Axes):
        return NotImplementedError

    self.figure.set_facecolor(plt.gcf().get_facecolor())
    other.figure.set_facecolor(plt.gcf().get_facecolor())

    fig = plt.figure(figsize=(8, 10))

    ax_top = fig.add_axes([0.0, 0.5, 1.0, 0.5])
    ax_bottom = fig.add_axes([0.0, 0.0, 1.0, 0.5])
    ax_top.axis("off")
    ax_bottom.axis("off")

    self.figure.canvas.draw()
    other.figure.canvas.draw()

    ax_top.imshow(_fig2rgb_array(self.figure))
    ax_bottom.imshow(_fig2rgb_array(other.figure))

    return ax_top


if __name__ == "__main__":
    from matplotlib.axes import Axes

    plt.style.use("dark_background")

    plt.rcParams["figure.dpi"] = 300
    plt.rcParams["savefig.dpi"] = 300

    # Monkey-patch our Axes class so + and / do special things
    Axes.__add__ = _add_axes
    Axes.__truediv__ = _truediv_axes

    _, ax1 = plt.subplots()
    ax1.set_facecolor("#fb4040")
    ax1.plot([1, 2, 3], [1, 2, 3])

    _, ax2 = plt.subplots()
    ax2.scatter([1, 2, 3], [3, 2, 1])

    _, ax3 = plt.subplots()
    ax3.bar(["A", "B", "C"], [1, 2, 3])

    # ax1 + ax2
    # plt.savefig("add.png")

    ax1 / ax2
    plt.savefig("div.png")

    # ax3 / (ax1 + ax2)
    # (ax1 + ax2) / ax3
    # plt.savefig("add_AND_div.png")
