nivel_fa = 0

assistiu = input("Já assistiu todos os filmes?")
if(assistiu.lower() == "sim"): nivel_fa += 1

tem_camiseta = input("Tem camiseta temática?")
if(tem_camiseta.lower() == "sim"): nivel_fa += 1

ja_fantasiou = input("Já se fantasiou de algum personagem?")
if(ja_fantasiou.lower() == "sim"): nivel_fa += 1

tem_action_figure = input("Tem algum action figure/nave/etc?")
if(tem_action_figure.lower() == "sim"): nivel_fa += 1

foi_parque = input("Já foi no Galaxy's Edge, o parque temático da franquia?")
if(foi_parque.lower() == "sim"): nivel_fa += 1

if(nivel_fa < 2): print("Inocente")
elif(nivel_fa == 2): print("Padawan")
elif(nivel_fa <= 4): print("Jedi")
else: print("One with the Force")