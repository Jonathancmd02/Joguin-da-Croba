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
                velocidade_y = tamanho_quadrado
            elif evento.key == pygame.K_RIGHT:
                velocidade_x = tamanho_quadrado
                velocidade_y = 0
            elif evento.key == pygame.K_LEFT:
                velocidade_x = tamanho_quadrado
                velocidade_y = 0

    

#Atualizar a posição da cobrinha
x += velo_x
y += velo_y


#Atualizar o corpo da cobrinha
segmentos.append([x,y])
if len(segmentos) > tamanho_cobra:
    del segmentos[0]

    #Desenhar a croba
    for pixel in segmentos[:-1]:
        pygame.draw.rect(tela, verde, [] )
    
    #desenhar a comida
    pygame.draw.rect(tela, vermelho, [comida_x,comida_y,tamanho_quadrado,tamanho_quadrado])
    
    
    #desenhar score
    fonte=pygame.font.SysFont("Arial",32)
    texto=fonte.render(f"Pontuação: {tamanho_cobra-1}", True, vermelho)
    tela.blit(texto, [1,1])

    pygame.display.update()

