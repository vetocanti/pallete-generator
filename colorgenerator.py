import colorsys

def generate_complementary_palette(base_color, num_colors):
    # Convert the RGB color to the range [0, 1]
    r, g, b = [x / 255.0 for x in base_color]

    # Convert RGB to HSV (Hue, Saturation, Value/Brightness)
    h, s, v = colorsys.rgb_to_hsv(r, g, b)

    # Find the complementary hue (180 degrees shift)
    complementary_h = (h + 0.5) % 1.0

    # Generate a color palette with complementary colors
    colors = []
    for i in range(num_colors):
        new_h = (complementary_h + (i + 1) * 0.1) % 1.0  # Slightly vary the hue
        r, g, b = colorsys.hsv_to_rgb(new_h, s, v)
        colors.append((int(r * 255), int(g * 255), int(b * 255)))

    return colors

def plot_color_palette(colors):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(8, 1))
    for i, color in enumerate(colors):
        ax.add_patch(plt.Rectangle((i, 0), 1, 1, color=[x / 255.0 for x in color]))
    ax.axis('off')
    plt.show()

if __name__ == "__main__":
    # Specify the base color in RGB format (e.g., red)
    base_color = (20,20,0)

    # Specify the number of colors you 4ant in the palette.
    num_colors = 6

    # Generate the complementary color palette.
    palette = generate_complementary_palette(base_color, num_colors)

    # Plot the color palette.
    plot_color_palette(palette)
