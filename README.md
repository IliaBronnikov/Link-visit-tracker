# Link-visit-tracker 
## Web-приложение для простого учета посещенных (неважно, как, кем и когда) ссылок. 

### Приложение предоставляет два HTTP ресурса.
- Ресурс загрузки посещений:
  - #### Запрос
  ```
  POST /visited_links
  {
  "links": [
  "https://ya.ru", "https://ya.ru?q=123", "funbox.ru",
  "https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor"
  ]
  }
  ```
  - #### Ответ
  ```
  {
  "status": "ok"
  }
```

- Ресурс получения статистики:
    - #### Запрос
```
GET /visited_domains?start=1545221231&end=1545217638
```
  - #### Ответ
```
{
"domains": [
"ya.ru",
"funbox.ru", "stackoverflow.com"
],
"status": "ok"
}
```

