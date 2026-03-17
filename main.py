from dados import alunos
from processamento import processar_alunos, filtrar_recuperacao, obter_melhor_aluno, gerar_relatorio


def main():
    alunos_processados, alunos_inconsistentes = processar_alunos(alunos)
    alunos_recuperacao = filtrar_recuperacao(alunos_processados)
    top_student = obter_melhor_aluno(alunos_processados)

    relatorio = gerar_relatorio(
        alunos_processados,
        alunos_recuperacao,
        top_student,
        alunos_inconsistentes
    )

    with open("resultado.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(relatorio)


main()