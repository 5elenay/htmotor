# Variables
Variables in htmotor is really simple. You will send a variable when render and it will replace the syntax with your variable.

## Example:
Python Code:
```py
from htmotor import HTML

motor = HTML(prevent_xss=True) # if you don't know what is this option. check PreventXSS.md

print(motor.render_file(
    "file.htmo", 
    message="Hello from Back-end!"
)) # we can send more variable like this:
# print(motor.render_file(
#   "file.htmo", 
#   message="Hello from Back-end!",
#   another_variable="Hello!"
# ))
```
file.htmo:
```html
<h1>{%v message %}</h1>
```
Now it will encode our htmo file and print the result.

## Disable XSS Protection:
If you enabled prevent_xss, You may want to render a variable without encoding. To make this:
```py
from htmotor import HTML

motor = HTML(prevent_xss=True)

print(motor.render_file(
    "file.htmo", 
    safe="<p>Safe Variable</p>",
    unsafe=("<p>Unsafe Variable</p>", False) # Now we closed the xss protection for this variable.
))
```

## Tags:
### v
Get a variable.
- Should be like this: `{%v a_variable %}`.
- This code is in python `a_variable`.