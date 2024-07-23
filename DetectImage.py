import pyautogui as py
import os


def getHero():
	directory = os.listdir("images") # list of all images to detect

	# loop through list to find the image that matches
	for file in directory:
		print(file)
		if file.endswith('.png') or file.endswith('.jpg'):
			try:
				search = py.locateOnScreen("images\\" + file, confidence=0.65)
				return file.removesuffix(".png").removesuffix(".jpg")
			except py.ImageNotFoundException:
				continue

	return None