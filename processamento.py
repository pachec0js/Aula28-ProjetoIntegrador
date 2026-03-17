def calcular_media(notas):
    soma = 0

    for nota in notas:
        soma += nota

    media = soma / len(notas)
    return media

def processar_alunos(alunos):
    alunos_processados = []
    alunos_inconsistentes = []

    for nome in alunos:
        if not isinstance(notas, list) or len(notas) == 0:
            alunos_inconsistentes.append(nome)
            continue

        notas_validas = True

        for nota in notas:
            if not isinstance(nota, (int, float)):
                notas_validas = False
                break

        if notas_validas:
            media = calcular_media(notas)

            alunos_processados.append({
                "nome": nome,
                "media": media
            })
        else:
            alunos_inconsistentes.append(nome)

    return alunos_processados, alunos_inconsistentes
  
  
  def filtrar_recuperacao(alunos_processados):
    alunos_recuperacao = []
    for aluno in alunos_processados:
        if aluno['media'] < 7:
            alunos_recuperacao.append(aluno)
    return alunos_recuperacao
