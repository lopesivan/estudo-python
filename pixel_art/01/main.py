from PIL import Image, ImageDraw

# Define the size of the image
width, height = 16, 16

# Create a new image with a white background
image = Image.new("RGBA", (width, height), (255, 255, 255, 0))

# Create a draw object to draw on the image
draw = ImageDraw.Draw(image)

# Define the colors for the tree
tree_color = (0, 128, 0, 255)
trunk_color = (139, 69, 19, 255)

# Draw the tree leaves
draw.rectangle([4, 2, 11, 5], fill=tree_color)
draw.rectangle([2, 6, 13, 9], fill=tree_color)
draw.rectangle([0, 10, 15, 12], fill=tree_color)

# Draw the tree trunk
draw.rectangle([6, 13, 9, 15], fill=trunk_color)

# Save the image as a PNG file
image.save("tree_pixel_art.png")

# Display the image
image.show()
