import pygame

class Nút:
	def __init__(self, vịTrí, kíchThước, tiêuĐề, màuNền, màuChữ, phông, phóngTo=1.3, đườngDẫn="khungnut.png"):
		# Khởi tạo đối tượng Nút với các thuộc tính cơ bản
		self.khung = pygame.Rect(vịTrí[0], vịTrí[1], kíchThước[0], kíchThước[1])
		self.chữ = phông.render(tiêuĐề, True, màuChữ)
		self.màuNền = màuNền
		self.màuChữ = màuChữ
		self.khungChữ = phông.render(tiêuĐề, True, màuChữ).get_rect(center=(vịTrí[0] + kíchThước[0] // 2, vịTrí[1] + kíchThước[1] // 2))
		self.khungNút = pygame.image.load(đườngDẫn)
		self.khungNút = pygame.transform.scale(self.khungNút, (kíchThước[0] + 4, kíchThước[1] + 8))
		self.chạm = False
		self.phóngTo = phóngTo

	def Vẽ(self, scr):
		# Vẽ đối tượng Nút lên màn hình
		if self.chạm:
			# Phóng to Nút khi chuột chạm vào
			scaled_width = int(self.khung.width * self.phóngTo)
			scaled_height = int(self.khung.height * self.phóngTo)
			scaled_khung = pygame.Rect(
				self.khung.x - (scaled_width - self.khung.width) // 2,
				self.khung.y - (scaled_height - self.khung.height) // 2,
				scaled_width,
				scaled_height
			)
			pygame.draw.rect(scr, self.màuNền, scaled_khung)
			khung_chữ = self.chữ.get_rect(center=scaled_khung.center)
			scaled_khung_nút = pygame.transform.scale(self.khungNút, (scaled_width + 4, scaled_height + 8))
			scr.blit(self.chữ, khung_chữ)
			scr.blit(scaled_khung_nút, (scaled_khung.x - 2, scaled_khung.y, scaled_khung.width, scaled_khung.height))
		else:
			# Vẽ Nút khi không có sự chạm
			pygame.draw.rect(scr, self.màuNền, self.khung)
			scr.blit(self.chữ, self.khungChữ)
			scr.blit(self.khungNút, (self.khung.x - 2, self.khung.y, self.khung.width, self.khung.height))

	def Chạm(self, pos):
		# Kiểm tra xem chuột có nằm trong Nút hay không
		self.chạm = self.khung.collidepoint(pos)
		return self.chạm

# Khởi tạo đối tượng Nút âm thanh
Nút.âmThanh = None
