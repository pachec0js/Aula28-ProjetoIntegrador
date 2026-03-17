def obter_melhor_aluno(alunos_processados):
    if len(alunos_processados) == 0:
        return None

    melhor_aluno = alunos_processados[0]

    for aluno in alunos_processados:
        if aluno["media"] > melhor_aluno["media"]:
            melhor_aluno = aluno

    return melhor_aluno
