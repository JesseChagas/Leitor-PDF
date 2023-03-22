import PyPDF2
from PIL import Image

# Nome do arquivo PDF a ser lido
filename = 'arquivo.pdf'

# Abre o arquivo PDF em modo binário
with open(filename, 'rb') as pdf_file:
    # Cria um objeto de leitura de PDF
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # Extrai o texto de cada página do PDF
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text = page.extractText()
        print(f'Texto na página {page_num + 1}:\n{text}')

        # Extrai as imagens de cada página do PDF
        xObject = page['/Resources']['/XObject'].getObject()
        for obj in xObject:
            if xObject[obj]['/Subtype'] == '/Image':
                size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
                data = xObject[obj].getData()
                if xObject[obj]['/ColorSpace'] == '/DeviceRGB':
                    mode = "RGB"
                else:
                    mode = "P"

                # Cria a imagem usando a biblioteca PIL
                image = Image.frombytes(mode, size, data)
                image.save(f'imagem_pagina{page_num+1}_{obj[1:]}.png')
