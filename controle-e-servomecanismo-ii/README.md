# Controle e Servomecanismo II

**Professor:** Prof. Dr. Renato de Aguiar Teixeira Mendes  
**Semestre:** 2026/2 · Engenharia de Computação · UniSALESIANO Araçatuba  
**Curso no Moodle:** [missaosalesiana.mrooms.net/course/view.php?id=17256](https://missaosalesiana.mrooms.net/course/view.php?id=17256) (requer login)  
**Conteúdo conferido em:** 13/10/2026

Conteúdo publicado até aqui, na ordem das aulas:

1. Resposta transitória de sistemas de 2ª ordem
2. Controle P, PI, PD e PID
3. Representação em variáveis de estado
4. Formas canônicas, controlabilidade e observabilidade
5. Projeto de controlador por realimentação de estados (alocação de polos)

## Material de apoio

| Arquivo | Tamanho | O que tem |
|---------|---------|-----------|
| [aula  segunda ordem.pptx](material-de-apoio/Resposta%20de%20Segunda%20Ordem/aula%20%20segunda%20ordem.pptx) | 1,8 MB | Resposta transitória de sistemas de 2ª ordem: comportamento sem amortecimento, resposta ao degrau para cada caso e especificações do caso subamortecido (máximo overshoot / ultrapassagem percentual, tempo de pico). 13 slides. |
| [aula segunda ordem 2.pdf](material-de-apoio/Resposta%20de%20Segunda%20Ordem/aula%20segunda%20ordem%202.pdf) | 745 KB | Sistemas de 2ª ordem: efeito dos parâmetros na forma da resposta; respostas superamortecida, subamortecida, não amortecida e criticamente amortecida a partir da posição dos polos. 14 slides. |
| [resumo_sistemas_segunda_ordem_simbolos.pdf](material-de-apoio/Resposta%20de%20Segunda%20Ordem/resumo_sistemas_segunda_ordem_simbolos.pdf) | 21 KB | Folha de fórmulas: T(s) = ωn² / (s² + 2ζωn·s + ωn²), resposta no tempo do caso subamortecido, ωd, tempo de pico, máxima sobrelevação (Mp) e tempo de acomodação (critério de 2 %). 1 página. |
| [segunda ordem 3.pptx](material-de-apoio/Resposta%20de%20Segunda%20Ordem/segunda%20ordem%203.pptx) | 4,7 MB | Especificações da resposta transitória: tempo de atraso, subida, pico, acomodação e sobressinal; faixa recomendada de ζ (0,4 a 0,8); relação geométrica entre polos, ζ e ωn. 24 slides. |
| [Controle_PID_Explicacao_Didatica.pdf](material-de-apoio/Controle_PID_Explicacao_Didatica.pdf) | 32 KB | Guia didático de PID: erro e(t) pela analogia do chuveiro; ação proporcional (presente), integral (passado) e derivativa (futuro); equação completa no tempo e em Laplace, C(s) = Kp + Ki/s + Kd·s. 3 páginas. |
| [State-Space_Modeling_Decoded.pptx](material-de-apoio/State-Space_Modeling_Decoded.pptx) | 14,6 MB | Representação em variáveis de estado (slides em imagem): Laplace × espaço de estados, conceito de estado, conversão de uma EDO de ordem n em n equações de 1ª ordem, forma ẋ = Ax + Bu / y = Cx + Du, ponte G(s) = C(sI − A)⁻¹B + D e exemplo resolvido de 3ª ordem. 14 slides. |
| [observ (2).pptx](material-de-apoio/observ%20%282%29.pptx) | 1,3 MB | Projeto de controladores por realimentação de estados (slides do professor, equações em imagem). 26 slides. |
| [State_Feedback_Controller_Design.pptx](material-de-apoio/State_Feedback_Controller_Design.pptx) | 15,0 MB | Projeto do controlador por realimentação de estados (slides em imagem): formas canônicas controlável, observável e diagonal; controlabilidade e observabilidade (det ≠ 0); lei u = −Kx; alocação de polos; síntese em 3 etapas e exercício resolvido (G(s) = 1/(s² + 4s + 1), P.O. 5 %, Tp 0,3 s → K = [208 16]). 15 slides. |

## Arquivos das atividades

| Arquivo | Tamanho | O que tem |
|---------|---------|-----------|
| [exercicios-espaco-estados-enunciados.docx](atividades/exercicios-espaco-estados-enunciados.docx) | 39 KB | Caderno com 12 exercícios: formas canônicas controlável, observável e diagonal; testes de controlabilidade e observabilidade (2ª e 3ª ordem); projeto por realimentação de estados com alocação direta e com especificações de P.O. e Tp; questão Petrobras 2012 adaptada; cancelamento polo-zero. |
| [lista_exercicios_sistemas_segunda_ordem.pdf](atividades/lista_exercicios_sistemas_segunda_ordem.pdf) | 14 KB | Enunciados (10 exercícios): polos, ωn, ζ, tempo de pico, sobrelevação, tempo de acomodação e de subida de sistemas de 2ª ordem. 1 página. |
| [Exercicios_Controle_P_PI_PD_PID.pdf](atividades/Exercicios_Controle_P_PI_PD_PID.pdf) | 37 KB | Lista resolvida 1 de controle P, PI, PD e PID: erro estacionário, constante de tempo, polos de malha fechada, amortecimento e projeto PID por casamento de polinômio característico. 5 exercícios, 3 páginas. |
| [Exercicios_Controle_P_PI_PD_PID_v2.pdf](atividades/Exercicios_Controle_P_PI_PD_PID_v2.pdf) | 36 KB | Lista resolvida 2 de controle P, PI, PD e PID: mesmos tipos de exercício da lista 1 com outros parâmetros. 3 páginas. |
| [Lista_Exercicios_Controle_PID_Enunciados.pdf](atividades/Lista_Exercicios_Controle_PID_Enunciados.pdf) | 21 KB | Enunciados (5 exercícios): erro estacionário com P, efeito do ganho na constante de tempo, ação integral (PI), ação derivativa (PD) e alocação de polos com PID. 2 páginas. |
| [lista-exercicios-estudante.docx](atividades/lista-exercicios-estudante.docx) | 32 KB | Enunciados (3 exercícios, com gabarito das matrizes ao final): massa-mola-amortecedor de 2ª ordem, sistema de 3ª ordem com saídas múltiplas e sistema de 2ª ordem com saída combinada. |

## Atividades e avaliações

| Tipo | Atividade | Abertura | Prazo | O que pede | Anexo |
|------|-----------|----------|-------|------------|-------|
| Tarefa | [RespostaTtransitória - Segunda Ordem](https://missaosalesiana.mrooms.net/mod/assign/view.php?id=255910) | 20 ago. 2026, 00:00 | 27 ago. 2026, 00:00 | Ver enunciado em anexo. | [lista_exercicios_sistemas_segunda_ordem.pdf](atividades/lista_exercicios_sistemas_segunda_ordem.pdf) |
| Tarefa | [Controle PID](https://missaosalesiana.mrooms.net/mod/assign/view.php?id=256893) | — | 3 set. 2026, 21:00 | Ver enunciado em anexo. | [Lista_Exercicios_Controle_PID_Enunciados.pdf](atividades/Lista_Exercicios_Controle_PID_Enunciados.pdf) |
| Tarefa | [Matrizes de Variaveis de Estado](https://missaosalesiana.mrooms.net/mod/assign/view.php?id=258121) | 3 set. 2026, 00:00 | 10 set. 2026, 00:00 | Ver enunciado em anexo. | [lista-exercicios-estudante.docx](atividades/lista-exercicios-estudante.docx) |
| Tarefa | [Projeto do controlador](https://missaosalesiana.mrooms.net/mod/assign/view.php?id=259643) | 17 set. 2026, 00:00 | 24 set. 2026, 00:00 | Ver enunciado em anexo. | [exercicios-espaco-estados-enunciados.docx](atividades/exercicios-espaco-estados-enunciados.docx) |
