import pygame
from nutbe import NútBé
from nut import Nút
class Number:
	def __init__(self,vịTrí,ngang,dọc , phông):
		self.vịTrí = vịTrí
		self.phông = phông
		self.ngang = ngang
		self.dọc = dọc
		self.nút = [
			NútBé((vịTrí[0] + 130,vịTrí[1]),(20,20),"+",pygame.Color("green"),pygame.Color("white"),phông),
			NútBé((vịTrí[0] + 130,vịTrí[1]+25),(20,20),"-",pygame.Color("red"),pygame.Color("white"),phông),
			NútBé((vịTrí[0] + 130,vịTrí[1]+50),(20,20),"+",pygame.Color("green"),pygame.Color("white"),phông),
			NútBé((vịTrí[0] + 130,vịTrí[1]+75),(20,20),"-",pygame.Color("red"),pygame.Color("white"),phông),
			Nút((vịTrí[0] + 160,vịTrí[1]+25),(150,50),"xác nhận",pygame.Color("orange"),pygame.Color("black"),phông,1.1)

		]
	def Chạm(self,pos,cóNhấpChuột):
		i = 0
		if(self.nút[i].Chạm(pos) == True and cóNhấpChuột):
			if self.ngang < 6 :
				self.ngang += 1
			return False
		i += 1
		if(self.nút[i].Chạm(pos) == True and cóNhấpChuột):
			if self.ngang > 2 :
				self.ngang -= 1
			return False
		i += 1
		if(self.nút[i].Chạm(pos) == True and cóNhấpChuột):
			if self.dọc < 6 :
				self.dọc += 1
			return False
		i += 1
		if(self.nút[i].Chạm(pos) == True and cóNhấpChuột):
			if self.dọc > 2: 
				self.dọc -= 1
			return False
		i += 1
		if(self.nút[i].Chạm(pos) == True and cóNhấpChuột):
			return True
		return False
		
	def Vẽ(self,src):
		src.blit(self.phông.render(f"Ngang: {self.ngang}", True, pygame.Color("black")),self.vịTrí)
		src.blit(self.phông.render(f"Dọc: {self.dọc}", True, pygame.Color("black")),(self.vịTrí[0],self.vịTrí[1] +55))
		for i in self. nút:
			i.Vẽ(src)