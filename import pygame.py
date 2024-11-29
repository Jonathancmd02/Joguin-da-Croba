import pygame
import random

#Iniciar o pygame
pygame.init()

pygame.display.set_caption("O Terrível Cobroso")
LARGURA, ALTURA=1200, 800
tela=pygame.display.set_mode((LARGURA, ALTURA))

relogio=pygame.time.Clock()

#Cores RGB
preta=(0,0,0)
branco=(255,255,255)
vermelho=(255,0,0)
verde=(0,255,0)
azul=(0,0,255)

tamanho_quadrado=20

#FPS do Jogo
velo_jogo= 3

#Gera a comida inicial
comida_x=round(random.randrange(0, LARGURA-tamanho_quadrado)/float(tamanho_quadrado))*float(tamanho_quadrado)
comida_y=round(random.randrange(0, ALTURA-tamanho_quadrado)/float(tamanho_quadrado))*float(tamanho_quadrado)

#posição inicial da cabeça da cobra
x=LARGURA/2
y=ALTURA/2

velo_x=0
velo_y=0

#comprimento da cobra
tamanho_cobra= 1
#corpo da cobra
segmentos=[]

sair=False

while not sair:
    #Criando a tela do jogo
    tela.fill(azul)

    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            fim_jogo= True
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_DOWN:
                velocidade_x = 0
                velocidade_y = tamanho_quadrado
            elif evento.key == pygame.K_UP:
                velocidade_x = 0
                velocidade_y = -tamanho_quadrado
            elif evento.key == pygame.K_RIGHT:
                velocidade_x = tamanho_quadrado
                velocidade_y = 0
            elif evento.key == pygame.K_LEFT:
                velocidade_x = -tamanho_quadrado
                velocidade_y = 0

    

#Atualizar a posição da cobrinha
x += velo_x
y += velo_y


#Atualizar o corpo da cobrinha
segmentos.append([x,y])
if len(segmentos) > tamanho_cobra:
    del segmentos[0]

#Verificar colisão com o próprio corpo
for lista in segmentos[:-1]:
    if lista == [x,y]:
        fim_jogo = True

#Verificar colisão na parede
if x < 0 or x>= LARGURA or y < 0 or y >= ALTURA:
    fim_jogo = True
    #Desenhar a croba
    for pixel in segmentos[:-1]:
        pygame.draw.rect(tela, verde, [] )

#Game Over
# Função para exibir a tela de "Game Over"
def exibir_game_over():
    tela.fill(preto)  # Preencher a tela com a cor preta

    # Criar o texto de "Game Over"
    texto_game_over = fonte.render("Game Over", True, vermelho)
    texto_rect = texto_game_over.get_rect(center=(largura//2, altura//3))
    tela.blit(texto_game_over, texto_rect)

    # Exibir a opção para reiniciar ou sair
    texto_reiniciar = fonte.render("Pressione R para Reiniciar", True, branco)
    texto_reiniciar_rect = texto_reiniciar.get_rect(center=(largura//2, altura//2))
    tela.blit(texto_reiniciar, texto_reiniciar_rect)

    texto_sair = fonte.render("Pressione Q para Sair", True, branco)
    texto_sair_rect = texto_sair.get_rect(center=(largura//2, altura//1.5))
    tela.blit(texto_sair, texto_sair_rect)

    pygame.display.update()

# Função para reiniciar o jogo
def reiniciar_jogo():
    # Resetar variáveis e elementos do jogo para o início
    pass

# Loop principal do jogo
def loop_jogo():
    # Variável para controlar o estado do jogo
    jogo_ativo = True

    while jogo_ativo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_q:  # Se pressionar Q, sai do jogo
                    pygame.quit()
                    sys.exit()
                if evento.key == pygame.K_r:  # Se pressionar R, reinicia o jogo
                    reiniciar_jogo()
                    jogo_ativo = True  # Reinicia o loop
    
    #desenhar a comida
    pygame.draw.rect(tela, vermelho, [comida_x,comida_y,tamanho_quadrado,tamanho_quadrado])
    
    
    #desenhar score
    fonte=pygame.font.SysFont("Arial",32)
    texto=fonte.render(f"Pontuação: {tamanho_cobra-1}", True, vermelho)
    tela.blit(texto, [1,1])

    pygame.display.update()

#Verificar se a cobrinha comeu a comida
    if x == comida_x and y == comida_y:
        tamanho_cobra += 1
        comida_x=round(random.randrange(0, LARGURA-tamanho_quadrado)/float(tamanho_quadrado))*float(tamanho_quadrado)
        comida_y=round(random.randrange(0, ALTURA-tamanho_quadrado)/float(tamanho_quadrado))*float(tamanho_quadrado)
        

    relogio.tick(velo_jogo)