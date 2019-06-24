from PIL import Image

image = Image.open('images/n.jpg')

width = image.size[0]
height = image.size[1]

ideal_width = 200
ideal_height = 200

ideal_aspect_ratio = ideal_width / float(ideal_height)

image_aspect_ratio = width/float(height)

# Define new_width and new_height
new_width = -1
new_height = -1

def createResizeTuple() :
	'''Get a Resize Tuple based on current aspect ratio of the image

	The Resize tuple will be in square dimensions and the image will be cropped equally from either left and right side or top and bottom side.
	it compares the aspect ratios - depending on whether width or height is larger, that will decide whether to chop off the sides or the top and bottom.
	
	Args:

	Returns: 
		tuple: tuple with 4 entries in form of (x1, x2, y1, y2)
	'''

	# If width is greater than height
	if image_aspect_ratio > ideal_aspect_ratio :
		# Then crop the left and right side edges

		# New Width will be equal to Height
		new_width = height

		# Distribute this width equally between both right and left sides
		offset = (width - new_width) / 2

		# Create Resize Tuple (x1, x2, y1, y2)
		return (offset, 0, width - offset, height)
	else :
		# Then crop the top and botton side edges

		# New Height will be width
		new_height = width

		# Distribute this new height equally between both top and bottom sides
		offset = (height - new_height) / 2

		# Create Resize Tuple (x1, x2, y1, y2)
		return (0, offset, width, height - offset)

resize = createResizeTuple()

new_image = image.crop(resize)

new_image.save('images/target/n_copy.jpg')

print(resize)