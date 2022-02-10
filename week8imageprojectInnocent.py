print("Innocent's Image Project")

from PIL import Image
# The first image
image_cactus = Image.open('cactus.jpg')
image_desert = Image.open('desert.jpg')
pixels_cactus = image_cactus.load()
pixels_desert = image_desert.load()
# image_cactus.show()
# image_desert.show()

# Create new image that is the same size as the original
cactus_desert = Image.new("RGB", image_cactus.size)
pixels_new = cactus_desert.load()

# Iterate through all the pixels of the green backgroung image
for y in range(0, 600):
    for x in range(0, 800):
        (r, g, b) = pixels_cactus[x, y]
        
        # The new pixels to set upon meeting the below conditions. First determine what the RGB values are on the backgroung color and then set the RGB if statement.
        if r <= 170 and g >= 150 and b <= 230:
            # (new_r, new_g, new_b) = pixels_desert[x, y]
            # pixels_cactus[x, y] = (new_r + 35 , new_g, new_b + 20)
            
            # Also try this if statement for a similar result:
            pixels_cactus[x, y] = pixels_desert[x, y]
        else:
            pixels_cactus[x, y] = (r, g, b) 

# Save the new image
image_cactus.save('the_first_new_image.jpg')
# Open the image, load pixels and show it
first_new = Image.open('the_first_new_image.jpg')
pixels_first_new = first_new.load()
first_new.show()

# The second image
image_penguin = Image.open('penguin.jpg')
image_beach = Image.open('beach.jpg')
pixels_penguin = image_penguin.load()
pixels_beach = image_beach.load()
# image_penguin.show()
# image_beach.show()

penguin_beach = Image.new("RGB", image_penguin.size)
pixels_new = penguin_beach.load()

for y in range(0, 600):
    for x in range(0, 800):
        (r, g, b) = pixels_penguin[x, y]
        
        if r <= 150 and g >= 150 and b <= 120:
            (new_r, new_g, new_b) = pixels_beach[x, y]

            pixels_penguin[x, y] = (new_r, new_g, new_b)
        else:
            pixels_penguin[x, y] = (r, g, b) 

image_penguin.save('the_second_new_image.jpg')

second_new = Image.open('the_second_new_image.jpg')
pixels_second_new = second_new.load()
second_new.show()

# The third image
image_penguin = Image.open('penguin.jpg')
image_snow = Image.open('snowscape.jpg')
pixels_penguin = image_penguin.load()
pixels_snow = image_snow.load()
# image_penguin.show()
# image_snow.show()

penguin_snow = Image.new("RGB", image_penguin.size)
pixels_new = penguin_snow.load()

for y in range(0, 600):
    for x in range(0, 800):
        (r, g, b) = pixels_penguin[x, y]
        
        if r <= 150 and g >= 150 and b <= 150:
            (new_r, new_g, new_b) = pixels_snow[x, y]
             
            pixels_penguin[x, y] = (new_r, new_g, new_b)
        else:
            pixels_penguin[x, y] = (r, g, b)


image_penguin.save('the_third_new_image.jpg')

third_new = Image.open('the_third_new_image.jpg')
pixels_third_new = third_new.load()

third_new.show()

# The fourth image
image_walk = Image.open('walk.jpg')
pixels_walk = image_walk.load
# image_walk.show()

image_sunset = Image.open('sunset.jpg')
pixels_sunset = image_sunset.load()
# image_sunset.show()

# Resize image_walk
image_walk_new = image_walk.resize((800, 600))
image_walk_new1 = image_walk_new.rotate(90)
# image_walk_new1.show()
image_walk_new1.save('walk_new.jpg')
image_walk_new1 = Image.open('walk_new.jpg')
pixels_walk_new = image_walk_new1.load()
(width2, height2) = image_walk_new1.size

sunset_walk = Image.new("RGB", image_walk_new.size)
pixels_new = sunset_walk.load()

for y in range(0, height2):
    for x in range(0, width2):
        (r, g, b) = pixels_walk_new[x, y]

        if r <= 200 and g <= 255 and b >= 200 or (r >= 100 and g >= 100 and b >= 245):
            (new_r, new_g, new_b) = pixels_sunset[x, y]
            pixels_walk_new[x, y] = (new_r, new_g, new_b)
        else:
            pixels_new[x, y] = (r, g, b)
            
# Final requirement 5. Save the new image to a file.
image_walk_new1.save('sunset_walk.jpg')
fourth_new = Image.open('sunset_walk.jpg')
pixels_fourth_new = fourth_new.load()

# Display final image
fourth_new.show()


# Requesting for the location of images on the computer to work with 

# The fifth image of user's choice (Making it my own)
from PIL import Image
image_sunset = Image.open('sunset.jpg')
pixels_sunset = image_sunset.load()

import glob
image_list = []
path = input('Please enter the path for your green background images, with the image name and format (I would recommend boat.jpg): ')

for filename in glob.glob(path):
    im = Image.open(filename)
    image_list.append(im)

    pixels_choice = im.load()
    # im.show()
    (width, height) = im.size
    
    choice_new = Image.new("RGB", im.size)
    pixels_choice_new = choice_new.load()

    for y in range(0, height):
        for x in range(0, width):
            (r, g, b) = pixels_choice[x, y]
            if r <= 120 and g >= 150 and b <= 120:
                (new_r, new_g, new_b) = pixels_sunset[x, y]
                pixels_choice[x, y] = (new_r, new_g, new_b)
            else:
                pixels_choice[x, y] = (r, g, b)
  
    im.save('your_image.jpg')
    im.show()
print('I hope you liked you liked images!')