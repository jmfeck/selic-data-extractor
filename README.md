# Extrator de Dados Históricos da Selic

Este projeto tem como objetivo baixar os resultados históricos da taxa Selic e gerar uma tabela detalhada por dia, facilitando a análise e o uso desses dados em diversos contextos.

## Estrutura do Projeto

- **data_outgoing/selic_historica.xlsx**: Arquivo de saída contendo os dados históricos da Selic em formato Excel, para uso e análise.
- **scripts/selic_data_extractor.py**: Script Python que realiza a extração dos dados da Selic a partir de uma fonte online e cria o arquivo de saída.
- **execute_extraction.bat**: Script em lote para facilitar a execução do extrator em sistemas Windows.

## Como Executar

1. Certifique-se de ter o Python 3.x instalado em sua máquina.
2. Instale as dependências necessárias. Navegue até a pasta `scripts` e execute o seguinte comando:
   ```bash
   pip install -r requirements.txt
   ```
   
3. Navegue até a pasta `scripts` e execute o script para realizar a extração dos dados:
   ```bash
   python selic_data_extractor.py
   ```
   
   Ou, se estiver em um sistema Windows, você pode executar o arquivo `.bat` diretamente clicando duas vezes em `execute_extraction.bat`.

## Requisitos

- **Python 3.x**: Certifique-se de que a versão do Python instalada é compatível.
- **Bibliotecas Python**: 
  - `os`
  - `pandas`
  - `datetime`
  - `requests`

## Funcionalidades

- **Extração Automática**: O script conecta-se a uma fonte de dados confiável para obter as informações mais recentes sobre a taxa Selic.
- **Geração de Arquivo Excel**: Os dados extraídos são salvos em um arquivo Excel para facilitar o uso e compartilhamento.
- **Execução Simples**: Possibilidade de executar o script através de um arquivo `.bat` para facilitar a utilização por usuários de Windows que não estão acostumados com a linha de comando.

## Estrutura do Código

O script principal, **selic_data_extractor.py**, está organizado da seguinte forma:

1. **Importação de Bibliotecas**: Importa as bibliotecas necessárias, como `requests` para realizar requisições HTTP e `pandas` para manipulação dos dados.
2. **Definição da Fonte de Dados**: URL da fonte oficial dos dados da Selic.
3. **Extração dos Dados**: Realiza a requisição para obter os dados e transforma-os em um formato processável.
4. **Geração do Arquivo Excel**: Cria um arquivo Excel com os dados históricos da Selic.

## Exemplos de Uso

Você pode usar os dados gerados por este script para:

- Realizar análises financeiras.
- Incorporar os dados em dashboards para acompanhamento de indicadores econômicos.
- Desenvolver modelos de previsão baseados nos dados históricos da taxa Selic.

## Possíveis Melhorias

- **Automatização com Scheduler**: Integrar o script a um scheduler (como o `cron` no Linux) para realizar a extração periodicamente de forma automática.
- **Integração com APIs**: Melhorar a fonte de dados utilizando APIs mais robustas e confiáveis para garantir a precisão das informações.
- **Geração de Gráficos**: Adicionar funcionalidades para geração automática de gráficos que ilustrem a evolução da taxa Selic ao longo do tempo.

## Demonstrativo em Vídeo

*Em breve*

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Autor

- **João M. Feck** - [joaomfeck@gmail.com](mailto:joaomfeck@gmail.com)

Se tiver qualquer dúvida ou sugestão, fique à vontade para entrar em contato!
