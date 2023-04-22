from PIL import Image
from colorthief import ColorThief
import matplotlib.pyplot as plt

# LOAD IMAGE FROM SAME FOLDER AS PYTHON PROJECT
image = Image.open("0001.png")

# USE COLOR-THIEF TO EXTRACT THE PALETTE OF COLORS
color_thief = ColorThief("0001.png")
palette = color_thief.get_palette(color_count=8)

# DISPLAY THE PALETTE VISUALLY USING MATPLOTLIB
fig = plt.figure(figsize=(8, 2))
ax = fig.add_subplot(111)

for i, color in enumerate(palette):
    r, g, b = color
    color_hex = "#{:02x}{:02x}{:02x}".format(r, g, b)
    rect = plt.Rectangle((i, 0), 1, 1, color=color_hex)
    ax.add_patch(rect)
    
    # ADD THE RGB INFO UNDERNEATH EACH COLOR
    ax.text(i + 0.5, -0.1, f"({r}, {g}, {b})", fontsize=8, ha='center', va='center')

plt.xlim((0, len(palette)))
plt.ylim((0, 1))
plt.axis('off')
plt.show()

# This Python code extracts the palette of colors from an image file and displays it visually using Matplotlib. 
# The code uses the Pillow library to load an image file and the colorthief library to extract the color palette.

# After opening the image file, the code uses the ColorThief class from the colorthief library 
# to extract the palette of colors from the image. The get_palette() method is called on the ColorThief object 
# with an argument of color_count=8 to specify the number of colors to extract.

# The code then creates a Matplotlib figure and adds a rectangle for each color in the palette. 
# The color of each rectangle is set using the RGB values of the corresponding color in the palette. 
# The RGB values are also displayed underneath each color rectangle.

# The resulting plot is displayed using the plt.show() method.

# Note that the image file must be in the same directory as the Python script and should be specified in both the Image.open() and ColorThief() methods.