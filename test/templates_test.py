import os
import tempfile
from src import templates


def test_render():
    with tempfile.NamedTemporaryFile(dir="src/templates", suffix=".html") as temp:
        with open(temp.name, "w") as file:
            file.write("I am a template with an escaped arg of {{ arg }}")

        template_name = os.path.basename(temp.name)
        result = templates.render(template_name, {"arg": "<b>BOLD</b>"})

        assert (
            result == "I am a template with an escaped arg of &lt;b&gt;BOLD&lt;/b&gt;"
        )
