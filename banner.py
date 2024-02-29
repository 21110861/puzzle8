class Banner:
	def __init__(self,x,y, chieuNgangPM,chữ,màu,phông):
		self.chữ = phông.render(chữ, True, màu)
		self.bắtĐầu = -self.chữ.get_rect().width
		self.kếtThúc = max(chieuNgangPM,-self.bắtĐầu)
		self.x1 = x + self.bắtĐầu
		self.x2 = x
		self.y = y
		
	def Vẽ(self,mànHình):
		mànHình.blit(self.chữ,(self.x1,self.y))
		mànHình.blit(self.chữ,(self.x2,self.y))
		
	def CậpNhật(self):
		self.x1 += 0.4
		if(self.x1 > self.kếtThúc):
			self.x1 = self.bắtĐầu
		
		self.x2 += 0.4
		if(self.x2 > self.kếtThúc):
			self.x2 = self.bắtĐầu