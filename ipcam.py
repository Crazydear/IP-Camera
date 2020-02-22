import cv2

'''
pip install opencv-contrib-python
'''
'''
url = 'rtsp://192.168.0.102:8080/h264_ulaw.sdp'
cap = cv2.VideoCapture(url)

while(cap.isOpened()):  # Capture frame-by-frame  
	ret, frame = cap.read()
	# Display the resulting frame  
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break   # When everything done, release the capture  
cap.release()
cv2.destroyAllWindows()'''

from tkinter import *
import cv2
import os
from PIL import Image, ImageTk
from tkinter import ttk


# from multiprocessing import Process
# import facial_recognition
# import database

class APP:
	def __init__(self):
		self.camera = None  # 摄像头
		self.root = Tk()
		self.root.title('IP Camera')
		self.root.geometry('%dx%d' % (1450, 1080))
		self.createFirstPage()
		mainloop()

	def createFirstPage(self):
		self.page1 = Frame(self.root)
		self.page1.place(relx=0., rely=0., relwidth=1.00, relheight=1.00)

		self.url = Label(self.page1, text='URL', font=('粗体', 10))
		self.url.place(relx=0.011, rely=0., relwidth=0.044, relheight=0.05)

		self.Text1Var = StringVar(value='')
		self.Text1 = Entry(self.page1, text='Text1', textvariable=self.Text1Var, font=('宋体', 9))
		self.Text1.place(relx=0.063, rely=0., relwidth=0.856, relheight=0.05)

		image = Image.open("1.jpg")  # 随便使用一张图片 不要太大
		photo = ImageTk.PhotoImage(image=image)
		self.data1 = Label(self.page1, image=photo)
		self.data1.image = photo
		self.data1.place(relx=0., rely=0.08, relwidth=0.92, relheight=0.898)

		self.button11 = Button(self.page1, width=18, height=2, text="检测", bg='red', font=("宋", 12),
							   relief='raise', command=self.createSecondPage)
		self.button11.place(relx=0.929, rely=0., relwidth=0.054, relheight=0.05)

		self.button12 = Button(self.page1, width=18, height=2, text="开始", bg='green', font=("宋", 12),
							   relief='raise', command=self.createSecondPage)
		self.button12.place(relx=0.939, rely=0.08, relwidth=0.044, relheight=0.05)

		self.button13 = Button(self.page1, width=18, height=2, text="暂停", bg='gray', font=("宋", 12),
							   relief='raise', command=self.backFirst)
		self.button13.place(relx=0.939, rely=0.16, relwidth=0.044, relheight=0.05)

		self.button14 = Button(self.page1, width=18, height=2,text='退出',  bg='gray', font=("宋", 12),
							   relief='raise', command=self.quitMain)
		self.button14.place(relx=0.939, rely=0.24, relwidth=0.044, relheight=0.05)

	def createSecondPage(self):
		url = 'rtsp://192.168.0.102:8080/h264_ulaw.sdp'
		self.camera = cv2.VideoCapture(url)
		self.video_loop(self.data1)

	def video_loop(self, panela):
		success, img = self.camera.read()  # 从摄像头读取照片
		if success:
			cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)  # 转换颜色从BGR到RGBA
			current_image = Image.fromarray(cv2image)  # 将图像转换成Image对象
			imgtk = ImageTk.PhotoImage(image=current_image)
			panela.imgtk = imgtk
			panela.config(image=imgtk)
			self.root.after(40, lambda: self.video_loop(panela))

	def backFirst(self):
		# 释放摄像头资源
		self.camera.release()
		cv2.destroyAllWindows()

	def backMain(self):
		self.root.geometry('900x600')
		self.page3.pack_forget()
		self.page1.pack()

	def quitMain(self):
		sys.exit(0)


if __name__ == '__main__':
	demo = APP()
