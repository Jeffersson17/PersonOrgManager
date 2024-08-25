# Use a imagem oficial do Python
FROM python:3.10-slim

# Defina o diretório de trabalho
WORKDIR /app

# Instale as dependências
COPY ./app/requirements/main.txt .
RUN pip install --no-cache-dir -r main.txt

# Copie o código da aplicação
COPY . .

# Expor a porta usada pelo Django
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["bash", "start.sh"]

