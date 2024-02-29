import pygame

class Nhạc:
	def __init__(self, x, y, bánKính):
		# Khởi tạo đối tượng Nhạc với các thuộc tính cơ bản
		self.center = (x, y)
		self.radius = bánKính
		self.ảnh = [
			pygame.transform.scale(pygame.image.load("onsound.png"), (30, 30)).convert_alpha(),
			pygame.transform.scale(pygame.image.load("offsound.png"), (30, 30)).convert_alpha()
		]
		self.trạngThái = 0  # Trạng thái âm thanh (Bật hoặc Tắt)
		self.chạm = False  # Trạng thái khi chuột chạm vào nút âm thanh
		self.thanhÂmLượng = pygame.Rect(self.center[0] + self.radius, self.center[1] * 0.6, 150, 15)
		self.âmLượng = pygame.Rect(self.thanhÂmLượng[0] + self.thanhÂmLượng[2] * 0.3, self.thanhÂmLượng[1] - 5, 15, 25)
		pygame.mixer.music.load("chill.mp3")
		pygame.mixer.music.play(-1)
		pygame.mixer.music.set_volume(0.3)

	def Vẽ(self, scr):
		# Vẽ đối tượng Nhạc lên màn hình
		scr.blit(self.ảnh[self.trạngThái], pygame.Rect(self.center[0] - 15, self.center[1] - 15, 30, 30))
		pygame.draw.rect(scr, pygame.Color("black"), self.thanhÂmLượng, 2)
		pygame.draw.rect(scr, pygame.Color("black"), self.âmLượng)

	def Chạm(self, pos, cóNhấpchuột):
		# Kiểm tra xem chuột có nằm trong hình tròn hay không
		distance = pygame.math.Vector2(self.center) - pygame.math.Vector2(pos)
		self.chạm = distance.length() <= self.radius

		# Xử lý sự kiện khi chuột nhấp vào nút âm thanh
		if self.chạm == True and cóNhấpchuột:
			self.trạngThái = not self.trạngThái
			if self.trạngThái:
				pygame.mixer.music.pause()
			else:
				pygame.mixer.music.unpause()

		# Xử lý sự kiện khi chuột nhấp vào thanh âm lượng
		chạm2 = self.thanhÂmLượng.collidepoint(pos)
		if chạm2 == True and cóNhấpchuột == True:
			if pos[0] <= self.thanhÂmLượng.x + self.thanhÂmLượng.width:
				độLớn = round((pos[0] - self.thanhÂmLượng.x) / self.thanhÂmLượng.width, 1)
				self.âmLượng.x = self.thanhÂmLượng.x + self.thanhÂmLượng.width * độLớn - 5
				print(độLớn)
				pygame.mixer.music.set_volume(độLớn)

		return self.chạm or chạm2

