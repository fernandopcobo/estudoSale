# Controle e Servomecanismo II — enunciados das atividades

Transcrição em texto dos enunciados publicados pelo Prof. Dr. Renato de Aguiar Teixeira Mendes, para leitura sem abrir os arquivos. O arquivo original continua sendo a referência.

**Notação usada aqui:** derivadas com apóstrofos (`y'` = ẏ, `y''` = ÿ, `y'''` = derivada terceira); matrizes linha a linha, com `;` separando as linhas.

## Resposta transitória — segunda ordem

Publicada em 20/08/2026 · prazo 27/08/2026, 00:00 · original: [lista_exercicios_sistemas_segunda_ordem.pdf](lista_exercicios_sistemas_segunda_ordem.pdf)

1. Determine os polos da função de transferência T(s) = 16 / (s² + 4s + 16).
2. Calcule a frequência natural (ωn) e o amortecimento (ζ) para o sistema T(s) = 25 / (s² + 6s + 25).
3. Um sistema tem ζ = 0,5 e ωn = 10 rad/s. Calcule o tempo de pico (tp).
4. Determine o percentual de máxima sobrelevação (Mp) para um sistema com ζ = 0,4.
5. Dado um sistema com ωn = 5 rad/s e ζ = 0,8, calcule o tempo de acomodação (ts, critério de 2%).
6. Encontre a função de transferência de um sistema que possui tempo de pico de 1 s e sobrelevação de 10%.
7. Um sistema de segunda ordem tem polos em −2 ± j3. Determine a razão de amortecimento (ζ).
8. Calcule o tempo de subida (tr) aproximado para um sistema com ωn = 8 rad/s.
9. Explique o efeito no comportamento temporal se o valor de ζ mudar de 0,2 para 0,7.
10. Se um sistema possui Mp = 25%, qual é o valor de ζ?

## Controle PID

Prazo 03/09/2026, 21:00 · original: [Lista_Exercicios_Controle_PID_Enunciados.pdf](Lista_Exercicios_Controle_PID_Enunciados.pdf)

Lista de Exercícios — Controle de Sistemas (P, PI, PD e PID) · Análise em Regime Permanente e Transitório

**Exercício 1 — Erro Estacionário e Controle Proporcional (P)**

Dada a planta G(s) = 1 / (s + 4) sob malha de realimentação unitária com controlador proporcional C(s) = Kp:

1. Determine o menor valor do ganho Kp que garante um erro estacionário para entrada degrau unitário ess ≤ 0,05 (5%).
2. Calcule a função de transferência em malha fechada T(s) correspondente ao ganho Kp encontrado.

**Exercício 2 — Efeito do Ganho na Constante de Tempo**

Considere a planta de primeira ordem G(s) = 1 / (s + 10) operando em malha fechada unitária com um controlador proporcional C(s) = Kp com ganho fixado em Kp = 15.

1. Encontre a função de transferência em malha fechada T(s) do sistema.
2. Determine a nova constante de tempo τ do sistema em malha fechada e compare com a constante de tempo original em malha aberta.

**Exercício 3 — Ação Integral (PI) e Erro em Regime Permanente**

Para a planta G(s) = 1 / (s + 3), projeta-se um controlador PI da forma C(s) = Kp + Ki / s = (Kp·s + Ki) / s. Considere os ganhos Kp = 5 e Ki = 10:

1. Demonstre analiticamente que o erro em regime permanente para uma entrada degrau unitário é estritamente zero (ess = 0).
2. Encontre a função de transferência em malha fechada T(s) e determine a localização dos polos do sistema.

**Exercício 4 — Ação Derivativa (PD) e Projeto de Amortecimento**

Uma planta de segunda ordem com integrador duplo G(s) = 1 / s² apresenta resposta não amortecida sob controle puramente proporcional. Projeta-se um controlador PD da forma C(s) = Kp + Kd·s:

1. Obtenha a equação característica do sistema em malha fechada.
2. Calcule os valores dos ganhos Kp e Kd necessários para que o sistema apresente frequência natural não amortecida ωn = 5 rad/s e fator de amortecimento ζ = 0,6.

**Exercício 5 — Alocação de Polos com Controlador PID**

Considere a planta de segunda ordem G(s) = 1 / [ s(s + 2) ] e o controlador PID paralelo de estrutura C(s) = Kp + Ki / s + Kd·s:

1. Determine os ganhos Kp, Ki e Kd de modo que a equação característica em malha fechada coincida com o polinômio desejado P(s) = (s + 4)(s² + 4s + 16) = s³ + 8s² + 32s + 64.
2. Escreva a função de transferência em malha fechada T(s) completa.

## Matrizes de variáveis de estado

Publicada em 03/09/2026 · prazo 10/09/2026, 00:00 · original: [lista-exercicios-estudante.docx](lista-exercicios-estudante.docx)

Representação em Variáveis de Estado — Atividade Prática de Modelagem

Resolva cada questão de forma estruturada, definindo claramente as variáveis de estado, reescrevendo a dinâmica do sistema em equações diferenciais de primeira ordem e apresentando o resultado final na forma matricial padrão:

- x'(t) = A·x(t) + B·u(t) (equação de estado)
- y(t) = C·x(t) + D·u(t) (equação de saída)

O texto cita um gabarito ao final da folha, mas o arquivo publicado não o traz.

**Exercício 1 — Sistema Massa-Mola-Amortecedor de 2ª Ordem**

Considere a dinâmica de um sistema mecânico linear descrito pela equação diferencial de segunda ordem abaixo, onde u(t) é a força de entrada (entrada de controle) e y(t) é a posição da massa (saída observada do sistema):

    y''(t) + 4y'(t) + 3y(t) = 2u(t)

Pede-se:

- a) Defina as variáveis de estado do sistema.
- b) Escreva o conjunto correspondente de equações diferenciais de primeira ordem.
- c) Obtenha a representação em espaço de estados na forma matricial padrão (equações de estado e de saída).

**Exercício 2 — Sistema de 3ª Ordem com Saídas Múltiplas**

Considere a equação diferencial linear de terceira ordem que representa um sistema dinâmico. Sabendo que a entrada é u(t) e que estamos interessados em monitorar simultaneamente a posição y(t) e a aceleração y''(t) do sistema (saídas do sistema: y1(t) = y(t) e y2(t) = y''(t)):

    y'''(t) + 6y''(t) + 11y'(t) + 6y(t) = u(t)

(No arquivo original o primeiro termo aparece grafado como ÿ; pelo enunciado, é a derivada terceira.)

Pede-se:

- a) Defina as variáveis de estado do sistema.
- b) Represente o modelo do sistema no espaço de estados.

**Exercício 3 — Sistema de 2ª Ordem com Saída Combinada**

Dada a equação diferencial de segunda ordem que descreve um sistema eletromecânico, onde a entrada é u(t). O sensor do sistema mede uma combinação linear de variáveis, de modo que a saída do sistema é y(t) = 2w(t) + w'(t):

    w''(t) + 7w'(t) + 12w(t) = 5u(t)

(No arquivo original o primeiro termo aparece grafado como ŵ; pelo enunciado, é a derivada segunda.)

Pede-se:

- a) Defina os estados do sistema utilizando as variáveis físicas do problema.
- b) Obtenha as matrizes A, B, C e D da representação no espaço de estados.

## Projeto do controlador

Publicada em 17/09/2026 · prazo 24/09/2026, 00:00 · original: [exercicios-espaco-estados-enunciados.docx](exercicios-espaco-estados-enunciados.docx)

Lista de Exercícios: Espaço de Estado & Formas Canônicas — Caderno de Enunciados, 12 exercícios práticos

**Exercício 1: Formas Canônicas Controlável e Observável (2ª Ordem)** — tópico: formas canônicas

Dada a função de transferência de um sistema linear e invariante no tempo (SLIT):

    G(s) = Y(s) / U(s) = (s + 3) / (s² + 5s + 6)

Obtenha a representação em espaço de estados nas seguintes formas canônicas: a) Forma Canônica Controlável; b) Forma Canônica Observável.

**Exercício 2: Forma Canônica Diagonal (Polos Reais Distintos)** — tópico: formas canônicas

Considere a função de transferência com polos reais distintos:

    G(s) = (2s + 5) / (s² + 5s + 4)

Expanda a função de transferência em frações parciais e determine a representação em espaço de estados na Forma Canônica Diagonal.

**Exercício 3: Teste de Controlabilidade em Sistema 2x2** — tópico: controlabilidade

Dado o sistema no espaço de estados:

    x' = A·x + B·u,   A = [ 1  1 ;  0  -1 ],   B = [ 1 ;  0 ]

Verifique se o sistema é completamente controlável determinando a matriz de controlabilidade Φ_Crt e seu determinante.

**Exercício 4: Teste de Controlabilidade para Sistema de 3ª Ordem** — tópico: controlabilidade

Verifique se o sistema contínuo invariante no tempo de 3ª ordem a seguir é controlável:

    x' = A·x + B·u,   A = [ -2  0  0 ;  0  -4  5 ;  0  -5  -4 ],   B = [ 1 ;  0 ;  2 ]

**Exercício 5: Teste de Observabilidade em Sistema 2x2** — tópico: observabilidade

Dado o sistema no espaço de estados:

    x' = A·x + B·u,   A = [ 1  1 ;  -2  -1 ],   B = [ 0 ;  1 ]
    y = C·x,          C = [ 1  0 ]

Verifique se o sistema é completamente observável determinando a matriz de observabilidade Φ_Obs.

**Exercício 6: Projeto de Controlador por Realimentação de Estados (Alocação Direta)** — tópico: realimentação de estados

Considere o sistema dinâmico:

    x' = A·x + B·u,   A = [ 0  1 ;  -2  -3 ],   B = [ 0 ;  1 ]

Projete o vetor de ganhos K = [ k1  k2 ] com a lei de controle u = −K·x para alocar os polos de malha fechada em s1 = −4 e s2 = −5.

**Exercício 7: Projeto de Controlador com Especificações Temporais (P.O. e Tp)** — tópico: projeto de controladores

Dada a função de transferência do sistema em malha aberta:

    G(s) = 1 / (s² + 4s + 1)

Projete o vetor de ganhos K = [ k1  k2 ] para que o sistema em malha fechada atenda às seguintes especificações de resposta ao degrau:

- Ultrapassagem percentual máxima (P.O.): 5%
- Tempo de pico (Tp): 0,3 s

**Exercício 8: Questão de Concurso (Petrobras 2012 - Adaptada)** — tópico: estabilizabilidade e controlabilidade

Um sistema linear e invariante no tempo é representado pelas equações de estado x'(t) = A·x(t) + B·u(t). Analise as seguintes opções de matrizes A e B em forma diagonal e determine em qual delas o sistema NÃO poderá ser estabilizado utilizando um controlador por realimentação de estados u = −K·x:

- (A) A = diag(5, −2, 1), B = [ 1  1  1 ]ᵀ
- (B) A = diag(−2, 5, −4), B = [ 1  1  0 ]ᵀ
- (C) A = diag(−2, 5, −4), B = [ 0  1  5 ]ᵀ
- (D) A = diag(2, 2, −4), B = [ 2  0  5 ]ᵀ
- (E) A = diag(2, −2, −4), B = [ 0  2  1 ]ᵀ

**Exercício 9: Conversão de E.D.O. de 3ª Ordem para Espaço de Estados** — tópico: modelagem no espaço de estados

Considere a equação diferencial linear de 3ª ordem:

    y'''(t) + 6y''(t) + 11y'(t) + 6y(t) = 2u(t)

Defina os estados como x1 = y, x2 = y', x3 = y'' e escreva as equações matriciais de estado e de saída na Forma Canônica Controlável.

**Exercício 10: Teste de Observabilidade em Sistema de 3ª Ordem** — tópico: observabilidade

Dado o sistema no espaço de estados:

    A = [ -1  1  0 ;  0  -2  1 ;  0  0  -3 ],   C = [ 1  0  0 ]

Determine a matriz de observabilidade Φ_Obs e verifique se o sistema é completamente observável.

**Exercício 11: Realimentação de Estado e Autovalores em Sistema Genérico** — tópico: alocação de polos

Um sistema possui as matrizes de estado:

    A = [ 1  2 ;  3  4 ],   B = [ 0 ;  1 ]

Determine o vetor de ganhos K = [ k1  k2 ] tal que os autovalores de malha fechada sejam λ1 = −2 e λ2 = −3.

**Exercício 12: Cancelamento Polo-Zero, Controlabilidade e Observabilidade** — tópico: propriedades canônicas avançadas

Considere a função de transferência:

    G(s) = (s + 2) / (s² + 3s + 2)

- a) Obtenha a representação em espaço de estados na Forma Canônica Controlável.
- b) Calcule as matrizes de controlabilidade Φ_Crt e de observabilidade Φ_Obs.
- c) Explique a relação entre o cancelamento polo-zero em G(s) e as propriedades de controlabilidade/observabilidade.
