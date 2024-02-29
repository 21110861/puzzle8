import sys
import copy

class BộĐếm:
	def __init__(self, vịTrí, màuChữ, phông):
		self.phông = phông
		self.chữ = [ phông.render("Số bước:", True, màuChữ) , phông.render("Duyệt:", True, màuChữ)]
		self.đếm = 0
		self.tốiĐa = 0
		self.chiếmBộNhớ = 0
		self.màuChữ = màuChữ
		self.x = vịTrí[0]
		self.y = vịTrí[1]
		self.dữLiệu = ["Trống" for i in range(9)]
		self.lịchSử = [phông.render(f"{i}." + self.dữLiệu[i],True,màuChữ) for i in range(9) ]
		self.khungLịchSử = [self.lịchSử[i].get_rect(topleft=(995, 50 * i+50)) for i in range(9)]
		self.khungChữ = [ self.chữ[0].get_rect(topleft=(vịTrí[0], vịTrí[1])) ,  self.chữ[1].get_rect(topleft=(vịTrí[0], vịTrí[1]+30))]
		self.lịchSử[0] = phông.render("BƯỚC ::  DUYỆT",True,màuChữ)
		self.khungLịchSử[0] = self.lịchSử[0].get_rect(topleft=(1123, 50))
	def CậpNhật(self):
		self.đếm = 0
		self.chiếmBộNhớ = 0
		self.tốiĐa = 0
		self.chữ[0] = self.phông.render("Số bước: 0 / 0" , True, self.màuChữ)
		self.khungChữ[0] = self.chữ[0].get_rect(topleft=(self.x , self.y))
		self.chữ[1] = self.phông.render("Duyệt: 0", True, self.màuChữ)
		self.khungChữ[1] = self.chữ[1].get_rect(topleft=(self.x, self.y+30))
		
	def Tăng(self):
		self.đếm = self.đếm + 1
		self.chữ[0] = self.phông.render(f"Số bước: {self.đếm} / {self.tốiĐa}" , True, self.màuChữ)
		self.khungChữ[0] = self.chữ[0].get_rect(topleft=(self.x , self.y ))
	
	def Giảm(self):
		self.đếm = self.đếm - 1
		self.chữ[0] = self.phông.render(f"Số bước: {self.đếm} / {self.tốiĐa}" , True, self.màuChữ)
		self.khungChữ[0] = self.chữ[0].get_rect(topleft=(self.x , self.y ))
	
	def TínhBộNhớ(self,tên,vậtThể,tổngBước):
		self.tốiĐa = tổngBước
		self.chiếmBộNhớ = len(vậtThể)
		self.chữ[1] = self.phông.render(f"Duyệt: {self.chiếmBộNhớ:,}", True, self.màuChữ)
		self.khungChữ[1] = self.chữ[1].get_rect(topleft=(self.x, self.y+30))
		for i in range(8,1,-1):
			self.dữLiệu[i] = copy.deepcopy(self.dữLiệu[i-1])
		self.dữLiệu[1] = (f"{tên}: {self.tốiĐa : 06d} :: {self.chiếmBộNhớ:,}")
		
		for i in range(1,9):
			self.lịchSử[i] = self.phông.render(f"{i}.  {self.dữLiệu[i]}", True, self.màuChữ)
			self.khungLịchSử[i] = self.lịchSử[i].get_rect(topleft=(995,50*i+ 50))

			
	def Vẽ(self,scr):
		scr.blit(self.chữ[0], self.khungChữ[0])
		scr.blit(self.chữ[1], self.khungChữ[1])
		for i in range(9):
			scr.blit(self.lịchSử[i], self.khungLịchSử[i])