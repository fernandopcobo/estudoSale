# Automação Industrial — enunciados das atividades

Transcrição em texto dos enunciados publicados pelo Prof. Amadeu Zanon Neto, para leitura sem abrir os arquivos. As figuras dos PDFs estão descritas entre colchetes; o arquivo original continua sendo a referência.

## Lista 01 — Ladder com sinais discretos

Publicada em 24/08/2026 · prazo 31/08/2026, 23:59 · original: [Exercicios 2026-08-24 - Entradas discretas.pdf](<Exercicios 2026-08-24 - Entradas discretas.pdf>)

Desenvolva os programas em Ladder para a solução dos problemas de automação abaixo:

1. Desenvolva projeto onde um tanque é carregado através de uma bomba, a bomba é ligada automaticamente quando o líquido chegar a um sensor de nível na parte inferior do tanque e desligar quando o líquido chegar ao sensor de nível máximo.

   [Figura: tanque com a bomba na entrada, sensor de nível alto no topo e sensor de nível baixo na base.]

2. Uma bomba alimenta três tanques onde as válvulas vão se fechando conforme cada tanque vai se enchendo. Ao ligar a bomba de maneira manual, o sistema verifica os tanques em que o nível de produto não está no máximo e as abre.

   [Figura: uma bomba em uma tubulação comum; três tanques, cada um com uma válvula na entrada e um sensor de nível alto.]

3. Crie um projeto para automatizar uma esteira transportadora de produtos onde ela separa caixas em um sistema para esquerda e direita alternadamente.

   [Figura: esteira em T com motor da esteira, um sensor antes da bifurcação e um motor separador que desvia para ESQUERDA ou DIREITA; painel com botoeira ON/OFF.]

4. Vamos automatizar uma máquina de assar pizzas, onde o operador liga o motor de uma esteira que leva a pizza que foi colocada nesta esteira, ao passar por um sensor aciona o sistema de aquecimento que assa a pizza e ao sair pelo outro lado da máquina, passa por outro sensor que desliga o aquecimento.

   [Figura: esteira com motor, sensor de entrada, aquecimento e sensor de saída; painel com botoeira ON/OFF.]

5. Desenvolva um projeto onde uma esteira seja automatizada para separar três tipos de materiais, metal, plástico e vidro através de sensores: indutivo para metais e dois capacitivos para vidro e plástico. Conforme o sensor detecta o material que entra pelo carregamento passa pelos sensores o atuador adequado é acionado, retraindo os outros dois que não serão utilizados no momento. O sistema só deve detectar e acionar os atuadores se estiver em situação de ativo pela botoeira no painel, mostrado pela lâmpada piloto e acionando o motor. Desliga-se o processo pela mesma botoeira do painel.

   [Figura: entrada de material, três sensores em sequência, três atuadores e três saídas (metal, vidro, plástico); motor da esteira; painel com botoeira ON/OFF e lâmpada piloto.]

## Lista de contadores em Ladder

Publicada em 31/08/2026 · prazo 21/09/2026, 23:59 · original: [Exercicios 2026-08-31 - Contadores.pdf](<Exercicios 2026-08-31 - Contadores.pdf>)

Desenvolver o programa Ladder para resolver os problemas propostos abaixo.

1. Desenvolva um programa para controlar uma esteira que conta 12 latas que passam por um sensor e ao final da contagem aciona um sistema de embalo. Zerar o contador através de uma botoeira e desligar o sistema acionado. Para ligar novamente coloque uma botoeira que também pode desligar a máquina.

   [Figura: painel com lâmpada "12 Latas" e botoeiras ON/OFF e RESET; motor da esteira principal; sensor; motor do sistema de embalagem.]

2. Um sistema de separação de parafusos, faz o sensoriamento de 5 tipos deles com um sensor indutivo de anel em cada tubo de passagem. Faça com que a cada 5 parafusos de cada tipo uma luz indicativa seja acionada no painel. Crie uma botoeira de reset de todos os contadores e desligue as luzes de painel.

   [Figura: cinco funis (Tipo 1 a Tipo 5), cada um com um sensor na saída; painel com cinco lâmpadas (Tipo 1 a 5) e botoeira RESET.]

3. Uma fábrica produz bolas em três cores, vermelha, verde e azul que passam por sensores que acionam uma saída digital para cada cor separadamente que fazem com que sejam acondicionadas em embalagens de 12 unidades. Quando qualquer uma das cores atingir a contagem de 12, um sinal deve acionar o sistema de lacre da embalagem e zerar o contador da cor finalizada através de uma botoeira para cada uma delas.

   [Figura: três sensores (vermelho, verde, azul), três atuadores para empurrar as bolas e três saídas para caixas; painel com lâmpada "12 UN", botoeira RESET e um par luz/botão para cada cor.]

4. Um sistema conta o número de pessoas que podem entrar em uma sala que comporta até sessenta pessoas através de uma catraca. Deve-se, conforme a contagem vai atingindo múltiplos de 10 (10, 20, 30, 40, 50 e 60) mostrar luzes do painel cada múltiplo indicando estas quantidades e trava esta catraca, não permitindo mais o acesso ao atingir o limite. Para facilitar os testes, coloque o limite de contadores em 1, 2, 3, 4, 5 e 6.

   [Figura: porta da SALA 01 com catraca e sensor; painel "PESSOAS" com seis luzes (10 a 60, a última marcada como limite) e botoeira RESET.]

5. Crie um projeto para automatizar uma esteira transportadora de produtos embalados, onde ela separa 6 caixas para à esquerda e para à direita alternadamente. A botoeira no painel liga e desliga o sistema, ao iniciar zera a contagem.

   [Figura: a mesma esteira em T do exercício 3 da Lista 01: motor da esteira, sensor, motor separador e botoeira ON/OFF.]

## Lista de temporizadores (timers) em Ladder

Publicada em 21/09/2026 · prazo 05/10/2026, 23:59 · original: [Exercicios 2026-09-14 - Temporizadores.pdf](<Exercicios 2026-09-14 - Temporizadores.pdf>)

Desenvolver programa Ladder para resolver os problemas propostos abaixo.

1. Desenvolver um sistema de semáforo de 2 tempos utilizando-se das luzes do painel de testes. O tempo de alternância deve ser de 5 segundos, ligar o amarelo na passagem do vermelho para o verde.

   [Figura: dois semáforos de três luzes.]

2. Faça projeto onde as lâmpadas do painel sejam acesas de maneira sequencial com intervalo de 3 segundos. Partir ao pressionar uma botoeira, ao atingir a última lâmpada retornar à primeira, desligar por outra botoeira.

   [Figura: painel com 8 lâmpadas em linha e botoeiras Partida e Parada.]

3. Em uma esteira, tijolos entram em um forno. Quando 6 tijolos estiverem no forno, desligue a esteira, ligue um sistema de aquecimento por 15 segundos e depois deste tempo ligue novamente a esteira e reinicie o processo. Colocar chave liga/desliga no sistema.

   [Figura: esteira com motor, sensor na entrada do aquecedor elétrico; painel com chave ON/OFF e duas luzes de estado.]

4. Desenvolva um projeto com intermitência das luzes do painel, onde quatro padrões de sequência podem ser selecionados através das chaves nas entradas.

   [Figura: painel com 8 lâmpadas, botoeiras Partida e Parada e quatro chaves numeradas de 1 a 4.]

5. Melhorando a máquina de assar pizzas. Agora o sistema deve ligar a esteira da máquina quando um sensor detectar que uma pizza foi colocada nela. A esteira é acionada para levar a pizza até o forno que possui um sensor interno que detecta a chegada da pizza, o motor da esteira se desliga, o sistema de aquecimento do forno é ativado por 20 segundos e desligado. Liga-se a esteira novamente até que o sensor no final detecte a saída desta e se desliga.

   [Figura: motor da esteira, sensor de entrada, sensor de aquecimento dentro do forno, aquecedor elétrico e sensor de saída; painel com três luzes de estado.]

6. Neste processo de mistura de tinta o programa deverá seguir o processo descrito nos passos abaixo:
   - a. Ao pressionar o botão início, inicia-se o processo, enchendo o tanque com o ingrediente 1 (bomba 1) até atingir o sensor de nível baixo.
   - b. O ingrediente 2 (bomba 2) é inserido no tanque até atingir o sensor de nível alto.
   - c. Comece a misturar os ingredientes ligando o motor do misturador e abra a válvula de vapor para começar o período de aquecimento por dez segundos.
   - d. Após este período esvazie o tanque da mistura pela válvula e pela bomba de dreno.
   - e. Após sete segundos depois de detectar que a mistura está abaixo do nível mínimo do tanque, desligue a válvula e a bomba de drenagem.
   - f. Para repetir o ciclo, deve-se pressionar o botão ON/OFF do painel.

   [Figura: tanque com Bomba 1 e Bomba 2 no topo, motor do misturador, sensor de nível alto, sensor de nível baixo, válvula de vapor, válvula de dreno e bomba de dreno; painel com botão ON/OFF ("Start do sistema").]

## Trabalho 01 — Controle automatizado de corte de toras

Publicado em 28/09/2026 · prazo no Moodle 19/10/2026, 19:05 · original: [Trabalho 01 - Corte automatizado de toras.docx](<Trabalho 01 - Corte automatizado de toras.docx>) (modelo de relatório a preencher)

Um cliente necessita de que uma máquina de corte de toras de eucalipto em tamanhos específicos regulado pelo sensor de presença da madeira. O operador pode ligar e desligar uma esteira transportadora da tora por uma botoeira, a madeira é transportada até o sensor de detecção, a esteira para; uma serra é ligada e seu disco abaixado até um sensor de fim de curso, o disco retorna e a serra é desligada onde a madeira é movimentada continuando o processo. Desenvolver o croqui e a programação Ladder para a solução do problema. A cada seis cortes efetuados um sinal luminoso deve ser acionado informando ao operador da situação e permitindo que este faça o reset manual.

Faça um desenho (croqui) para representar a máquina e o posicionamento dos sensores.

- **Formas de apresentação marcadas no modelo:** seminário/apresentação/banner, relatório, simulação e desenvolvimento de software.
- **Datas no modelo:** apresentação do projeto em 28/09/2026, 19:05; encerramento em 19/10/2026, 19:50.
- **Seções do relatório:** integrantes e funções, enunciado, croqui, datas, componentes e materiais, equipamentos de laboratório, softwares utilizados, problemas e soluções, conclusões e anexo com a programação.
