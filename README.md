Claro! Aqui está o README corrigido para refletir que os exercícios foram feitos utilizando Python:

---

# Repositório: Exercícios para Teste de Desenvolvedor da Target Systems

Este repositório contém uma série de 5 exercícios técnicos propostos para avaliação no processo seletivo de desenvolvedor da Target Systems. Os exercícios envolvem lógica de programação, manipulação de dados e implementação de soluções utilizando Python.

## Exercícios

### 1. **Cálculo da Soma com Loop**
Dado o trecho de código abaixo:
```plaintext
int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
```
Ao final do processamento, qual será o valor da variável `SOMA`?

### 2. **Sequência de Fibonacci**
Escreva um programa que calcule a sequência de Fibonacci, onde se inicia por 0 e 1, e o próximo valor sempre será a soma dos dois valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...).

O programa deve:
- Receber um número (através de entrada ou pré-definido).
- Calcular a sequência de Fibonacci até esse número.
- Verificar se o número informado pertence à sequência.

### 3. **Faturamento Diário de uma Distribuidora**
Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa que:
- Calcule o menor valor de faturamento ocorrido em um dia do mês.
- Calcule o maior valor de faturamento ocorrido em um dia do mês.
- Calcule o número de dias em que o faturamento diário foi superior à média mensal.

**Importante:**
- Os dados do faturamento devem ser extraídos de um arquivo JSON ou XML.
- Ignorar os dias sem faturamento (finais de semana e feriados).

### 4. **Percentual de Representação por Estado**
Dado o valor de faturamento mensal de uma distribuidora por estado:
- **SP** – R$67.836,43
- **RJ** – R$36.678,66
- **MG** – R$29.229,88
- **ES** – R$27.165,48
- **Outros** – R$19.849,53

Escreva um programa que calcule o percentual de representação de cada estado dentro do valor total mensal da distribuidora.

### 5. **Inversão de String**
Escreva um programa que inverta os caracteres de uma string informada.

**Importante:**
- A string pode ser fornecida por entrada ou pré-definida no código.
- Evite usar funções prontas, como `reverse`.

---

## Como Rodar o Código

1. Clone este repositório para sua máquina local:
   ```bash
   git clone <URL_DO_REPOSITÓRIO>
   ```

2. Navegue até a pasta do repositório:
   ```bash
   cd <nome_do_repositório>
   ```

3. Execute os programas utilizando Python:
   ```bash
   python3 <nome_do_arquivo>.py
   ```
