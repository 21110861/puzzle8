import pygame
import tkinter as tk
from tkinter import filedialog
from dichuyen import DiChuyển
from huongdichuyen import *
from hieuung import HiệuỨng

class MaTrận:
	def __init__(self,viTri ,hàngTốiĐa: int, cộtTốiĐa: int, phông: str):
		self.x = viTri[0]
		self.y = viTri[1]
		self.hàngTốiĐa = hàngTốiĐa
		self.cộtTốiĐa = cộtTốiĐa
		self.kíchThước = (600/self.cộtTốiĐa , 600/self.hàngTốiĐa)
		self.maTrận = [i for i in range(cộtTốiĐa * hàngTốiĐa)]
		self.cũ = [self.maTrận[:]]
		self.len = hàngTốiĐa * cộtTốiĐa
		self.phôngChữ = phông
		self.số0 = (0, 0)
		self.ảnh = [i for i in range(cộtTốiĐa * hàngTốiĐa)]
		self.dùngNềnSố = False
		self.id = 0
#----------------------------------------------------------------------------------------

	def get(self, x: int, y: int) -> int:
		return self.maTrận[y * self.cộtTốiĐa + x]
#----------------------------------------------------------------------------------------

	def getẢnh(self, x: int, y: int) -> object:
		try:
			return self.ảnh[self.get(x, y)]
		except:
			print(f"index= {self.get(x, y)} len = {len(self.ảnh)}")
#----------------------------------------------------------------------------------------

	def set(self, x: int, y: int, giáTrị: int) -> None:
		self.maTrận[y * self.cộtTốiĐa + x] = giáTrị
#----------------------------------------------------------------------------------------

	def print(self) -> None:
		for i in range(self.hàngTốiĐa):
			for j in range(self.cộtTốiĐa):
				print(self.maTrận[i * self.cộtTốiĐa + j], end=" ")
			print()
#----------------------------------------------------------------------------------------

	def ĐảoNgẫuNhiên(self) -> None:
		self.set0();
		import random
		i = 0
		while(i < 51):
			hướng = random.choice(DiChuyển.hướng)
			hướng(self,False)
			i = i + 1;
		self.cũ = self.maTrận[:]
#----------------------------------------------------------------------------------------

	def set0(self) -> None:
		try:
			i = self.maTrận.index(0)
		except:
			print(self.maTrận)
		self.số0 = (i % self.cộtTốiĐa, i // self.cộtTốiĐa)
#----------------------------------------------------------------------------------------

	def Vẽ(self, mànHình: pygame.Surface) -> None:
		
		#Vẽ Khung
		pygame.draw.rect(mànHình, pygame.Color("black"), (self.x - 5, self.y -5,610, 610), 5)
		for x in range(self.cộtTốiĐa):
			for y in range(self.hàngTốiĐa):
				X = self.x + x * self.kíchThước[0]
				Y = self.y + y * self.kíchThước[1]
				if self.get(x, y) != 0:
					ảnhBànCờ =self.getẢnh(x, y)
					xSố = X + 10
					ySố = Y + 10
					if(self.dùngNềnSố == True):
						ảnhBànCờ = self.ảnh[-1]
						xSố = X + self.kíchThước[0]/2 - 10
						ySố = Y + self.kíchThước[1]/2 - 10
					# Vẽ ảnh
					mànHình.blit(ảnhBànCờ, pygame.Rect(X, Y, self.kíchThước[0], self.kíchThước[1]))
					# Vẽ số
					mànHình.blit(self.phôngChữ.render(f"{self.get(x, y)}", True, pygame.Color("black")),
									  (xSố, ySố))
		
		#Vẽ đường kẻ
		maxY = self.y + 600
		maxX = self.x + 600
		for x in range(1,self.cộtTốiĐa):
			for y in range(1,self.hàngTốiĐa):
				X = self.x + x * self.kíchThước[0]
				Y = self.y + y * self.kíchThước[1]
				pygame.draw.line(mànHình,pygame.Color("black") , ( X,self.y),(X,maxY), 2)
				pygame.draw.line(mànHình,pygame.Color("black") , ( self.x,Y),(maxX,Y), 2)

#----------------------------------------------------------------------------------------

	def TạoẢnh(self,đườngDẫn="big.png"):
		ảnh = []
		fullpic = pygame.image.load( đườngDẫn )
		width, height = fullpic.get_size()
		width = width/self.cộtTốiĐa
		height = height/self.hàngTốiĐa
		for y in range(self.hàngTốiĐa):
			for x in range(self.cộtTốiĐa):
				vùng = pygame.Surface((width, height))
				vùng.blit(fullpic, (0,0) , (x * width, y * height , width,height))
				vùng = pygame.transform.scale( vùng,self.kíchThước )
				vùng.set_alpha(0)
				ảnh.append (vùng)
		self.ảnh = ảnh
		self.ảnh.append(pygame.transform.scale( pygame.image.load( "number.png" ),self.kíchThước ))
		HiệuỨng.danhSách.append(([0],self.CậpNhậtHiệuỨng))
#----------------------------------------------------------------------------------------

	def LấyẢnh(self) -> None:
		
		root = tk.Tk()
		root.withdraw()
		đườngDẫn = filedialog.askopenfilename()
		if(đườngDẫn):
			self.TạoẢnh(đườngDẫn)
#----------------------------------------------------------------------------------------
	def VịTrí0(self):
		return self.số0[1] * self.cộtTốiĐa + self.số0[0]
#----------------------------------------------------------------------------------------
	
	def LấyGiáTrịMới(self,danhSách):
		for i in range(self.len):
			self.maTrận[i] = danhSách[i]
		self.set0()
#----------------------------------------------------------------------------------------

	def KhởiTạoLại(self,ngang,dọc):
		if self.ảnh[1].get_alpha() < 255:
			return
		self.hàngTốiĐa = dọc
		self.cộtTốiĐa = ngang
		self.kíchThước = (600/ngang , 600/dọc)
		self.maTrận = [i for i in range(ngang * dọc)]
		self.cũ = self.maTrận[:] 
		self.len = ngang * dọc
		self.số0 = (0, 0)
		self.TạoẢnh()
#----------------------------------------------------------------------------------------

	def CậpNhậtHiệuỨng(self,thờiGian):

		if thờiGian[0] >= 100:
			thờiGian[0] = 0
			for i in range(len(self.ảnh)-1) :
				self.ảnh[i].set_alpha(self.ảnh[i].get_alpha() + 15)
			if(self.ảnh[0].get_alpha() == 255):
				return True
		return False
		