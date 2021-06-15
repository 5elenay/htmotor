# For Loops.
For loops in htmotor is really simple.
```html
{%f i in range(1, 11) do %}
    <a href="">{%fv i %}</a>
{% end %}
```
in Python:
```py
for i in range(1, 11):
    print(f"<a href="">{i}</a>")
```

## Tags:
### f
Start for loop tag.
- Should be like this: `{%f variable_name in ["abc", "def"] do %}`.
- This code is in python `for variable_name in ["abc", "def"]:`.
### fv
For loop variable.
- Should be like this: `{%fv i %}`.
- This code is in python `i`.

For loops has a built-in XSS protection. Htmotor encodes the for-variable when it renders.