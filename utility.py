def planta(insumo):
	if insumo == "madeira":
		plant(Entities.Bush)
	elif insumo == "cenoura":
		if get_ground_type() == Grounds.Grassland:
			till()
		plant(Entities.Carrot)
	elif insumo == "arvore":
		plant(Entities.Tree)
	elif insumo == "abobora":
		if get_ground_type() == Grounds.Grassland:
			till()
		plant(Entities.Pumpkin)
	elif insumo == "grama":
		plant(Entities.Grass)
	
	
def colhe():
	if can_harvest():
		harvest()
		
def mov_direita(y,x):
	if get_pos_y() == y and get_pos_x() == x:
		move(East)
		
		
def agua_solo():
	if get_water() < 0.65:
		use_item(Items.Water)
	else:
		pass

		
def centralizar():
	y = get_pos_y()
	x = get_pos_x()
	if y > 0:
		for cont in range(y):
			move(South)
	if x > 0:
		for cont in range(x):
			move(West)
	