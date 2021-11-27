# Link-visit-tracker 
## Web-приложение для простого учета посещенных (неважно, как, кем и когда) ссылок. 

### Приложение предоставляет два HTTP ресурса.
- Ресурс загрузки посещений:
  - Запрос
  ```
  POST /visited_links
  {
  "links": [
  "https://ya.ru", "https://ya.ru?q=123", "funbox.ru",
  "https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor"
  ]
  }
  ```
  - Ответ
  ```
  {
  "status": "ok"
  }
  ```

- Ресурс получения статистики:
    - Запрос
  ```
  GET /visited_domains?start=1545221231&end=1545217638
  ```
  - Ответ
  ```
  {
  "domains": [
  "ya.ru",
  "funbox.ru", "stackoverflow.com"
  ],
  "status": "ok"
  }
  ```
  
### Запуск проекта

- Собрать образ 
```
docker-compose up
```
- Образ redis работает на порту 6379
- Сервис доступен по адресу http://127.0.0.1:8000/
- POST запрос
  ```
  curl --location --request POST 'http://127.0.0.1:8000/visited_links/' --header 'Content-Type: application/json' --data-raw '{"links": ["https://ya.ru", "https://ya.ru?q=123", "funbox.ru", "https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor"]}'
  ```
- GET запрос
  ```
  curl --location --request GET '/visited_domains?start=13&end=9999999999999'
  ```
 

