# Técnicas de Segurança em Redes

**Professor:** Prof. Me. Hericson dos Santos  
**Semestre:** 2026/2 · Engenharia de Computação · UniSALESIANO Araçatuba  
**Curso no Moodle:** [missaosalesiana.mrooms.net/course/view.php?id=17428](https://missaosalesiana.mrooms.net/course/view.php?id=17428) (requer login)  
**Conteúdo conferido em:** 13/10/2026

Apostilas numeradas, uma por aula, que constroem passo a passo um laboratório virtual (VirtualBox + Kali Linux + Metasploitable 3) e o usam para análise de tráfego (Wireshark) e reconhecimento (NMAP), fechando o bimestre com ameaças, malware e legislação.

## Links da disciplina

- [Evidências da atividade da aula 1 (download)](https://drive.google.com/uc?export=download&id=1HX8dkeTtT3nGp-TUOQs98px_Yf-5JcP_)
- [Kali Linux — máquinas virtuais](https://www.kali.org/get-kali/#kali-virtual-machines)
- [Vídeo de apoio da Atividade 1 (Wireshark)](https://drive.google.com/file/d/1-b5RDgIjA1nX984rECOwk8YDL9Q5f2Fu/preview)

## Geral

| Arquivo | Tamanho | O que tem |
|---------|---------|-----------|
| [Simulado 1 - Segurança de Redes.pdf](geral/Simulado%201%20-%20Seguran%C3%A7a%20de%20Redes.pdf) | 314 KB | Simulado do 1º bimestre: 30 questões de múltipla escolha sobre o conteúdo das apostilas (sem gabarito). 6 páginas. |

## Material de apoio

| Arquivo | Tamanho | O que tem |
|---------|---------|-----------|
| [1 - Apostila de Introdução à Cybersecurity.pdf](material-de-apoio/1%20-%20Apostila%20de%20Introdu%C3%A7%C3%A3o%20%C3%A0%20Cybersecurity.pdf) | 1,1 MB | Aula 1 — Introdução à cibersegurança: apresentação da disciplina, pilares pessoas/processos/tecnologias e a tríade confidencialidade, integridade e disponibilidade. 7 páginas. |
| [2 - Funções Hash e Criptografia.pdf](material-de-apoio/2%20-%20Fun%C3%A7%C3%B5es%20Hash%20e%20Criptografia.pdf) | 1,7 MB | Aula 2 — Hash e criptografia: função hash e integridade, por que hash não é criptografia, principais algoritmos; texto claro × cifrado, chave, criptografia simétrica e assimétrica; ransomware como uso malicioso da criptografia (contaminação e defesa); atividade e questões de fixação. 17 páginas. |
| [3 - Iniciando a Construção do Laboratório de Segurança.pdf](material-de-apoio/3%20-%20Iniciando%20a%20Constru%C3%A7%C3%A3o%20do%20Laborat%C3%B3rio%20de%20Seguran%C3%A7a.pdf) | 1,0 MB | Aula 3 — Início do laboratório: requisitos de hardware, conceitos de virtualização, instalação do VirtualBox e primeiros passos no Kali Linux (comandos básicos, ferramentas, diagnóstico de rede). 12 páginas. |
| [4 - Análise de Tráfego de Redes com Wireshark.pdf](material-de-apoio/4%20-%20An%C3%A1lise%20de%20Tr%C3%A1fego%20de%20Redes%20com%20Wireshark.pdf) | 3,9 MB | Aula 4 — Wireshark: captura de pacotes (local, espelhamento de porta, TAP), instalação, interface, primeira captura e geração de tráfego para análise. 22 páginas. |
| [5 - Construindo o Laboratório de Segurança de Redes.pdf](material-de-apoio/5%20-%20Construindo%20o%20Laborat%C3%B3rio%20de%20Seguran%C3%A7a%20de%20Redes.pdf) | 1,5 MB | Aula 5 — Laboratório completo: importação da Metasploitable 3 e configuração dos adaptadores de rede (Host-Only) no VirtualBox. 7 páginas. |
| [6 - Alguns Comados do Kali Linux.pdf](material-de-apoio/6%20-%20Alguns%20Comados%20do%20Kali%20Linux.pdf) | 492 KB | Aula 6 — Comandos do Kali Linux: navegação e manipulação de arquivos, root, principais ferramentas e comandos de rede (`ifconfig`, `ping`, `traceroute`, `arp`, `netstat`/`ss`). 4 páginas. |
| [7 - Mapeamento de Redes com NMAP.pdf](material-de-apoio/7%20-%20Mapeamento%20de%20Redes%20com%20NMAP.pdf) | 1,0 MB | Aula 7 — NMAP: o que é reconhecimento, NMAP × Wireshark, revisão de host/IP/porta/serviço e primeiras varreduras no laboratório. 8 páginas. |
| [8 - Cybersegurança e legislação.pdf](material-de-apoio/8%20-%20Cyberseguran%C3%A7a%20e%20legisla%C3%A7%C3%A3o.pdf) | 1,9 MB | Aula 8 — Cibersegurança e legislação: ameaça, vulnerabilidade, risco, ataque e incidente; malware; legislação e principais crimes digitais. 12 páginas. |

## Arquivos das atividades

| Arquivo | Tamanho | O que tem |
|---------|---------|-----------|
| [Atividade1 - WireShark.pdf](atividades/Atividade1%20-%20WireShark.pdf) | 398 KB | Roteiro da Atividade 1: capturar com o Wireshark no Kali uma sessão em texto claro (netcat na porta 18000 × cliente TCP no PowerShell) e entregar prints com as informações pedidas. 2 páginas. |
| [Atividade 2 - NMAP.pdf](atividades/Atividade%202%20-%20NMAP.pdf) | 228 KB | Roteiro da Atividade 2: varreduras NMAP na rede local (hosts, portas, serviços `-sV`, sistema operacional `-O`), com prints em PDF. |

## Atividades e avaliações

Enunciados transcritos em texto, com as figuras descritas: [atividades/ENUNCIADOS.md](atividades/ENUNCIADOS.md).

| Tipo | Atividade | Abertura | Prazo | O que pede | Anexo |
|------|-----------|----------|-------|------------|-------|
| Tarefa | [Atividade 1 - Wireshark](https://missaosalesiana.mrooms.net/mod/assign/view.php?id=258302) | 5 set. 2026, 23:59 | 30 set. 2026, 23:59 | A atividade traz os conceitos de protocolos de comunicação, protocolos de testes, camada OSI e a interceptação de informações e pacotes com o Wireshark. | [Atividade1 - WireShark.pdf](atividades/Atividade1%20-%20WireShark.pdf) |
| Tarefa | [Atividade 2 - NMAP](https://missaosalesiana.mrooms.net/mod/assign/view.php?id=259834) | 22 set. 2026, 19:00 | 30 set. 2026, 23:59 | De acordo com aula de NMAP realize uma varredura em sua rede. | [Atividade 2 - NMAP.pdf](atividades/Atividade%202%20-%20NMAP.pdf) |
