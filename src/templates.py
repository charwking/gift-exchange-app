import jinja2

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader("src/templates"),
    autoescape=jinja2.select_autoescape(["html"]),
)


def render(path, args):
    template = env.get_template(path)
    return template.render(args)
