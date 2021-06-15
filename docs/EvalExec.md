# Eval & Exec.
Eval and exec is usefull when you need to run some python code in htmotor.

## When Should i use Exec or Eval?
- Use eval for when you need to run some function and return a value.
- Use exec when you need to add a code and run it.
- ### Example:
    - Eval: `{%ev time.time() %}`
        - But you can't import a module when you use eval. Instead, use exec.
    - Exec: `{%ex import time %}`
        - Exec does not returns anything. When we combine them together:

        -   ```html
            {%ex import time %}
            <a>{%ev time.time() %}</a>
            ```


## Tags:
### ex
Execute a python code.
- Should be like this: `{%ex import datetime %}`.
- This code is in python `import datetime`, `exec("import datetime", globals())`.
### ev
Eval a code.
- Should be like this: `{%ev 1330 + 7 %}`.
- This code is in python `1330 + 7`, `eval("1330 + 7")`.