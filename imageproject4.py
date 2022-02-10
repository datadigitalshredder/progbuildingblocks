print('fourth image')

from PIL import Image
image_walk = Image.open('walk.jpg')
pixels_walk = image_walk.load
image_walk.show()

image_sunset = Image.open('sunset.jpg')
pixels_sunset = image_sunset.load()
image_sunset.show()
(width, height) = image_walk.size
(width1, height1) = image_sunset.size
print(f'Walk width: {width}; Walk height: {height} \nSunset width: {width1}; Sunset height: {height1}')

## Resize image_walk
image_walk_new = image_walk.resize((800, 600))
image_walk_new1 = image_walk_new.rotate(90)
image_walk_new1.show()
image_walk_new1.save('walk_new.jpg')
image_walk_new1 = Image.open('walk_new.jpg')
pixels_walk_new = image_walk_new1.load()
(width2, height2) = image_walk_new1.size
print(f'Width new walk: {width2}; Height new walk: {height2}')
print(pixels_walk_new[500, 40])
print(pixels_walk_new[680, 550])

for y in range(0, height2):
    for x in range(0, width2):
        (r, g, b) = pixels_walk_new[x, y]

        if r <= 200 and g <= 255 and b >= 200 or (r >= 100 and g >= 100 and b >= 245):
            (new_r, new_g, new_b) = pixels_sunset[x, y]
            pixels_walk_new[x, y] = (new_r, new_g, new_b)
        else:
            pixels_walk_new[x, y] = (r, g, b)

## Create new image that is the same size as the original
sunset_walk = Image.new("RGB", image_walk_new.size)
pixels_new = sunset_walk.load()
# sunset_walk.show()

## Final requirement 5. Save the new image to a file.
image_walk_new1.save('sunset_walk.jpg')
fourth_new = Image.open('sunset_walk.jpg')
pixels_fourth_new = fourth_new.load()

## Display final image
fourth_new.show()
# print(fourth_new.size)