# Análise de Cenários

## TCP:

- Cenário Ideal: Comunicação confiável, como transações financeiras, aplicações que requerem a entrega garantida de dados (ex.: navegação web, download de arquivos).
- Vantagens: Confiabilidade, controle de congestionamento, retransmissão de pacotes.
- Limitações: Sobrecarga de conexão e controle de fluxo, tempo de resposta maior.

## UDP:

- Cenário Ideal: Aplicações que priorizam velocidade sobre confiabilidade, como streaming de vídeo, transmissão de áudio ou DNS.
- Vantagens: Menor latência, sem necessidade de estabelecer conexão.
- Limitações: Não há garantia de entrega, pacotes podem ser perdidos, falta de controle de fluxo.

## Resumo dos Testes de Desempenho

- TCP geralmente tem um tempo de resposta maior devido ao estabelecimento de conexão e mecanismos de controle.
- UDP é mais rápido para grandes quantidades de requisições, porém apresenta risco de perda de pacotes, o que pode não ser ideal para transferências de dados críticos.

# Tempo das 10 mil requisições

| TCP: Time taken for 10,000 requests: 4.40 seconds
| UDP: Time taken for 10,000 requests: 3.48 seconds