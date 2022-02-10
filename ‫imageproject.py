print('hello')

from PIL import Image
# print('Import worked successfuly')

## Loading the image
# image_og = Image.open('cat.jpg')
## Showing the image
# image_og.show()
## Pixel values
# width, height = image_og.size
# print(image_og.size)
## Get the pixels of the image and store them into a variable like this
# pixels_og = image_og.load()
## Once you have the pixels stored in a variable, you can access the red, green, and blue (RGB) values of an individual pixel at any spot in the image
# r, g, b = pixels_og[40, 40]
# print(pixels_og[40, 40])
## NOW set new red, green, and blue values (0 to 255) for the pixel at some x, y location (original RGB is 67,229,24) in the picture like this:
# pixels_og[40, 40] = (255, 0, 255)
## THEN display the picture
# image_og.show()
## READY to call the save function to save the new image
# image_og.save('the_file_goes_here.jpg')

# test = Image.open('the_file_goes_here.jpg')
# test.show()
# pixels_og = test.load()
# r, g, b = pixels_og[40, 40]
# print(pixels_og[40, 40])

## Requirement 4
# print(pixels_og[40, 40])
# print(pixels_og[400, 300])
# print(pixels_og[500, 200])
# print(pixels_og[700, 10])
# print(pixels_og[700, 250])

## Requirement 5
# pixels_og[40, 40] = (0, 0, 255)
# pixels_og[400, 300] = (255, 0, 0)
# pixels_og[500, 200] = (255, 0, 255)
# pixels_og[700, 10] = (0, 0, 255)
# pixels_og[700, 250] = (255, 0, 255)

## Requirement 6
# image_og.show()

## Final requirement 1. (Load a green image and a background image. NB: desert.jpg is the background image).
image_cactus = Image.open('cactus.jpg')
image_desert = Image.open('desert.jpg')
pixels_cactus = image_cactus.load()
pixels_desert = image_desert.load()
# image_cactus.show()
# image_desert.show()
width, height = image_cactus.size
width, height = image_desert.size
print(image_cactus.size)
print(image_desert.size)
# print(pixels_cactus[40, 40])
# print(pixels_cactus[700, 500])
# print(pixels_cactus[200, 500])

## Final requirement 3. Iterate through all the pixels of the green image. Check to see if the green value is greater than a certain number and that the red and blue values are less than a certain number. If so, get the red, green, and blue values from the pixel at that location in the background image, if it's not a bright green color, get the red, green, and blue values from the pixel at that location in the green, foreground image.
for y in range(0, height):
    for x in range(0, width):
        (r, g, b) = pixels_cactus[x, y]
        
        if r <= 170 and g >= 150 and b <= 230:
            # test = input('Check!')
            # new_r = pixels_desert[x, y]
            # new_g = pixels_desert[x, y]
            # new_b = pixels_desert[x, y]
            # new_r = r * 0 + 255
            # new_g = g * 0 + 255
            # new_b = b * 0 + 255

            (new_r, new_g, new_b) = pixels_desert[x, y]
            
            pixels_cactus[x, y] = (new_r + 35 , new_g, new_b)

        else:
            pixels_cactus[x, y] = (r, g, b) 

## Final requirement 2. Create a new image that is the same size as the other images.
cactus_desert = Image.new("RGB", image_cactus.size)
pixels_new = cactus_desert.load()

## Final requirement 5. Save the new image to a file.
image_cactus.save('the_first_new_image.jpg')

## Open the new image and display it
first_new = Image.open('the_first_new_image.jpg')
pixels_first_new = first_new.load()
first_new.show()


# image_new = Image.new("RGB", image_cactus.size)
# pixels_new = image_new.load()
# r, g, b = pixels_new
# pixels_new = (r, g, b)
# image_new.show()


## Final requirement 2
# image_cactus.paste(image_desert, (0,0))
# image_desert.paste(image_cactus, (0,0))
# overlayed_image = image_desert.paste(image_cactus, (0,0))


# overlayed_image.save('overlay.jpg')
# width, height = overlayed_image.size
# print(overlayed_image.size)

