# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
import time

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
WIDTH = 480
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Navinha')

# ----- Inicia assets
METEOR_WIDTH = 50
METEOR_HEIGHT = 38
SHIP_WIDTH = 50
SHIP_HEIGHT = 38
assets = {}
assets['background'] = pygame.image.load('assets/img/starfield.png').convert()
assets['meteor_img'] = pygame.image.load('assets/img/meteorBrown_med1.png').convert_alpha()
assets['meteor_img'] = pygame.transform.scale(assets['meteor_img'], (METEOR_WIDTH, METEOR_HEIGHT))
assets['ship_img'] = pygame.image.load('assets/img/playerShip1_orange.png').convert_alpha()
assets['ship_img'] = pygame.transform.scale(assets['ship_img'], (SHIP_WIDTH, SHIP_HEIGHT))
assets['bullet_img'] = pygame.image.load('assets/img/laserRed16.png').convert_alpha()

# Carrega os sons do jogo
pygame.mixer.music.load('assets/snd/tgfcoder-FrozenJam-SeamlessLoop.ogg')
pygame.mixer.music.set_volume(0.4)
assets['boom_sound'] = pygame.mixer.Sound('assets/snd/expl3.wav')
assets['destroy_sound'] = pygame.mixer.Sound('assets/snd/expl6.wav')
assets['pew_sound'] = pygame.mixer.Sound('assets/snd/pew.wav')

# ----- Inicia estruturas de dados
# Definindo os novos tipos
class Ship(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['ship_img']
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.groups = groups
        self.assets = assets

    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        # A nova bala vai ser criada logo acima e no centro horizontal da nave
        new_bullet = Bullet(self.assets, self.rect.top, self.rect.centerx)
        self.groups['all_sprites'].add(new_bullet)
        self.groups['all_bullets'].add(new_bullet)
        self.assets['pew_sound'].play()

class Meteor(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['meteor_img']
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-METEOR_WIDTH)
        self.rect.y = random.randint(-100, -METEOR_HEIGHT)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9)

    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH-METEOR_WIDTH)
            self.rect.y = random.randint(-100, -METEOR_HEIGHT)
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(2, 9)

# Classe Bullet que representa os tiros
class Bullet(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, assets, bottom, centerx):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['bullet_img']
        self.rect = self.image.get_rect()

        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedy = -10  # Velocidade fixa para cima

    def update(self):
        # A bala só se move no eixo y
        self.rect.y += self.speedy

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()

game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30

# Criando um grupo de meteoros
all_sprites = pygame.sprite.Group()
all_meteors = pygame.sprite.Group()
all_bullets = pygame.sprite.Group()
groups = {}
groups['all_sprites'] = all_sprites
groups['all_meteors'] = all_meteors
groups['all_bullets'] = all_bullets

# Criando o jogador
player = Ship(groups, assets)
all_sprites.add(player)
# Criando os meteoros
for i in range(8):
    meteor = Meteor(assets)
    all_sprites.add(meteor)
    all_meteors.add(meteor)

# ===== Loop principal =====
pygame.mixer.music.play(loops=-1)
while game:
    clock.tick(FPS)

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx -= 8
            if event.key == pygame.K_RIGHT:
                player.speedx += 8
            if event.key == pygame.K_SPACE:
                player.shoot()
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx += 8
            if event.key == pygame.K_RIGHT:
                player.speedx -= 8

    # ----- Atualiza estado do jogo
    # Atualizando a posição dos meteoros
    all_sprites.update()

    # Verifica se houve colisão entre tiro e meteoro
    hits = pygame.sprite.groupcollide(all_meteors, all_bullets, True, True)
    for meteor in hits: # As chaves são os elementos do primeiro grupo (meteoros) que colidiram com alguma bala
        # O meteoro e destruido e precisa ser recriado
        assets['destroy_sound'].play()
        m = Meteor(assets)
        all_sprites.add(m)
        all_meteors.add(m)

    # Verifica se houve colisão entre nave e meteoro
    hits = pygame.sprite.spritecollide(player, all_meteors, True)
    if len(hits) > 0:
        # Toca o som da colisão
        assets['boom_sound'].play()
        time.sleep(1) # Precisa esperar senão fecha

        game = False

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(assets['background'], (0, 0))
    # Desenhando meteoros
    all_sprites.draw(window)

    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

