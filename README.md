# Características de Repositórios Populares do GitHub

Este repositório contém a implementação e resultados do estudo “Características de repositórios populares”, desenvolvido como parte do Laboratório de Experimentação de Software.

O objetivo principal foi mapear propriedades de sistemas open-source populares no GitHub, analisando 1.000 repositórios com maior número de estrelas.

## Questões de Pesquisa (RQs)

* **RQ01:** Sistemas populares são maduros/antigos?
* **RQ02:** Sistemas populares recebem muita contribuição externa?
* **RQ03:** Sistemas populares lançam releases com frequência?
* **RQ04:** Sistemas populares são atualizados com frequência?
* **RQ05:** Sistemas populares são escritos nas linguagens mais populares?
* **RQ06:** Sistemas populares possuem um alto percentual de issues fechadas?
* **RQ07:** Sistemas escritos em linguagens mais populares recebem mais contribuição externa, lançam mais releases e são atualizados com mais frequência?

## Metodologia
##### 1. Coleta de dados
* Utilização da API GraphQL do GitHub.
* Consulta paginada (10 repositórios por requisição).
* Amostra de 1.000 repositórios mais estrelados.

##### 2. Tratamento dos dados
* Armazenamento em arquivos .csv.
* Métricas extraídas: idade, PRs aceitos, releases, tempo da última atualização, linguagem principal, issues abertas/fechadas.

##### 3. Análise
* Exploração estatística das variáveis.
* Teste das hipóteses (H0 e H1) associadas a cada RQ.

## Estrutura do Repositório
```
├── code/              
│   └── analytics.py 
|   └── main.py
├── LAB_1__Caracteristicas_de_repositorios_populares.pdf 
├──Relatorio_analise_das_RQs.pbix
├──collected_repos.csv
└── README.md
```

## Execução do Script de Coleta

O script collect_data.py realiza a coleta dos repositórios mais populares no GitHub.

#### Pré-requisitos

* Python 3.8+

* Biblioteca requests

* Token de acesso pessoal do GitHub (necessário para autenticação na API GraphQL)

```
# Instalar dependências
pip install requests

# Executar coleta
python scripts/collect_data.py --token SEU_TOKEN_AQUI
```

Os dados serão salvos em data/repositories.csv.

## Principais Achados

* Repositórios populares têm em média 8 anos de idade, mas projetos recentes também alcançam grande visibilidade.

* A maioria recebe contribuições externas moderadas, com poucos casos extremos.

* Grande parte lança releases de forma moderada, embora existam outliers com centenas de versões.

* 75% dos projetos foram atualizados nos últimos 109 dias, mostrando atividade frequente.

* Python, TypeScript e JavaScript concentram a maioria dos projetos populares.

* Issues fechadas costumam ter alto percentual em repositórios ativos, mas com exceções.

* Linguagens populares não garantem maior engajamento — comunidades e práticas de governança têm mais peso.