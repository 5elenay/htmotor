# Prevent XSS
XSS is a dangerous method for attack a website. Htmotor comes with built-in XSS preventation support.

## Usage:
You only need to set `prevent_xss` to `True`.
```py
from htmotor import HTML

motor = HTML(prevent_xss=True)

# Now when we send a variable, eval a code or add a for-variable
# It will encode the value.
```

Also htmotor has a function if you want to encode a text manualy:
```py
from htmotor import HTML

motor = HTML()

motor.prevent_xss("<a>Hello!</a>") # -> &#60;&#97;&#62;&#72;&#101;&#108;&#108;&#111;&#33;&#60;&#47;&#97;&#62;
```