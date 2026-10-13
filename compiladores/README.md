# Compiladores

**Semestre:** 2026/2 · Engenharia de Computação · UniSALESIANO Araçatuba  
**Curso no Moodle:** [missaosalesiana.mrooms.net/course/view.php?id=17434](https://missaosalesiana.mrooms.net/course/view.php?id=17434) (requer login)  
**Conteúdo conferido em:** 13/10/2026

O semestre gira em torno do projeto de um compilador para uma linguagem tipo Pascal: primeiro o autômato e o analisador léxico (B1), depois a análise sintática a partir da gramática fornecida.

## Links da disciplina

- [Plano/documento da disciplina (PDF no Google Drive)](https://drive.google.com/file/d/1moFJWeX7rnm3ojpbQuOiU5wPdGgCMhQj/view?usp=sharing)
- [Livro "Compiladores - Princípios, Técnicas e Ferramentas" (link indicado pelo professor)](https://drive.google.com/file/d/1XKhHcLJBQc1zffAUQXoJBWmBbReUYsWJ/view?usp=sharing)

## Material de apoio

| Arquivo | Tamanho | O que tem |
|---------|---------|-----------|
| [ApostilaCompiladores.pdf](material-de-apoio/ApostilaCompiladores.pdf) | 370 KB | Apostila "Compiladores I" (2006, 53 páginas): teoria dos compiladores e fases (análise e síntese); análise léxica (tokens, bufferização, expressões regulares, diagramas de transição, autômatos finitos determinísticos e não determinísticos); análise sintática (erros, gramáticas livres de contexto, ambiguidade, EBNF, descendente recursiva, preditivos); especificações Lex. |
| [JFlap.rar](material-de-apoio/JFlap.rar) | 8,4 MB | JFLAP (`JFLAP.jar`) para desenhar e simular autômatos, com um exemplo (`Amigos.jff`). Requer Java. |
| [Léxico - Desenho.jpg](material-de-apoio/L%C3%A9xico%20-%20Desenho.jpg) | 2,9 MB | Imagem do autômato do analisador léxico do projeto (diagrama de estados completo). |
| [Gramática.pdf](material-de-apoio/Grama%CC%81tica.pdf) | 170 KB | Gramática do projeto de compilador em BNF estendida: programa, declarações, tipos (`integer`, `boolean`, `real`, `char`), comandos (atribuição, leitura, escrita, composto, condicional, repetição) e expressões. 1 página. |
| [Exemplo Codigo Lex.docx](material-de-apoio/Exemplo%20Codigo%20Lex.docx) | 17 KB | Exemplo de analisador léxico em C: função `Lex()` como máquina de estados (`switch` de estado e de caractere) reconhecendo operadores, identificadores e números. |

## Atividades e avaliações

| Tipo | Atividade | Abertura | Prazo | O que pede | Anexo |
|------|-----------|----------|-------|------------|-------|
| Tarefa | [Autômato da Linguagem](https://missaosalesiana.mrooms.net/mod/assign/view.php?id=256081) | 21 ago. 2026, 00:00 | 21 ago. 2026, 23:59 | Envie o autômato criado em formato de PDF ou Imagem Somente um aluno do grupo envia. Coloque o nome de todos os integrantes | — |
| Tarefa | [B1](https://missaosalesiana.mrooms.net/mod/assign/view.php?id=261282) | 2 out. 2026, 00:00 | 9 out. 2026, 19:00 | Envio projeto completo do léxico. Envie em um arquivo texto o nome de todos os integrantes do grupo. Somente 1 integrante efetua o envio. | — |
