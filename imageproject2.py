print('second image')

from PIL import Image

## Penguin on the beach
## Final requirement 1. (Load a green image and a background image. NB: desert.jpg is the background image).
image_penguin = Image.open('penguin.jpg')
image_beach = Image.open('beach.jpg')
pixels_penguin = image_penguin.load()
pixels_beach = image_beach.load()
image_penguin.show()
image_beach.show()
(width, height) = image_penguin.size
(width1, height1) = image_beach.size
print(f'Width Penguin: {width}; Height Penguin: {height}. \nWidth Beach: {width1}; Height Beach: {height1}')

## Final requirement 2. Create a new image that is the same size as the other images.
second_new = Image.open('the_second_new_image.jpg')
pixels_second_new = second_new.load()

# print(image_penguin.size)

## Get the idea of what the RGB are at a given backgound color.
print(pixels_penguin[40, 40])
# print(pixels_penguin[700, 500])
# print(pixels_penguin[200, 500])

## Final requirement 3. Iterate through all the pixels of the green image. Check to see if the green value is greater than a certain number and that the red and blue values are less than a certain number. If so, get the red, green, and blue values from the pixel at that location in the background image, if it's not a bright green color, get the red, green, and blue values from the pixel at that location in the green, foreground image.
for y in range(0, height):
    for x in range(0, width):
        (r, g, b) = pixels_penguin[x, y]
        
        if r <= 150 and g >= 150 and b <= 120:
            (new_r, new_g, new_b) = pixels_beach[x, y]
            ## Note the values are r <= 150, g >= 150, b <= 120
            pixels_penguin[x, y] = (new_r, new_g, new_b)

        else:
            pixels_penguin[x, y] = (r, g, b) 

## Create new image that is the same size as the original
penguin_beach = Image.new("RGB", image_penguin.size)
pixels_new = penguin_beach.load()

## Final requirement 5. Save the new image to a file.
image_penguin.save('the_second_new_image.jpg')

second_new = Image.open('the_second_new_image.jpg')
pixels_second_new = second_new.load()

# Display the final image
second_new.show()










