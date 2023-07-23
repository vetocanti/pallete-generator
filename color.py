import matplotlib.pyplot as plt
import numpy as np

def generate_color_palette(cmap_name, num_colors):
    cmap = plt.get_cmap(cmap_name)
    colors = cmap(np.linspace(0, 1, num_colors))
    return colors

def plot_color_palette(colors):
    fig, ax = plt.subplots(figsize=(8, 1))
    for i, color in enumerate(colors):
        ax.add_patch(plt.Rectangle((i, 0), 1, 1, color=color))
    ax.axis('off')
    plt.show()

if __name__ == "__main__":
    # Choose a colormap name from matplotlib's available colormaps.
    # You can find the list of available colormaps at:
    # https://matplotlib.org/stable/tutorials/colors/colormaps.html
    colormap_name = "viridis"

    # Specify the number of colors you want in the palette.
    num_colors = 20

    # Generate the color palette.
    palette = generate_color_palette(colormap_name, num_colors)

    # Plot the color palette.
    plot_color_palette(palette)
