
# берем образ python версии 3.12
FROM python:3.12

# создаем директорию app
WORKDIR /app

# копируем в директорию app файл с внешними зависимостями 
COPY requirements.txt .

# устанавливаем зависимости проекта 
RUN pip install -r requirements.txt

# копируем в директорию app все файлы проекта
COPY . .

# запускаем pytest с генерация отчета через allure 
CMD ["pytest", "--alluredir", "allure-results"]