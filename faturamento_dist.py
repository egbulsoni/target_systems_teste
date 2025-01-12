import json

caminho_arquivo = 'dados.json'

with open(caminho_arquivo, 'r') as file:
    faturamento = json.load(file)

faturamento_valido = [item['valor'] for item in faturamento if item['valor'] > 0]

menor_faturamento = min(faturamento_valido)
maior_faturamento = max(faturamento_valido)

media_mensal = sum(faturamento_valido) / len(faturamento_valido)

dias_acima_da_media = sum(1 for item in faturamento if item['valor'] > media_mensal)

print(f"Menor faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior faturamento: R$ {maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
