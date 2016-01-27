import numpy
from PIL import Image, ImageGrab
from pymouse import PyMouse
from pykeyboard import PyKeyboard
from time import sleep
import random
from splinter import Browser

global counter, scrolled
m = PyMouse()
k = PyKeyboard()
br = Browser("firefox")
scrolled = []

share = Image.open("Images/share.png")
selec = Image.open("Images/selec.png")
poss = Image.open("Images/poss.png")
group = Image.open("Images/group.png")
like = Image.open("Images/like.png")

def subimg(img1,img2):
	print("Image captured")
	img1=numpy.asarray(img1)
	img2=numpy.asarray(img2)

	img1y=img1.shape[0]
	img1x=img1.shape[1]

	img2y=img2.shape[0]
	img2x=img2.shape[1]

	stopy=img2y-img1y+1
	stopx=img2x-img1x+1

	for x1 in range(0,stopx):
		for y1 in range(0,stopy):
			x2=x1+img1x
			y2=y1+img1y

			pic=img2[y1:y2,x1:x2]
			test=pic==img1

		if test.all():
			return x1, y1

	return False

def checkpost():
	br.visit("https://www.facebook.com/devbattles")
	sleep(10)
	for s in scrolled:
		m.scroll(s)
	if subimg(like, ImageGrab.grab()) == False:
		return False
	else:
		return True
		
def main():
	try:
		pos = False
		scrolled = []
		f = open("groups.txt", "r")
		while pos == False:
			scrolled.append(random.randint(-3, -1))
			m.scroll(scrolled[-1])
			sleep(3)
			pos = subimg(share, ImageGrab.grab())
		if pos[1] > 450:
			m.scroll(-2)
			sleep(2)
			pos = subimg(share, ImageGrab.grab())
			scrolled.append(-2)
			sleep(4)
		for line in f.readlines():
			pos = subimg(like, ImageGrab.grab())
			sleep(2)
			m.click(pos[0] + random.randint(20, 30), pos[1] + random.randint(5, 10))
			sleep(2)
			pos = subimg(share, ImageGrab.grab())
			sleep(2)
			m.click(pos[0] + random.randint(20, 30), pos[1] + random.randint(5, 10))
			sleep(2)
			m.click(pos[0] + random.randint(10, 20), pos[1] + random.randint(65, 75))
			sleep(13)
			pos1 = subimg(selec, ImageGrab.grab())
			sleep(15)
			m.click(pos1[0] + random.randint(10, 20), pos1[1] + random.randint(5, 17))
			sleep(15)
			pos = subimg(group, ImageGrab.grab())
			m.click(pos[0] + random.randint(10, 50), pos[1] + random.randint(5, 17))
			sleep(15)
			k.type_string(line, 0.2)
			m.click(pos1[0] + random.randint(170, 200), pos1[1] + random.randint(89, 100))
			m.scroll(-5)
			sleep(10)
			pos = subimg(poss, ImageGrab.grab())
			m.click(pos[0] + random.randint(2, 10), pos[1] + random.randint(5, 17))
			sleep(10)
		f.close()
	except:
		pass
br.visit("http://fb.com")
raw_input("Open facebook and press Enter...")
sleep(5)
main()
while True:
	if checkpost():
		br.visit("https://www.facebook.com/devbattles")
		sleep(10)
		main()