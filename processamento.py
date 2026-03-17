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
  

  def obter_melhor_aluno(alunos_processados):
    if len(alunos_processados) == 0:
        return None

    melhor_aluno = alunos_processados[0]

    for aluno in alunos_processados:
        if aluno["media"] > melhor_aluno["media"]:
            melhor_aluno = aluno

    return melhor_aluno

  
  def gerar_relatorio(alunos_processados, alunos_recuperacao, top_student, alunos_inconsistentes):
    relatorio = "=== RELATÓRIO FINAL DE DESEMPENHO ACADÊMICO ===\n\n"

    relatorio += "ALUNOS PROCESSADOS:\n"
    for aluno in alunos_processados:
        relatorio += f'{aluno["nome"]}: média {aluno["media"]:.2f}\n'

    relatorio += "\nALUNOS EM RECUPERAÇÃO:\n"
    if len(alunos_recuperacao) == 0:
        relatorio += "Nenhum aluno em recuperação.\n"
    else:
        for aluno in alunos_recuperacao:
            relatorio += f'{aluno["nome"]}: média {aluno["media"]:.2f}\n'

    relatorio += "\nTOP STUDENT:\n"
    if top_student is None:
        relatorio += "Nenhum aluno válido para ranking.\n"
    else:
        relatorio += f'{top_student["nome"]}: média {top_student["media"]:.2f}\n'

    relatorio += "\nALUNOS COM INCONSISTÊNCIA DE DADOS:\n"
    if len(alunos_inconsistentes) == 0:
        relatorio += "Nenhum aluno com inconsistência.\n"
    else:
        for nome in alunos_inconsistentes:
            relatorio += f"{nome}\n"

    return relatorio