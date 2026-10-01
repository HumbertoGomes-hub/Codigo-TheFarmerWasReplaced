import utility


def sobe(x,insumo_sobe,y = 7): 
	while get_pos_y() < y and get_pos_x() == x:
		utility.colhe()
		utility.planta(insumo_sobe)
		utility.agua_solo()
			
		move(North)
		if get_pos_y() == y and get_pos_x() == x: 
			utility.colhe()
			utility.planta(insumo_sobe)
			utility.agua_solo()
			
	
def desce(x,insumo_desce, y = 0):
	while get_pos_y() > y and get_pos_x() == x:
		utility.colhe()
		utility.planta(insumo_desce)
		utility.agua_solo()
		
		move(South)
		if get_pos_y() == y and get_pos_x() == x:
			utility.colhe()
			utility.planta(insumo_desce)
			utility.agua_solo()
			
	
		
		
