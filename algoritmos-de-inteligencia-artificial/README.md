# Algoritmos de Inteligência Artificial

**Professor:** Prof. Dr. João Augusto Silva Lêdo  
**Semestre:** 2026/2 · Engenharia de Computação · UniSALESIANO Araçatuba  
**Curso no Moodle:** [missaosalesiana.mrooms.net/course/view.php?id=16874](https://missaosalesiana.mrooms.net/course/view.php?id=16874) (requer login)  
**Conteúdo conferido em:** 13/10/2026

Disciplina sobre resolução de problemas por busca: do histórico e fundamentos da IA até a modelagem em espaço de estados e os algoritmos de busca cega, com implementação em Python.

**Avaliação (dos slides):** provas com peso 4 e trabalhos com peso 6 em cada bimestre.

**Sequência de estudo sugerida:** slides → pseudoalgoritmo de cada busca → conferir no `ArvoreDeBusca-v2.py`.

## Material de apoio

| Arquivo | Tamanho | O que tem |
|---------|---------|-----------|
| [Pseudo_Algoritmo_Árvore_Geral.pdf](material-de-apoio/Pseudo_Algoritmo_%C3%81rvore_Geral.pdf) | 34 KB | Pseudoalgoritmo da árvore de busca geral (`GenerateSearchTree`): fronteira, explorado e construção da árvore até o nó objetivo. |
| [Algoritimos_de_IA_Aula.pdf](material-de-apoio/Algoritimos_de_IA_Aula.pdf) | 10,0 MB | Slides da disciplina (87): apresentação e critério de avaliação (provas peso 4, trabalhos peso 6); ementa; visão geral e histórico da IA (de 1773 a 2022); fundamentos e Teste de Turing; otimização linear × problema de busca; espaço de estados; rede e árvore semântica; caixeiro viajante; mundo do aspirador de pó; tipos de problema de busca; árvore de busca e estratégias; busca cega (largura, custo uniforme); preparação do ambiente Python (VS Code, venv). Traz listas de exercícios ao fim de cada bloco. |
| [Pseudo_Algoritmo_Busca_em_Largura.pdf](material-de-apoio/Pseudo_Algoritmo_Busca_em_Largura.pdf) | 35 KB | Pseudoalgoritmo da busca em largura (`BreadthFirstSearch`): fronteira como fila (FIFO). |
| [Pseudo_Algoritmo_Busca_Uniforme.pdf](material-de-apoio/Pseudo_Algoritmo_Busca_Uniforme.pdf) | 37 KB | Pseudoalgoritmo da busca de custo uniforme: fronteira como fila de prioridade pelo custo acumulado. 2 páginas. |
| [ArvoreDeBusca-v1.py](material-de-apoio/ArvoreDeBusca-v1.py) | 3 KB | Implementação em Python, 1ª versão: árvore de busca geral e busca em largura sobre um grafo de 6 nós (A–F), lendo estado inicial e objetivo do teclado. |
| [Pseudo_Algoritmo_Busca_em_Profundidade.pdf](material-de-apoio/Pseudo_Algoritmo_Busca_em_Profundidade.pdf) | 35 KB | Pseudoalgoritmo da busca em profundidade (`DepthFirstSearch`). |
| [ArvoreDeBusca-v2.py](material-de-apoio/ArvoreDeBusca-v2.py) | 6 KB | Implementação em Python, 2ª versão: acrescenta busca de custo uniforme (com `heapq` e grafo ponderado) e busca em profundidade — 4 estratégias no mesmo programa. |
