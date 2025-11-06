from PIL import Image, ImageDraw, ImageFont

# Load the image (simulating scanning)
image = Image.open("C:\\image.jpg")  # Replace with your image path

# Create a drawing context
draw = ImageDraw.Draw(image)

# Choose a font and size
font = ImageFont.truetype("arial.ttf", size=40)  # You can change font and size

# Define the text and position
text = "Subh Deepawali"
position = (270, 300)  # x, y coordinates

# Set text color
text_color = (255, 0, 0)  # Red in RGB

# Add the text to the image
draw.text(position, text, fill=text_color, font=font)

# Save or show the image
image.save("output_image.jpg")  # Or use image.show()
