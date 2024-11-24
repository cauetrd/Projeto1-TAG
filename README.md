# Projeto 1 - Teoria e Aplicação de Grafos (Turma 01, 2/2024)

**Universidade de Brasília**  
**Departamento de Ciência da Computação**  
**Prof. Díbio**

**link para o repositório do projeto:** [link] (https://github.com/cauetrd/Projeto1-TAG)

## Informações do Projeto

Este projeto consiste na implementação de algoritmos para a análise de uma rede social de relações duradouras entre golfinhos, modelada como um grafo não direcionado, baseado no artigo de David Lusseau et al. (2003). Os dados estão contidos no arquivo `soc-dolphins.mtx`.

## Funcionalidades Implementadas

1. Construção de um grafo não direcionado usando listas de adjacências e as biblioteca `networkx` e `matplotlib`.
2. Cálculo do grau de cada vértice.
3. Identificação de todos os cliques maximais usando o algoritmo de Bron-Kerbosch com pivotamento.
4. Cálculo do coeficiente de aglomeração de cada vértice.
5. Cálculo do coeficiente médio de aglomeração do grafo.
6. Visualização do grafo completo, com coloração diferente para cada clique maximal.

## Estrutura do Código

O código foi implementado de forma modular e está organizado nas seguintes funções principais:

- **`obter_dados()`**: Lê os dados do arquivo e constrói o grafo como objeto da biblioteca `networkx` e lista de adjacências.
- **`bron_kerbosch(adjlist)`**: Identifica os cliques maximais utilizando o algoritmo de Bron-Kerbosch com pivotamento.
- **`obter_coeficientes_aglomeracao(grafo)`**: Calcula os coeficientes de aglomeração de cada vértice e o coeficiente médio.
- **`visualizacao_grafo(grafo, cliquesmaximais)`**: Gera uma visualização gráfica do grafo, destacando os cliques maximais.

## Detalhes de Implementação

1. **Entrada**:

   - Arquivo `soc-dolphins.mtx` contendo as relações entre os vértices (golfinhos).

2. **Saída**:
   - Grau de cada vértice.
   - Lista de cliques maximais ordenados pelo tamanho.
   - Coeficiente de aglomeração de cada vértice e coeficiente médio do grafo.
   - Visualização gráfica do grafo.

## Dependências

Certifique-se de ter as seguintes bibliotecas instaladas no Python:

- `networkx`
- `matplotlib`

### Instalação das Dependências

Execute o comando abaixo para instalar as bibliotecas necessárias:

```bash
pip install networkx matplotlib
```

## Como Executar o Código

1. Certifique-se de que o arquivo `soc-dolphins.mtx` está no mesmo diretório do código.
2. Execute o script Python:

```bash
python main.py
```

3. O programa exibirá os resultados no terminal e abrirá uma janela com a visualização do grafo.

## Organização dos Resultados

- **Grau dos Vértices**: Exibe o grau de cada vértice na ordem crescente de índices.
- **Cliques Maximais**: Lista de cliques maximais ordenados pelo tamanho, indicando os vértices que os compõem.
- **Coeficiente de Aglomeração**: Exibe o coeficiente de cada vértice e o coeficiente médio.
- **Visualização do Grafo**: Mostra o grafo completo com coloração diferenciada para os cliques maximais.

## Autor

- Nome: Cauê de Macedo Britto Trindade de Sousa
  Matrícula: 231019003

  Realizado individualmente.
