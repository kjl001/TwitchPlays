import pyautogui as py
import os


def getHero():
	image_list = [] # list of images

	directory = os.listdir("images") # list of all images to detect

	for file in directory:
		if file.endswith('.png') or file.endswith('.jpg'):
			image_list.append(file)

	# loop through list to find the image that matches
	for image in image_list:
		print(image)
		try:
			search = py.locateOnScreen("images\\" + image, confidence=0.7)
			print("IMAGE FOUND")
			return image
		except py.ImageNotFoundException:
			print("IMAGE NOT FOUND")