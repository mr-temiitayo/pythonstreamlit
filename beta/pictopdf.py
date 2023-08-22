from PIL import Image

# Open the image file
img = Image.open("C:\\Users\\USER\\Desktop\\streamlipython\\pythonstreamlit\\media\\Golfcart Robot.jpg")

# Create a PDF file and add the image to it
img.save('golfcart.pdf', 'PDF', resolution=100.0)

# Close the image file
img.close()
