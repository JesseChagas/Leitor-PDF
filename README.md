# Programa Python para extrair texto e imagens de arquivos PDF

Este programa Python usa a biblioteca PyPDF2 para ler arquivos PDF e extrair o texto e as imagens.

## Como usar o programa

1. Instale o PyPDF2: `pip install PyPDF2`

2. Baixe o arquivo `extrair_pdf.py` deste repositório e coloque-o na pasta do seu projeto.

3. Substitua `'arquivo.pdf'` no arquivo `extrair_pdf.py` pelo nome do arquivo PDF que deseja ler.

4. Execute o programa usando o seguinte comando: `python extrair_pdf.py`

O programa extrairá o texto e as imagens do arquivo PDF especificado e exibirá o texto na saída padrão e salvará as imagens em arquivos na pasta do projeto.

## Dependências

- PyPDF2
- PIL (Python Imaging Library)

Você pode instalar as dependências usando o comando `pip install <nome_da_dependencia>`. 

Observe que este programa pode não funcionar corretamente com todos os arquivos PDF. Alguns arquivos PDF podem conter outros tipos de conteúdo, como formulários ou scripts, que não podem ser extraídos dessa maneira. Além disso, este programa não trata o caso de arquivos PDF criptografados ou protegidos por senha. 

## Contribuições

Se você quiser contribuir para este projeto, sinta-se à vontade para enviar um pull request ou abrir uma issue.
