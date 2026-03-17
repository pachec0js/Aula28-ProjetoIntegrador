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
