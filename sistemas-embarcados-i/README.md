# Sistemas Embarcados I

**Professor:** Prof. Amadeu Zanon Neto  
**Semestre:** 2026/2 · Engenharia de Computação · UniSALESIANO Araçatuba  
**Curso no Moodle:** [missaosalesiana.mrooms.net/course/view.php?id=16321](https://missaosalesiana.mrooms.net/course/view.php?id=16321) (requer login)  
**Conteúdo conferido em:** 13/10/2026

**Objetivo (página do curso):** desenvolver conhecimentos específicos para construção de softwares de controle de máquinas robotizadas e linguagens avançadas para fins didáticos, industriais e científicos, com incentivo à pesquisa.

Na prática: microcontroladores PIC (16F690, 16F887) programados em mikroBasic e simulados no Proteus. Temas até aqui: comunicação serial RS-232, comunicação em anel, displays de 7 segmentos, interrupções por timer e por hardware, cristal oscilador, memórias RAM externa e EEPROM.

Os `.zip` são projetos completos (fonte `.pbas`, `.hex` compilado e simulação `.DSN`).

## Links da disciplina

- [Textos e softwares (Google Drive do professor)](https://drive.google.com/file/d/1heeG6eJG2l94dfLoYdRiX6pTgEwysXu8/view?usp=drive_link)

## Material de apoio

| Arquivo | Tamanho | O que tem |
|---------|---------|-----------|
| [Aula 2026-08-04 - Comunicacao Serial.zip](material-de-apoio/Aula%202026-08-04%20-%20Comunicacao%20Serial.zip) | 128 KB | Projeto da aula de comunicação serial RS-232: fonte mikroBasic (`RS232.pbas`), arquivos compilados (`.hex`, `.asm`, `.lst`) e simulação Proteus (`Placa.DSN`) com esquemático em PDF. |
| [Aula 2026-08-18 - Comunicacao em Anel - Serial.zip](material-de-apoio/Aula%202026-08-18%20-%20Comunicacao%20em%20Anel%20-%20Serial.zip) | 131 KB | Projeto da aula de comunicação serial em anel entre dois microcontroladores (`PIC01` e `PIC02`): fontes mikroBasic, compilados e simulação Proteus. |
| [Teste126 - RAM - 62256 com PIC 16F887 - Terminal Texto.zip](material-de-apoio/Teste126%20-%20RAM%20-%2062256%20com%20PIC%2016F887%20-%20Terminal%20Texto.zip) | 3,4 MB | Exemplo de gravação e leitura em RAM externa HM62256 (32 KB) com PIC16F887 e terminal de texto: descrição do método (DOCX/PDF), datasheets do PIC16F887 e da RAM, esquemático e simulação Proteus, arquivos de texto para teste. |
| [FÓRMULA PARA CÁLCULO DE TEMPO DE ACIONAMENTO DE INTERRUPÇÃO POR TIMER.pdf](material-de-apoio/F%C3%93RMULA%20PARA%20C%C3%81LCULO%20DE%20TEMPO%20DE%20ACIONAMENTO%20DE%20INTERRUP%C3%87%C3%83O%20POR%20TIMER.pdf) | 673 KB | Fórmula do tempo de disparo da interrupção por timer: `t = 4 / fosc × prescaler × 256`, com o significado de cada termo e exemplo numérico (4 MHz, prescaler 4 → 1,024 ms). 1 página. |
| [PIC16F690 INTCON.pdf](material-de-apoio/PIC16F690%20INTCON.pdf) | 73 KB | Página do datasheet Microchip do PIC16F690 com o registrador `INTCON` (bits de habilitação e flags de interrupção: TMR0, mudança em PORTA, INT externa). |
| [PIC16F690 OPTION_REG.pdf](material-de-apoio/PIC16F690%20OPTION_REG.pdf) | 73 KB | Página do datasheet Microchip do PIC16F690 com o registrador `OPTION_REG` (prescaler do Timer0/WDT, borda da INT externa, pull-ups). |
| [Tabela ASCII com códigos de controle e teclado.pdf](material-de-apoio/Tabela%20ASCII%20com%20c%C3%B3digos%20de%20controle%20e%20teclado.pdf) | 332 KB | Tabela ASCII com códigos de controle e códigos de teclado (imagem escaneada, sem texto pesquisável). |
| [Tabela ASCII Padrão.pdf](material-de-apoio/Tabela%20ASCII%20Padr%C3%A3o.pdf) | 136 KB | Tabela ASCII padrão (caractere × hexadecimal × decimal), página extraída de livro de sistemas digitais. |
| [tabelaASCII.pdf](material-de-apoio/tabelaASCII.pdf) | 141 KB | Tabela ASCII completa com decimal, binário, hexadecimal e descrição de cada código. 7 páginas. |
| [TabelaClock.png](material-de-apoio/TabelaClock.png) | 15 KB | Imagem com a tabela de configuração de clock. |
| [Valores-capacitores-cristal.jpg](material-de-apoio/Valores-capacitores-cristal.jpg) | 40 KB | Imagem com os valores de capacitores recomendados para cada faixa de cristal oscilador. |
| [Como funciona o cristal na eletrônica (ART423).pdf](material-de-apoio/Como%20funciona%20o%20cristal%20na%20eletr%C3%B4nica%20%28ART423%29.pdf) | 3,1 MB | Artigo "Como funciona o cristal na eletrônica" (ART423): efeito piezoelétrico, cristais de quartzo, ressonância e uso em osciladores. 11 páginas. |
| [Comunicação Serial RS-232.pdf](material-de-apoio/Comunica%C3%A7%C3%A3o%20Serial%20RS-232.pdf) | 259 KB | Resumo do professor sobre RS-232 como protocolo eletrônico de comunicação serial e ASCII como protocolo lógico dos dados. 2 páginas. |
| [Teste139 - Interrupcao com TIMERS e Hardware com PIC 16F690.zip](material-de-apoio/Teste139%20-%20Interrupcao%20com%20TIMERS%20e%20Hardware%20com%20PIC%2016F690.zip) | 4,0 MB | Exemplo de interrupção por timers e por hardware no PIC16F690: projeto mikroBasic PRO (`TIMER2PRO`), simulação Proteus e a fórmula de cálculo do tempo do timer. |
| [Teste169 - Memoria EEprom - PIC 16F690.zip](material-de-apoio/Teste169%20-%20Memoria%20EEprom%20-%20PIC%2016F690.zip) | 119 KB | Exemplo de leitura e gravação na memória EEPROM interna do PIC16F690: fonte mikroBasic, compilados e simulação Proteus. |

## Arquivos das atividades

| Arquivo | Tamanho | O que tem |
|---------|---------|-----------|
| [Exercicio 2026-08-11 - Comunicação entre microcontroladores.pdf](atividades/Exercicio%202026-08-11%20-%20Comunica%C3%A7%C3%A3o%20entre%20microcontroladores.pdf) | 146 KB | Enunciado: oito LEDs na porta C e seis botões em pull-down na porta A; pelo terminal serial, ligar e desligar LEDs (individual e geral) e consultar o estado dos botões. |
| [Exercicio 2026-08-25 - Display de sete segmentos com serial.pdf](atividades/Exercicio%202026-08-25%20-%20Display%20de%20sete%20segmentos%20com%20serial.pdf) | 423 KB | Enunciado: enviar pelo terminal serial um valor de 0 a 99 e mostrá-lo em dois displays de 7 segmentos; montagem em protoboard com Bluetooth ou conversor USB-serial FTDI. |
| [Exercicio 2026-09-01 - Comunicação em Anel e displays de 7 segmentos.pdf](atividades/Exercicio%202026-09-01%20-%20Comunica%C3%A7%C3%A3o%20em%20Anel%20e%20displays%20de%207%20segmentos.pdf) | 154 KB | Enunciado: três microcontroladores ligados em anel pela serial; o terminal envia um valor de 0 a 99 endereçado a um deles, que o mostra em dois displays de 7 segmentos (simulador). |
| [Exercicio 2026-08-25 - Serial com Display de 7 segmentos - TextoSerial.zip](atividades/Exercicio%202026-08-25%20-%20Serial%20com%20Display%20de%207%20segmentos%20-%20TextoSerial.zip) | 180 KB | Projeto de apoio ao exercício de 25/08: serial com display de 7 segmentos, variação que trata texto recebido pela serial (`SERIALDISPLAY.pbas` + Proteus). |
| [Exercicio 2026-08-25 - Serial com Display de 7 segmentos.zip](atividades/Exercicio%202026-08-25%20-%20Serial%20com%20Display%20de%207%20segmentos.zip) | 143 KB | Projeto de apoio ao exercício de 25/08: envio de valores pela serial para display de 7 segmentos (`SERIALDISPLAY.pbas` + Proteus + esquemático PDF). |
| [Exercicio 2026-09-01 - Comunicacao em Anel.zip](atividades/Exercicio%202026-09-01%20-%20Comunicacao%20em%20Anel.zip) | 211 KB | Projeto de apoio ao exercício de 01/09: comunicação em anel com dois microcontroladores (`MCU01`, `MCU02`) e displays de 7 segmentos. |
| [Exercicio 2026-09-08 - Intermitência com Interrupção.pdf](atividades/Exercicio%202026-09-08%20-%20Intermit%C3%AAncia%20com%20Interrup%C3%A7%C3%A3o.pdf) | 151 KB | Enunciado: três LEDs em sequência a cada 200 ms; com interrupção em RA2 os três piscam juntos a cada 500 ms e, ao fim dela, a sequência continua de onde parou. Tudo por interrupções, com cristal de 4 MHz, em simulador e protoboard. |
| [Trabalho 01 - Controle de multiplexação com interrupção.docx](atividades/Trabalho%2001%20-%20Controle%20de%20multiplexa%C3%A7%C3%A3o%20com%20interrup%C3%A7%C3%A3o.docx) | 161 KB | Modelo de relatório + enunciado do Trabalho 01: PIC16F690 recebe pela serial um valor de 0 a 999 e mostra em três displays de 7 segmentos multiplexados; cristal oscilador e interrupção por timer são obrigatórios. |

## Atividades e avaliações

Enunciados transcritos em texto, com as figuras descritas: [atividades/ENUNCIADOS.md](atividades/ENUNCIADOS.md).

| Tipo | Atividade | Abertura | Prazo | O que pede | Anexo |
|------|-----------|----------|-------|------------|-------|
| Tarefa | [11/08/2026 - Controle por Comunicação Serial](https://missaosalesiana.mrooms.net/mod/assign/view.php?id=254046) | 11 ago. 2026, 19:05 | 18 ago. 2026, 20:45 | Desenvolver o projeto de comunicação serial de acordo com o documento em anexo. | [Exercicio 2026-08-11 - Comunicação entre microcontroladores.pdf](atividades/Exercicio%202026-08-11%20-%20Comunica%C3%A7%C3%A3o%20entre%20microcontroladores.pdf) |
| Tarefa | [18/08/2026 - Envio de valores a displays de 7 segmentos.](https://missaosalesiana.mrooms.net/mod/assign/view.php?id=255537) | 18 ago. 2026, 19:05 | 25 ago. 2026, 23:59 | Desenvolver o projeto do documento em anexo para envio de valores por comunicação serial. | [Exercicio 2026-08-25 - Display de sete segmentos com serial.pdf](atividades/Exercicio%202026-08-25%20-%20Display%20de%20sete%20segmentos%20com%20serial.pdf) |
| Tarefa | [25/09/2026 - Comunicação Serial em Anel](https://missaosalesiana.mrooms.net/mod/assign/view.php?id=256558) | 25 ago. 2026, 19:05 | 1 set. 2026, 23:59 | Desenvolver o projeto do documento em anexo. | [Exercicio 2026-09-01 - Comunicação em Anel e displays de 7 segmentos.pdf](atividades/Exercicio%202026-09-01%20-%20Comunica%C3%A7%C3%A3o%20em%20Anel%20e%20displays%20de%207%20segmentos.pdf) |
| Tarefa | [Exercício - 2026-09-15 Intermitência com interrupção](https://missaosalesiana.mrooms.net/mod/assign/view.php?id=259252) | 15 set. 2026, 19:05 | 22 set. 2026, 23:59 | Desenvolver o projeto do documento em anexo para aplicar os conhecimentos sobre interrupções. | [Exercicio 2026-09-08 - Intermitência com Interrupção.pdf](atividades/Exercicio%202026-09-08%20-%20Intermit%C3%AAncia%20com%20Interrup%C3%A7%C3%A3o.pdf) |
| Tarefa | [TRABALHO 01 - Interrupção com recepção de dados. Interrupção e comunicação.](https://missaosalesiana.mrooms.net/mod/assign/view.php?id=259824) | 22 set. 2026, 19:05 | 6 out. 2026, 23:59 | Desenvolver o trabalho para avaliação de acordo com o documento em anexo, cujo o tema é o tratamento de interrupções e cristal oscilador. | [Trabalho 01 - Controle de multiplexação com interrupção.docx](atividades/Trabalho%2001%20-%20Controle%20de%20multiplexa%C3%A7%C3%A3o%20com%20interrup%C3%A7%C3%A3o.docx) |
