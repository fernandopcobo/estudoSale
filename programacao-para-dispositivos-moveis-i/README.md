# Programação para Dispositivos Móveis I

**Professor:** Prof. Moreira  
**Semestre:** 2026/2 · Engenharia de Computação · UniSALESIANO Araçatuba  
**Curso no Moodle:** [missaosalesiana.mrooms.net/course/view.php?id=16319](https://missaosalesiana.mrooms.net/course/view.php?id=16319) (requer login)  
**Conteúdo conferido em:** 13/10/2026

Desenvolvimento Android nativo com Android Studio, layouts em XML e lógica em Java. As aulas seguem a ordem: criar projeto → `TextView` → `Button` → `EditText` → `ImageView` → multimídia (áudio) e envio em Base64 para API.

## Material de apoio

| Arquivo | Tamanho | O que tem |
|---------|---------|-----------|
| [aula-01-000 Criando um Projeto no Android Studio.pdf](material-de-apoio/aula-01-000%20Criando%20um%20Projeto%20no%20Android%20Studio.pdf) | 1,2 MB | Passo a passo do primeiro projeto no Android Studio: New Project, template *Empty Views Activity*, configuração (nome, Java) e os arquivos iniciais `MainActivity.java` e `activity_main.xml` — XML é a parte visual, Java o comportamento. 13 slides. |
| [Aula-01-001 TextView.pdf](material-de-apoio/Aula-01-001%20TextView.pdf) | 320 KB | Componente `TextView`: para que serve, como inserir pelo editor Design ou direto no XML, atributos mais usados (id, tamanho, cor, alinhamento) e troca do texto em tempo de execução pelo Java. 13 slides. |
| [Aula-02 Botoes.pdf](material-de-apoio/Aula-02%20Botoes.pdf) | 341 KB | Componente `Button`: inserção no layout, atributos e tratamento do clique em Java para executar uma ação. 16 slides. |
| [Aula-02 Entrada de texto.pdf](material-de-apoio/Aula-02%20Entrada%20de%20texto.pdf) | 348 KB | Componente *Plain Text* (`EditText`): campo de entrada digitada pelo usuário, `inputType`, leitura do valor no Java. Ideia-chave: `TextView` mostra, `EditText` recebe. 15 slides. |
| [aula-02 Imagens.pdf](material-de-apoio/aula-02%20Imagens.pdf) | 269 KB | Componente `ImageView` com imagens locais: pasta `res/drawable`, regras de nome de arquivo (minúsculas, números e `_`), referência por `@drawable/nome`, redimensionamento. 11 slides. |
| [aula-06 multimidia e base64.pdf](material-de-apoio/aula-06%20multimidia%20e%20base64.pdf) | 516 KB | Multimídia e Base64: permissão `RECORD_AUDIO` no manifest e em tempo de execução (Android 6+), gravação com `MediaRecorder`, reprodução com `MediaPlayer` e codificação Base64 para envio a uma API em segundo plano. Estudo de caso: app Chamado Técnico. 8 slides. |

## Atividades e avaliações

| Tipo | Atividade | Abertura | Prazo | O que pede | Anexo |
|------|-----------|----------|-------|------------|-------|
| Tarefa | [Atividade Realizada em Sala de Aula em 21 e 29 de Agosto](https://missaosalesiana.mrooms.net/mod/assign/view.php?id=256058) | 21 ago. 2026, 22:30 | 28 ago. 2026, 23:59 | Deve ser entregue o exercicio da Media das 4 notas O exercicio do IMC poder ser enviado, é opcional mandar ele. | — |
| Tarefa | [app Chamado Tecnico feito em sala no dia 04/09/2026](https://missaosalesiana.mrooms.net/mod/assign/view.php?id=258261) | 4 set. 2026, 00:00 | 6 set. 2026, 23:59 | — | — |
| Tarefa | [Aplicativo de Chamado Tecnico com Som](https://missaosalesiana.mrooms.net/mod/assign/view.php?id=259793) | 18 set. 2026, 00:00 | 19 set. 2026, 23:59 | exercicio feito em sala de aula onde implementamos a gravacao de audio, reproducao e envio para a API | — |
| Tarefa | [Criar um app com um jogo de Animais x Sons](https://missaosalesiana.mrooms.net/mod/assign/view.php?id=260636) | 25 set. 2026, 21:30 | 25 set. 2026, 23:20 | Vamos praticar neste app o uso das classes multimidia para reproduzir sons e imagens clicaveis alem de campos texto e botoes na tela. | — |
