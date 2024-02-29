import pygame
from huongdichuyen import SangPhải , SangTrái , LênTrên , XuốngDưới

def DiChuyển( bànCờ, key : int, đảo : bool ) -> None :

	if key == pygame.K_LEFT :
		DiChuyển.hướng[ 1-đảo ] ( bànCờ,False )

	elif key == pygame.K_RIGHT :
		DiChuyển.hướng[ 0+đảo ] ( bànCờ,False )

	elif key == pygame.K_UP :
		DiChuyển.hướng[ 2 + đảo ] ( bànCờ,False )

	elif key == pygame.K_DOWN :
		DiChuyển.hướng[ 3-đảo ] ( bànCờ,False )

DiChuyển.hướng = [ SangPhải, SangTrái, LênTrên, XuốngDưới ] 
# ------------------------------------------------------------------------------------------------------


