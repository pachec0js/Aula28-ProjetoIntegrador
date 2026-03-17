# Atividade Kanban II - SENAI Ciência de Dados

Este repositório contém a solução da atividade "Metodologias Ágeis - Kanban II". O objetivo é desenvolver um programa em Python para processar o desempenho acadêmico dos alunos, usando listas e tuplas, tratando dados corrompidos e gerando um relatório detalhado (`resultado.txt`).

---

## 2. Levantamento de Requisitos

Abaixo estão os requisitos e regras de negócio mapeados a partir do _Briefing_ da Coordenação do SENAI:

### Requisitos Funcionais (RF)

- **RF01:** O sistema deve receber e processar uma entrada de dados estruturada em uma lista de tuplas no formato `[("Nome", [notas])]`.
- **RF02:** O sistema deve validar a lista de notas de cada aluno, identificando notas ausentes (vazias) ou possíveis corrupções de dados (valores nulos).
- **RF03:** O sistema deve usar estruturas de repetição para percorrer as notas e calcular a média aritmética de cada aluno validado.
- **RF04:** O sistema deve identificar automaticamente se um aluno está em "Recuperação".
- **RF05:** O sistema deve identificar e destacar o aluno com o melhor desempenho ("Top Student").
- **RF06:** Ao final da execução, o sistema deve exportar os dados consolidados para um arquivo de texto chamado `resultado.txt` contendo as médias, situação dos alunos e o Top Student.

### Requisitos Não-Funcionais (RNF)

- **RNF01:** A solução deve ser desenvolvida em Python.
- **RNF02:** O código não pode estar em um arquivo único; deve ser **modularizado**, separando a lógica de negócios na qual um arquivo se chamará `processamento.py` e a execução principal deverá ocorrer no arquivo `main.py`.
- **RNF03:** O código deve conter tratamento de erros adequado durante o processamento de variáveis (dados inconsistentes) para que a aplicação não "quebre" na execução.
- **RNF04:** O código final produzido pelo desenvolvedor dever ser versionado no GitHub usando branches separadas (ex: `feat/calculo`) e passar por um fluxo de Merge para a branch `main`.

### Regras de Negócio (RN)

- **RN01:** A situação de _Recuperação_ aplica-se apenas a alunos cuja média final seja inferior a **7.0**.
- **RN02:** O título de _Top Student_ é dado exclusivamente ao aluno que possuir a **maior média** dentre todos os registros válidos processados da turma.

---

## 3. Metodologia (Design Thinking e Gestão Ágil)

> 📌 **Acompanhamento Visual e Dinâmico:** O detalhamento em texto abaixo sobre o Mapa de Empatia e o Kanban serve como um registro estrutural de como o planejamento inicial foi concebido. A gestão ágil oficial, dinâmica e visual das tarefas e ideias do projeto ocorre em nosso **[Board no Miro](https://miro.com/welcomeonboard/cWh0SW8wbmNMNEdGakYyUXJlV3owNCs1Lzk4aktHTVNlUVlaYVQxTk41bzB1Z3BEelV4WGptZmpQaVViTEZTRWIzZHhOV1l2Wk40dEpjWGhSSFNHbHlodXBEWmpTdVNCdDdoNFNuSEh1aEFLdjlzZFptUCttK2lDYUdnQVRFeFNyVmtkMG5hNDA3dVlncnBvRVB2ZXBnPT0hdjE=?share_link_id=724497200461)**.
>
> _As capturas de tela das dinâmicas realizadas no Miro encontram-se documentadas na pasta:_ `prints/`.

### Mapa de Empatia (Coordenação do SENAI)

**1. Com quem estamos sendo EMPÁTICOS?**

- A Coordenação do SENAI, que é responsável pela validação de notas, cálculo de médias e tomada de decisão sobre o desempenho acadêmico dos alunos.

**2. O que ela precisa fazer?**

- Processar o desempenho acadêmico da turma (entender o formato `[("Nome", [notas])]`).
- Lidar com dados inconsistentes, nulos ou ausentes sem que o sistema "quebre".
- Identificar rapidamente os alunos em recuperação (média < 7.0) e o "Top Student".
- Gerar um relatório padronizado e limpo em texto (`resultado.txt`).

**3. O que ela VÊ?**

- Planilhas e informações chegando em múltiplos formatos ou com graves lacunas.
- Dificuldade na identificação de alunos precisando de apoio e negligência com destaques.
- Desorganização nos sistemas antigos, com códigos "espaguete", difíceis de dar manutenção.

**4. O que ela FALA?**

- "Preciso cobrar envios corretos, pois com dados nulos nosso fechamento trava."
- "O processo de fechamento tem dependido de correções à mão, o que é inseguro."

**5. O que ela FAZ?**

- Perde horas calculando quem passou ou quem reprovou, gerando estresse e atrasos.
- Corre atrás de correções pontuais, registro por registro.
- Lida com retrabalho em fechamentos manuais de média.

**6. O que ela ESCUTA?**

- Professores sobrecarregados pela falta de automatização nos lançamentos.
- Reclamações de alunos / responsáveis sobre inconsistências nas médias publicadas ou demoras no resultado.

**7. O que ela PENSA e SENTE?**

- Sente **frustração e insegurança** contínua com perdas de dados e retrabalhos. Teme que decisões erradas afetem o futuro do aluno.
- **Dores:** Falta de clareza acadêmica; trabalho braçal muito cansativo; alto risco de falha manual.
- **Desejos:** Necessita de uma solução automatizada, modularizada (`processamento.py` e `main.py`) e confiável que lide com exceções graciosamente. Deseja obter uma lista visual limpa das médias e de destaques/recuperação sem esforço adicional.

---

### Quadro Kanban do Projeto

Abaixo está o fluxo de trabalho detalhado usando o método Kanban para guiar o desenvolvimento do projeto. Essa estrutura visa maximizar a previsibilidade e organização, sendo o modelo oficial a ser replicado no **Miro**.

#### 📝 To Do (A Fazer - Pendências da Sprint)

- **[Setup]** Configurar branch `feat/processamento` e inicializar o arquivo base `processamento.py`. `(🔴 Alta Prioridade)`
- **[Core]** Implementar rotinas matemáticas: Cálculo de Média Aritmética e filtro de Recuperação (`média < 7`). `(🔴 Alta Prioridade)`
- **[Core]** Desenvolver algoritmo de varredura para identificar o aluno de maior destaque (_Top Student_). `(🟡 Média Prioridade)`
- **[Exportação]** Codificar a rotina de formatação e geração do relatório de saída `resultado.txt`. `(🔴 Alta Prioridade)`
- **[Integração]** Construir arquivo `main.py`, declarar a lista de tuplas base `[("Nome", [notas])]` e invocar os módulos. `(🔴 Alta Prioridade)`
- **[QA/Testes]** Executar bateria de testes manuais locais, validando comportamento contra dados corrompidos (strings ou `None`). `(🟡 Média Prioridade)`
- **[DevOps]** Realizar commit estruturado e Merge Request final para a branch principal `main`. `(🟢 Baixa Prioridade - Final da Sprint)`

#### 🔄 Doing (Em Progresso)

- **[Projeto/Gestão]** Modelagem da infraestrutura ágil no README e transição do quadro para a plataforma visual **Miro**. `(🔥 Em Execução)`

#### ✅ Done (Concluído)

- **[Produto]** Leitura e análise profunda do _briefing_, interpretando as necessidades do SENAI. `(✔️ Concluído)`
- **[Requisitos]** Documentação e levantamento estruturado de RFs, RNFs e Regras de Negócio. `(✔️ Concluído)`
- **[UX/Empatia]** Construção e preenchimento detalhado do Mapa de Empatia em 7 pilares (Perspectiva da Coordenação). `(✔️ Concluído)`
- **[Setup]** Inicialização do repositório no GitHub, estruturação documental inicial do `README.md`. `(✔️ Concluído)`

---
