# Htmotor
HTML Template Engine for Python!

## Installation:
Open your terminal and type `pip install htmotor`. Now you are ready to go!

## Supports:
- Variables
- For Loop
- Eval, Exec
- XSS Preventation

## Documentation:
Documentation is avaible at [GitHub](https://github.com/5elenay/htmotor).

## Bug? Issue?
If you got an error or bug, please report at [here](https://github.com/5elenay/htmotor/issues).

## Simple Example
if you want to see htmotor syntax, here you go:
```html
<!DOCTYPE html>
<html lang="en">
<head>
        {% responsive %}
        <title>{%v title %}</title>
</head>
<body>
        <h1>{%v name %}</h1>
        {%ex import datetime %}
        <p>Datetime: {%ev datetime.datetime.utcnow().strftime("%d/%m/%Y, %H:%M:%S") %}</p>
</body>
</html>
```