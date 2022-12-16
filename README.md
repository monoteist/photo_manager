# Photo Manager

### Выполнение тестового задания 

#### Сделать REST фото менеджер.

1) Загружать фотографии авторизованным пользователям.

1.1) При загрузке можно указывать различную метадату: гео локацию, описание, имена людей на фото.

2) Отображать список фотографий, без мета данных.

2.2) Фильтровать фотографии по дате.

2.3) Фильтровать фотографии по геолокации.

2.4) Фильтровать фотографии по имени человека.

3) Получать фотографию по айди с метаданными.

4) Дополнительная задача: сделать апи автодополнение по поиску возможных имен людей присутствующих на фотографиях. 

Пример:

Передаем часть имени: "Алекс"

На выходе получаем: Алекс, Алексей, Александр, Александра

Вбиваем: "Алексан"

Получаем: Александр, Александра

Tech stack: Django, Python 3.9+, Any SQL database, DRF is optional


### Установка

#### Docker

Перед установкой убедитесь в том что ваша хост машина подерживает виртуализацию, и в том что она включена.

Для Windows: убедитесь в том что у вас включен компонент Hyper-V.

Затем скачайте и установите Docker, Docker-Compose

#### Запуск

Склонируйте репорзиторий к себе!

Для запуска программы используйте команду:  `docker compose up --build`

Приложение доступно по адресу `http://127.0.0.1:8000/`

#### REST Api

Для просмотра endpoint'ов перейдите по адресу `http://127.0.0.1:8000/api/schema/swagger-ui/#/`