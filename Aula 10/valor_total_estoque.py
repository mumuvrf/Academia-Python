import json

preco = 0
with open("Aula 10/estoque.json", 'r') as estoque_json:
    estoque = estoque_json.read()
    produtos = json.loads(estoque)
    print(produtos['produtos'])
    for produto in produtos['produtos']:
        preco += produto['quantidade']*produto['valor']

print(preco)