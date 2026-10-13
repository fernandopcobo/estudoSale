# Sistemas Embarcados I — enunciados das atividades

Transcrição em texto dos enunciados publicados pelo Prof. Amadeu Zanon Neto, para leitura sem abrir os arquivos. O arquivo original continua sendo a referência. Os PDFs não têm figuras além do cabeçalho.

## 11/08/2026 — Controle por comunicação serial

Prazo 18/08/2026, 20:45 · original: [Exercicio 2026-08-11 - Comunicação entre microcontroladores.pdf](<Exercicio 2026-08-11 - Comunicação entre microcontroladores.pdf>)

Utilizando-se de um microcontrolador, coloque oito resistores de 220R e oito leds na porta C e seis botões em pull-down na porta A dele.

Após a montagem, crie um programa onde seja possível através do terminal ligar e desligar leds individualmente e geral, e saber se os botões estão ligados ou desligados.

## 18/08/2026 — Envio de valores a displays de 7 segmentos

Prazo 25/08/2026, 23:59 · original: [Exercicio 2026-08-25 - Display de sete segmentos com serial.pdf](<Exercicio 2026-08-25 - Display de sete segmentos com serial.pdf>)

Desenvolva um projeto onde através de um terminal e comunicação serial, seja possível enviar um valor entre 0 e 99 e mostrar este valor enviado em dois displays de sete segmentos.

Montar a protoboard e utilizar bluetooth ou conversor USB-SERIAL FTDI para teste.

A montagem deve ser feita em laboratório e deve ser enviada a pasta com os arquivos do projeto e uma foto da atividade pronta (apresentar ao professor).

Projetos de apoio publicados pelo professor: [Exercicio 2026-08-25 - Serial com Display de 7 segmentos.zip](<Exercicio 2026-08-25 - Serial com Display de 7 segmentos.zip>) e [versão TextoSerial](<Exercicio 2026-08-25 - Serial com Display de 7 segmentos - TextoSerial.zip>).

## Comunicação serial em anel

Publicada em 25/08/2026 · prazo 01/09/2026, 23:59 · original: [Exercicio 2026-09-01 - Comunicação em Anel e displays de 7 segmentos.pdf](<Exercicio 2026-09-01 - Comunicação em Anel e displays de 7 segmentos.pdf>)

Usando o método de comunicação serial em anel, desenvolva um projeto em simulador onde seja possível enviar um valor em um sistema de três microcontroladores conectados pela porta serial em anel, através de um terminal um valor de 0 a 99 com endereçamento em um dos três microcontroladores e este valor deve ser mostrado em dois dígitos de displays de 7 segmentos controlados por cada um.

Projeto de apoio publicado pelo professor: [Exercicio 2026-09-01 - Comunicacao em Anel.zip](<Exercicio 2026-09-01 - Comunicacao em Anel.zip>).

## Intermitência com interrupção

Publicada em 15/09/2026 · prazo 22/09/2026, 23:59 · original: [Exercicio 2026-09-08 - Intermitência com Interrupção.pdf](<Exercicio 2026-09-08 - Intermitência com Interrupção.pdf>)

Desenvolver projeto em simulador e protoboard onde seja possível controlar a intermitência de três leds com intervalo de 200 ms.

Quando houver a interrupção em RA2, fazer com que os três leds pisquem juntos em intervalo de 500 ms, quando a interrupção se encerrar voltar a sequência de onde parou.

Todo o controle deve ser feito através de interrupções e utilize um cristal oscilador de 4 MHz.

## Trabalho 01 — Multiplexação por interrupção de timer

Publicado em 22/09/2026 · prazo no Moodle 06/10/2026, 23:59 · original: [Trabalho 01 - Controle de multiplexação com interrupção.docx](<Trabalho 01 - Controle de multiplexação com interrupção.docx>) (modelo de relatório a preencher)

Desenvolver projeto completo com simulador, linguagem mikroBasic e montagem em protoboard onde o microcontrolador PIC 16F690 possa receber via serial um valor entre 0 e 999 (inclusive) e mostrar esse valor em três displays de 7 segmentos para centena, dezena e unidade.

Obrigatoriamente deve-se utilizar no circuito um cristal oscilador e o método de interrupção por timer.

- **Formas de apresentação marcadas no modelo:** montagem prática, seminário/apresentação/banner, relatório, simulação e desenvolvimento de software.
- **Datas no modelo:** apresentação do projeto em 22/09/2026, 19:05; encerramento em 19/10/2026, 19:05. O prazo de envio no Moodle é anterior (06/10/2026).
- **Seções do relatório:** integrantes e funções, enunciado, esquemático ou croqui, datas, componentes e materiais, equipamentos de laboratório, softwares utilizados, problemas e soluções, conclusões e anexo com a programação.
