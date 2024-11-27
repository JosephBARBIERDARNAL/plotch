import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure


def _copy_figure_properties(source_fig: Figure, target_fig: Figure):
    """
    Copy essential figure properties from source to target figure.

    Args:
        source_fig (Figure): Source figure to copy properties from
        target_fig (Figure): Target figure to copy properties to
    """
    target_fig.set_facecolor(source_fig.get_facecolor())
    target_fig.set_edgecolor(source_fig.get_edgecolor())
    target_fig.set_dpi(source_fig.get_dpi())


def _add_axes(self, other):
    """
    Horizontally combine two axes using subfigures.

    Args:
        self (Axes): First axes to combine
        other (Axes): Second axes to combine

    Returns:
        Axes: The first subplot in the new layout
    """
    if not isinstance(other, Axes):
        return NotImplemented

    # Create a new figure with subfigures
    fig = plt.figure(figsize=(12, 7))
    _copy_figure_properties(self.figure, fig)

    # Create subfigures
    subfigs = fig.subfigures(1, 2, wspace=0.05)

    # Draw source figures to capture their contents
    self.figure.canvas.draw()
    other.figure.canvas.draw()

    # Create axes in subfigures and render existing plots
    sf1_ax = subfigs[0].add_subplot(111)
    sf1_ax.imshow(self.figure.canvas.renderer.buffer_rgba(), interpolation="nearest")
    # sf1_ax.axis("off")

    sf2_ax = subfigs[1].add_subplot(111)
    sf2_ax.imshow(other.figure.canvas.renderer.buffer_rgba(), interpolation="nearest")
    # sf2_ax.axis("off")

    fig.tight_layout()
    return sf1_ax


def _divide_axes(self, other):
    """
    Vertically combine two axes using subfigures.

    Args:
        self (Axes): First axes to combine
        other (Axes): Second axes to combine

    Returns:
        Axes: The first subplot in the new layout
    """
    if not isinstance(other, Axes):
        return NotImplemented

    # Create a new figure with subfigures
    fig = plt.figure(figsize=(7, 10))
    _copy_figure_properties(self.figure, fig)

    # Create subfigures
    subfigs = fig.subfigures(2, 1, height_ratios=[1, 1], hspace=0.05)

    # Draw source figures to capture their contents
    self.figure.canvas.draw()
    other.figure.canvas.draw()

    # Create axes in subfigures and render existing plots
    sf1_ax = subfigs[0].add_subplot(111)
    sf1_ax.imshow(self.figure.canvas.renderer.buffer_rgba(), interpolation="nearest")
    # sf1_ax.axis("off")

    sf2_ax = subfigs[1].add_subplot(111)
    sf2_ax.imshow(other.figure.canvas.renderer.buffer_rgba(), interpolation="nearest")
    # sf2_ax.axis("off")

    fig.tight_layout()
    return sf1_ax


if __name__ == "__main__":
    from matplotlib.axes import Axes

    # Monkey patch Axes class with custom methods
    Axes.__add__ = _add_axes
    Axes.__truediv__ = _divide_axes

    # Create sample plots
    _, ax1 = plt.subplots(dpi=300)
    ax1.set_facecolor("#fb4040")
    ax1.plot([1, 2, 3], [1, 2, 3])

    _, ax2 = plt.subplots(dpi=300)
    ax2.scatter([1, 2, 3], [3, 2, 1])

    _, ax3 = plt.subplots(dpi=300)
    ax3.bar(["Jo", "Mat", "Lo"], [1, 2, 3])

    # Combine plots using custom operators
    (ax1 + ax2) / ax3

    # Save the figure
    fig = plt.gcf()
    fig.savefig("test.png", dpi=300)
