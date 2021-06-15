# Motor
Quick documentation about functions, You also can get more information with python `help` function.

## prevent_xss
`<HTML>.prevent_xss(text: str) -> str`

Encode text for prevent XSS attacks.

Parameters:
- text (`str`): The text will be encoded.

Returns:
- `str`: Encoded string.

## render
`<HTML>.render(html: str, **kwargs) -> str`

Render htmotor syntax to HTML.

Parameters:
- htmotor (`str`): Htmotor syntax.
- **kwargs: Variables.

Returns:
- `str`: Rendered HTML string.

## render_file
`<HTML>.render_file(path_like: str, **kwargs) -> str`

Read htmotor file and render to HTML.

Parameters:
- path_like (`str`): File path.
- **kwargs: Variables.

Returns:
- `str`: Rendered HTML string.