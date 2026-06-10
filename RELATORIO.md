# Relatório Técnico

## Estrutura de Dados

O sistema utiliza listas (vetores) para armazenar os produtos em memória durante a execução.

## Busca Linear

A busca por nome é realizada utilizando busca linear, percorrendo todos os elementos da lista até encontrar os produtos correspondentes.

Complexidade:

O(n)

Onde n representa a quantidade de produtos cadastrados.

## Busca Binária

A busca por código é realizada utilizando busca binária em um vetor ordenado por código.

Complexidade:

O(log n)

A busca binária foi escolhida por ser mais eficiente para localizar produtos quando a lista está ordenada.

## Persistência de Dados

Os dados são armazenados em arquivo JSON, permitindo que os produtos cadastrados permaneçam disponíveis após o encerramento da aplicação.

## Conclusão

O projeto aplica conceitos de programação em Python, manipulação de arquivos, estruturas de dados, algoritmos de busca e organização modular do código.
