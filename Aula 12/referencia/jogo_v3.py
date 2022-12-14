# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Hello World!')

# ----- Inicia estruturas de dados
game = True

# ----- Inicia assets
font = pygame.font.SysFont(None, 48)
fortaleza_text = font.render('FORTALEZA', True, (255, 0, 0))
esporte_text = font.render('ESPORTE', True, (0, 0, 255))
clube_text = font.render('CLUBE', True, (255, 255, 255))

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(fortaleza_text, (10, 10))
    window.blit(esporte_text, (10, 50))
    window.blit(clube_text, (10, 90))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

