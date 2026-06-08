# Mission Control AI
# Global Solution 2026.1
# Pensamento Computacional e Automação com Python

nome_missao = "Orion Control Alpha"
nome_equipe = "ORION Control IA"

dados_missao = [
    [24, 92, 88, 96, 90],
    [27, 80, 72, 94, 85],
    [31, 65, 58, 91, 70],
    [36, 42, 38, 87, 55],
    [39, 28, 19, 78, 35],
    [34, 55, 32, 82, 50]
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]


def analisar_temperatura(temperatura):
    if temperatura < 18:
        return "ATENÇÃO", 1, "Temperatura abaixo do ideal"
    elif temperatura <= 30:
        return "NORMAL", 0, "Temperatura estável"
    elif temperatura <= 35:
        return "ATENÇÃO", 1, "Temperatura elevada"
    else:
        return "CRÍTICO", 2, "Risco de superaquecimento"


def analisar_comunicacao(comunicacao):
    if comunicacao < 30:
        return "CRÍTICO", 2, "Comunicação com a base em nível crítico"
    elif comunicacao < 60:
        return "ATENÇÃO", 1, "Comunicação instável"
    else:
        return "NORMAL", 0, "Comunicação estável"


def analisar_bateria(bateria):
    if bateria < 20:
        return "CRÍTICO", 2, "Bateria em nível crítico"
    elif bateria < 50:
        return "ATENÇÃO", 1, "Bateria abaixo do recomendado"
    else:
        return "NORMAL", 0, "Energia estável"


def analisar_oxigenio(oxigenio):
    if oxigenio < 80:
        return "CRÍTICO", 2, "Oxigênio em nível crítico"
    elif oxigenio < 90:
        return "ATENÇÃO", 1, "Oxigênio abaixo do ideal"
    else:
        return "NORMAL", 0, "Oxigênio adequado"


def analisar_estabilidade(estabilidade):
    if estabilidade < 40:
        return "CRÍTICO", 2, "Estabilidade operacional crítica"
    elif estabilidade < 70:
        return "ATENÇÃO", 1, "Estabilidade operacional reduzida"
    else:
        return "NORMAL", 0, "Estabilidade operacional adequada"


def classificar_ciclo(pontuacao):
    if pontuacao <= 2:
        return "MISSÃO ESTÁVEL"
    elif pontuacao <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


def gerar_recomendacao(classificacoes):
    if "CRÍTICO" in classificacoes:
        return "Ativar modo de segurança e priorizar os sistemas críticos."
    elif "ATENÇÃO" in classificacoes:
        return "Monitorar sistemas em atenção e preparar plano de contingência."
    else:
        return "Manter operação normal e continuar monitoramento."


def analisar_tendencia(riscos):
    primeiro = riscos[0]
    ultimo = riscos[-1]

    if ultimo > primeiro:
        return "A missão apresentou tendência de piora."
    elif ultimo < primeiro:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável em relação ao início."


def identificar_area_mais_afetada(risco_por_area):
    maior_risco = max(risco_por_area)
    posicao = risco_por_area.index(maior_risco)
    return areas_monitoradas[posicao]


def gerar_relatorio_final(riscos, risco_por_area):
    quantidade_ciclos = len(dados_missao)

    soma_temperatura = 0
    soma_comunicacao = 0
    soma_bateria = 0
    soma_oxigenio = 0
    soma_estabilidade = 0

    for ciclo in dados_missao:
        soma_temperatura += ciclo[0]
        soma_comunicacao += ciclo[1]
        soma_bateria += ciclo[2]
        soma_oxigenio += ciclo[3]
        soma_estabilidade += ciclo[4]

    media_temperatura = soma_temperatura / quantidade_ciclos
    media_comunicacao = soma_comunicacao / quantidade_ciclos
    media_bateria = soma_bateria / quantidade_ciclos
    media_oxigenio = soma_oxigenio / quantidade_ciclos
    media_estabilidade = soma_estabilidade / quantidade_ciclos

    maior_risco = max(riscos)
    ciclo_mais_critico = riscos.index(maior_risco) + 1
    risco_medio = sum(riscos) / quantidade_ciclos

    ciclos_criticos = 0
    for risco in riscos:
        if risco >= 6:
            ciclos_criticos += 1

    tendencia = analisar_tendencia(riscos)
    area_mais_afetada = identificar_area_mais_afetada(risco_por_area)
    classificacao_final = classificar_ciclo(round(risco_medio))

    print("=" * 60)
    print("RELATÓRIO FINAL DA MISSÃO")
    print("=" * 60)
    print(f"Missão: {nome_missao}")
    print(f"Equipe: {nome_equipe}")
    print(f"Quantidade de ciclos analisados: {quantidade_ciclos}")
    print(f"Média de temperatura: {media_temperatura:.2f} °C")
    print(f"Média de comunicação: {media_comunicacao:.2f}%")
    print(f"Média de bateria: {media_bateria:.2f}%")
    print(f"Média de oxigênio: {media_oxigenio:.2f}%")
    print(f"Média de estabilidade: {media_estabilidade:.2f}%")
    print(f"Ciclo mais crítico: Ciclo {ciclo_mais_critico}")
    print(f"Maior pontuação de risco: {maior_risco}")
    print(f"Risco médio da missão: {risco_medio:.2f}")
    print(f"Quantidade de ciclos críticos: {ciclos_criticos}")
    print()
    print("Tendência da missão:")
    print(tendencia)
    print()
    print("Pontuação acumulada por área:")

    for i in range(len(areas_monitoradas)):
        print(f"{areas_monitoradas[i]}: {risco_por_area[i]} pontos")

    print()
    print("Área mais afetada:")
    print(area_mais_afetada)
    print()
    print("Classificação final da missão:")
    print(classificacao_final)
    print()
    print("Conclusão:")

    if classificacao_final == "MISSÃO ESTÁVEL":
        print("A missão apresentou bom desempenho geral e pode continuar em operação normal.")
    elif classificacao_final == "MISSÃO EM ATENÇÃO":
        print("A missão apresentou instabilidade em alguns sistemas e exige monitoramento constante.")
    else:
        print("A missão apresentou risco elevado e deve ativar protocolos de emergência.")


def executar_sistema():
    riscos = []
    risco_por_area = [0, 0, 0, 0, 0]

    print("=" * 60)
    print("MISSION CONTROL AI")
    print("=" * 60)
    print(f"Missão: {nome_missao}")
    print(f"Equipe: {nome_equipe}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print("=" * 60)

    for numero_ciclo in range(len(dados_missao)):
        ciclo = dados_missao[numero_ciclo]

        temperatura = ciclo[0]
        comunicacao = ciclo[1]
        bateria = ciclo[2]
        oxigenio = ciclo[3]
        estabilidade = ciclo[4]

        status_temp, risco_temp, msg_temp = analisar_temperatura(temperatura)
        status_com, risco_com, msg_com = analisar_comunicacao(comunicacao)
        status_bat, risco_bat, msg_bat = analisar_bateria(bateria)
        status_oxi, risco_oxi, msg_oxi = analisar_oxigenio(oxigenio)
        status_est, risco_est, msg_est = analisar_estabilidade(estabilidade)

        pontuacao_total = risco_temp + risco_com + risco_bat + risco_oxi + risco_est
        classificacao = classificar_ciclo(pontuacao_total)

        classificacoes = [status_temp, status_com, status_bat, status_oxi, status_est]
        recomendacao = gerar_recomendacao(classificacoes)

        riscos.append(pontuacao_total)

        risco_por_area[0] += risco_temp
        risco_por_area[1] += risco_com
        risco_por_area[2] += risco_bat
        risco_por_area[3] += risco_oxi
        risco_por_area[4] += risco_est

        print()
        print(f"CICLO {numero_ciclo + 1}")
        print("-" * 60)
        print(f"Temperatura: {temperatura} °C | {status_temp} | {msg_temp}")
        print(f"Comunicação: {comunicacao}% | {status_com} | {msg_com}")
        print(f"Bateria: {bateria}% | {status_bat} | {msg_bat}")
        print(f"Oxigênio: {oxigenio}% | {status_oxi} | {msg_oxi}")
        print(f"Estabilidade: {estabilidade}% | {status_est} | {msg_est}")
        print(f"Pontuação de risco do ciclo: {pontuacao_total}")
        print(f"Classificação do ciclo: {classificacao}")
        print(f"Recomendação: {recomendacao}")

    print()
    gerar_relatorio_final(riscos, risco_por_area)


executar_sistema()