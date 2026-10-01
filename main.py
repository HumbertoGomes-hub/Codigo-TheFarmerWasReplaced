import utility
import mega


utility.centralizar()
do_a_flip()
change_hat(Hats.Purple_Hat)
pet_the_piggy()

while True:
	mega.sobe(0,"cenoura")
	utility.mov_direita(get_pos_y(),get_pos_x())
	
	mega.desce(1,"madeira")
	utility.mov_direita(get_pos_y(),get_pos_x())
	
	mega.sobe(2,"arvore")
	utility.mov_direita(get_pos_y(),get_pos_x())
	
	mega.desce(3,"arvore")
	utility.mov_direita(get_pos_y(),get_pos_x())
	
	mega.sobe(4,"arvore")
	utility.mov_direita(get_pos_y(),get_pos_x())
	
	mega.desce(5,"abobora",4)
	mega.desce(5,"grama")
	utility.mov_direita(get_pos_y(),get_pos_x())
	
	mega.sobe(6,"grama",4)
	mega.sobe(6,"abobora")
	utility.mov_direita(get_pos_y(),get_pos_x())
	
	mega.desce(7,"grama")
	utility.centralizar()
	


	
