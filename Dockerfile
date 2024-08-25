# Use a imagem oficial do Python
FROM python:3.10-slim

# Defina o diretório de trabalho
WORKDIR /app

# Instale as dependências
COPY ./app/requirements/main.txt .
RUN pip install --no-cache-dir -r main.txt

# Comando para rodar a aplicação
CMD ["bash", "start.sh"]

