# Use a imagem oficial do Python
FROM python:3.10-slim

# Defina o diretório de trabalho
WORKDIR /app

# Instale as dependências
COPY ./client_scheduling/requirements/main.txt .
RUN pip install --no-cache-dir -r main.txt

# Comando para rodar a aplicação
CMD ["bash", "django/start.sh"]
