import pygame
class NútBé:

	def __init__(self, vịTrí, kíchThước, tiêuĐề, màuNền, màuChữ, phông):
		self.khung = pygame.Rect(vịTrí[0], vịTrí[1], kíchThước[0], kíchThước[1])
		self.chữ = phông.render(tiêuĐề, True, màuChữ)
		self.màuNền = màuNền
		self.màuChữ = màuChữ
		self.khungChữ = phông.render(tiêuĐề, True, màuChữ).get_rect(center=(vịTrí[0] + kíchThước[0] // 2, vịTrí[1] + kíchThước[1] // 2))

	def Vẽ(self,scr):
		pygame.draw.rect(scr, self.màuNền, self.khung)
		scr.blit(self.chữ, self.khungChữ)
		

	def Chạm(self,pos):
		return self.khung.collidepoint(pos)