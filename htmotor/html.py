from dataclasses import dataclass


@dataclass
class HTML:
    VAR_REGEX = r"({%v *([a-zA-Z0-9]+) *%})"

    def __init__(self, prevent_xss: bool = False) -> None:
        self.xss = prevent_xss

    def prevent_xss(self, text: str) -> str:
        return "".join(
            f"&#{ord(i)};" for i in text
        )

    def render(self, html: str, **kwargs) -> str:
        return self.__render_variables(html, kwargs)

    def render_file(self, path_like: str, **kwargs) -> str:
        with open(path_like, "r", encoding="utf-8") as file:
            return self.render(file.read(), **kwargs)

    # Private Functions:
    def __render_variables(self, html: str, kwargs: dict) -> str:
        from re import findall

        for result in findall(self.VAR_REGEX, html):
            var = str(kwargs[result[1].strip()])
            if self.xss:
                var = self.prevent_xss(var)

            html = html.replace(result[0], var)

        return html
