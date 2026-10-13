# Técnicas de Segurança em Redes — enunciados das atividades

Transcrição em texto dos roteiros publicados pelo Prof. Me. Hericson dos Santos, para leitura sem abrir os arquivos. As figuras dos PDFs estão descritas entre colchetes; o arquivo original continua sendo a referência.

As duas atividades são práticas: dependem do laboratório (Kali Linux e Windows em rede Host-Only) e a entrega é feita com prints da sua própria execução.

## Atividade 1 — Wireshark

Publicada em 05/09/2026 · prazo 30/09/2026, 23:59 · original: [Atividade1 - WireShark.pdf](<Atividade1 - WireShark.pdf>)

**1. Exercício prático com Wireshark no Kali Linux com serviço Telnet**

Deixe o Wireshark rodando no Kali Linux na porta que está conectada com o Windows (possivelmente é a porta `eth1`).

A) Serviço Telnet ativo no Kali Linux na porta 18000:

    nc -lvnp 18000

B) No Windows, com o PowerShell, execute:

    $client = New-Object System.Net.Sockets.TcpClient("<ip_do_kali_linux>",18000)

C) Verifique o que acontece no Kali Linux. Faça um print e coloque no documento da atividade.

D) Configure o Windows para enviar uma mensagem para o Kali. No PowerShell execute os comandos:

    $stream = $client.GetStream()
    $writer = New-Object System.IO.StreamWriter($stream)
    $writer.AutoFlush = $true

E) Envie a mensagem para o Kali. No PowerShell execute:

    $writer.WriteLine("Olá, meu nome é ..., esta mensagem esta trafegando pela rede!")

F) Observe a transmissão de dados no Kali Linux. Faça um print e coloque no documento da atividade.

G) No Wireshark, filtre pela porta que você configurou o serviço Telnet (18000) e localize os dados interceptados pelo Wireshark.

[Figura: painel de detalhes do Wireshark com as camadas Frame, Ethernet II, Internet Protocol, Transmission Control Protocol e o campo Data selecionado.]

H) Print e informação, conforme exemplo.

[Figura: visão hexadecimal do pacote com os bytes do campo Data destacados e, ao lado, o texto da mensagem enviada legível em ASCII.]

## Atividade 2 — NMAP

Publicada em 22/09/2026 · prazo 30/09/2026, 23:59 · original: [Atividade 2 - NMAP.pdf](<Atividade 2 - NMAP.pdf>)

1. De acordo com as aulas 6 (Linux) e 7 (NMAP), reproduza os passos mostrados em aula em sua rede local. Print as saídas e gere um PDF para entrega.

       nmap 192.168.56.20          <host>
       nmap -p- 192.168.56.20      <portas>
       nmap -sV 192.168.56.20      <serviços>
       sudo nmap -O 192.168.56.20  <sistema operacional>

2. Caso a sua descoberta de redes apresente portas abertas, identifique-as e pesquise quais serviços estão relacionados a elas.
