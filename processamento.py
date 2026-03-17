def filtrar_recuperacao(alunos_processados):
    alunos_recuperacao = []
    for aluno in alunos_processados:
        if aluno['media'] < 7:
            alunos_recuperacao.append(aluno)
    return alunos_recuperacao
    