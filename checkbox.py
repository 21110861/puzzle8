import pygame
class CheckBox:
	def __init__(self, x, y,width, height, text, color=(0, 255, 0), font=None):
		self.rect = pygame.Rect(x, y, width, height)
		self.text = font.render(text, True, color)
		self.text_rect = self.text.get_rect()
		self.text_rect.midleft = (self.rect.right + 10, self.rect.centery)
		self.color = color
		self.checked = False

	def Vẽ(self, screen):
		# Vẽ khung CheckBox
		pygame.draw.rect(screen, self.color, self.rect, 2)

		# Vẽ vị trí đánh dấu nếu được chọn
		if self.checked:
			pygame.draw.line(screen, pygame.Color("lime"), (self.rect.left + 5, self.rect.centery), (self.rect.left + self.rect.width // 3, self.rect.bottom - 5), 3)
			pygame.draw.line(screen, pygame.Color("lime"), (self.rect.left + self.rect.width // 3, self.rect.bottom - 5), (self.rect.right - 5, self.rect.top + 5), 3)


		# Vẽ văn bản
		# text_surface = self.font.render(self.text, True, self.color)
		# text_rect = text_surface.get_rect()
		# text_rect.midleft = (self.rect.right + 10, self.rect.centery)
		screen.blit(self.text, self.text_rect)

	def Nhấn(self,cóChạmNút):
		if self.rect.collidepoint(pygame.mouse.get_pos()) and cóChạmNút:
			self.checked = not self.checked
		return self.checked
			
