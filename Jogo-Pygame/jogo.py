import pygame as pyg
import random
import time

# Inicializa o Pygame
pyg.init()

# Configurações da tela
largura = 1200
altura = 650
tela = pyg.display.set_mode((largura, altura))
pyg.display.set_caption("Pegue o Quadrado")

# Cores usadas nas imagens
vermelho = (252, 3, 115)
roxo = (169, 62, 250)
preto = (3, 3, 3)
Azul_escuro = (252, 252, 252)
cinza = (100, 100, 100)
azul = (50, 150, 255)

# Fonte
fonte = pyg.font.Font(None, 30)
# Para contagem regressiva
fonte_grande = pyg.font.Font("C:/Windows/Fonts/BRUSHSCI.TTF", 120)  

# Função para desenhar texto centralizado
def desenhar_texto(texto, fonte, cor, x, y):
    imagem = fonte.render(texto, True, cor)
    rect = imagem.get_rect(center=(x, y))
    tela.blit(imagem, rect)

# Função principal do jogo
def jogar(recorde_atual):
    jogador_tamanho = 45
    jogador_x = largura // 2
    jogador_y = altura // 2
    velocidade = 20

    alvo_tamanho = 25
    alvo_x = random.randint(0, largura - alvo_tamanho)
    alvo_y = random.randint(0, altura - alvo_tamanho)

    pontos = 0
    tempo_total = 20

    # --- Contagem regressiva ---
    for i in range(3, 0, -1):
        tela.fill(preto)
        desenhar_texto(str(i), fonte_grande, Azul_escuro, largura // 2, altura // 2)
        pyg.display.update()
        time.sleep(1)

    inicio = time.time()
    rodando = True
    bateu_borda = False  # controle da penalidade

    while rodando:
        pyg.time.delay(30)
        for evento in pyg.event.get():
            if evento.type == pyg.QUIT:
                return recorde_atual, pontos, False

        # Movimento
        teclas = pyg.key.get_pressed()
        if teclas[pyg.K_LEFT] and jogador_x > 0:
            jogador_x -= velocidade
        if teclas[pyg.K_RIGHT] and jogador_x < largura - jogador_tamanho:
            jogador_x += velocidade
        if teclas[pyg.K_UP] and jogador_y > 0:
            jogador_y -= velocidade
        if teclas[pyg.K_DOWN] and jogador_y < altura - jogador_tamanho:
            jogador_y += velocidade

        # Penalidade ao encostar na borda
        encostou = (
            jogador_x <= 0 or 
            jogador_x >= largura - jogador_tamanho or
            jogador_y <= 0 or 
            jogador_y >= altura - jogador_tamanho
        )

        if encostou and not bateu_borda:
            pontos -= 2
            if pontos < 0:
                pontos = 0
            bateu_borda = True
        elif not encostou:
            bateu_borda = False

        # Colisão com o alvo
        if (jogador_x < alvo_x + alvo_tamanho and
            jogador_x + jogador_tamanho > alvo_x and
            jogador_y < alvo_y + alvo_tamanho and
            jogador_y + jogador_tamanho > alvo_y):
            pontos += 1
            alvo_x = random.randint(0, largura - alvo_tamanho)
            alvo_y = random.randint(0, altura - alvo_tamanho)

        # Tempo
        tempo_restante = tempo_total - int(time.time() - inicio)
        if tempo_restante <= 0:
            rodando = False

        # Desenho
        tela.fill(preto)
        pyg.draw.rect(tela, vermelho, (jogador_x, jogador_y, jogador_tamanho, jogador_tamanho))
        pyg.draw.rect(tela, roxo, (alvo_x, alvo_y, alvo_tamanho, alvo_tamanho))

        desenhar_texto(f"Pontos: {pontos}", fonte, Azul_escuro, 70, 15)
        desenhar_texto(f"Tempo: {tempo_restante}", fonte, Azul_escuro, 70, 37)
        desenhar_texto(f"Recorde: {recorde_atual}", fonte, Azul_escuro, 80, 57)

        pyg.display.update()

    # Atualiza recorde
    if pontos > recorde_atual:
        recorde_atual = pontos

    return recorde_atual, pontos, True

# Função da tela final
def tela_final(pontos, recorde):
    while True:
        tela.fill(preto)
        desenhar_texto("Fim de jogo!", fonte_grande, azul, largura // 2, altura // 2 - 80)
        desenhar_texto(f"Pontos da partida: {pontos}", fonte, Azul_escuro, largura // 2, altura // 2 - 30)
        desenhar_texto(f"Recorde: {recorde}", fonte, Azul_escuro, largura // 2, altura // 2 + 10)

        botao_rect = pyg.Rect(largura // 2 - 100, altura // 2 + 60, 200, 60)
        pyg.draw.rect(tela, cinza, botao_rect)
        desenhar_texto("Jogar Novamente", fonte, Azul_escuro, largura // 2, altura // 2 + 90)

        pyg.display.update()

        for evento in pyg.event.get():
            if evento.type == pyg.QUIT:
                return False
            if evento.type == pyg.MOUSEBUTTONDOWN and evento.button == 1:
                if botao_rect.collidepoint(evento.pos):
                    return True

# Loop principal
recorde = 0
rodando = True
while rodando:
    recorde, pontos_rodada, terminou = jogar(recorde)
    if not terminou:
        rodando = False
        break
    rodando = tela_final(pontos_rodada, recorde)

pyg.quit()