# Clima para Agricultura: Integração de Ontologia com Aplicações de Voz

## Descrição do Domínio
Este projeto integra uma ontologia no domínio de "Clima para Agricultura" com uma aplicação de voz. A ontologia modela conceitos relacionados ao clima e sua influência na agricultura, incluindo classes como `Precipitação`, `Temperatura`, `Umidade`, suas propriedades e relações.

## Estrutura do Projeto
- **Ontologia**: Arquivo OWL criado no Protégé.
- **Aplicação Python**: Interpreta comandos de voz, consulta a ontologia e sintetiza respostas em áudio.
- **Documentação**: Este arquivo `README.md`.

## Como Executar
1. Instale as dependências: `pip install -r requirements.txt`
2. Execute a aplicação: `python src/main.py`
3. Fale um comando relacionado ao clima para agricultura.
4. Ouça a resposta sintetizada.

## Exemplo de Uso
- Comando: "Qual é a previsão de chuva para amanhã?"
- Resposta: "A previsão de chuva para amanhã é de 20%."

## Instruções para Desenvolvimento
- Modifique o arquivo `ontology_query.py` para ajustar as consultas SPARQL conforme necessário.
- Atualize o arquivo OWL no Protégé para refletir mudanças na ontologia.