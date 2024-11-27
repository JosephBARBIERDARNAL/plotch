import matplotlib.pyplot as plt


# Assuming you have two existing axes
def transfer_axes_elements(source_axes, destination_axes):
    """
    Transfer all children (elements) from one axes to another.

    Parameters:
    -----------
    source_axes : matplotlib.axes.Axes
        The source axes from which elements will be transferred
    destination_axes : matplotlib.axes.Axes
        The destination axes where elements will be added
    """
    # Get all children from the source axes
    children = source_axes.get_children()

    # Transfer each child to the destination axes
    for child in children:
        # Some children might need special handling
        if hasattr(child, "axes"):
            print(child)
            # child.axes = destination_axes
            # destination_axes.add_artist(child)


# Example usage
fig, (ax1, ax2) = plt.subplots(1, 2)

# Plot something on the first axes
ax1.plot([1, 2, 3], [4, 5, 6], "r-")
ax1.set_title("Original Axes")

# Transfer elements to the second axes
transfer_axes_elements(ax1, ax2)
ax2.set_title("Transferred Elements")

plt.show()
