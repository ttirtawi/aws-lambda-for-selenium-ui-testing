This only works with Python 3.6 and lambda image for python 3.6 only available in x86

```
sam build && sam local invoke SeleniumFunction --event events/event.json
```

sample output

```
{
  "statusCode": 200,
  "body": "{\"text\": \"Seru terooos internetan dengan Telkomsel PraBayar\\nSeru-seruan terus dengan beragam pilihan paket Telkomsel PraBayar.\", \"duration\": 2}"
}
```
