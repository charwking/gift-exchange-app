# gift-exchange-app

## Development

1. Install [pipenv](https://pipenv.pypa.io/en/latest/)
1. Install dependencies: `pipenv install --dev`
1. Install the pre-commit hooks: `pipenv run pre-commit install`
1. Install [MySQL 8+](https://dev.mysql.com/doc/refman/8.0/en/installing.html)
1. Login to MySQL and run the one-time setup for local dev: `source db_setup_local.sql`
1. Login to MySQL and run the one-time setup for testing: `source db_setup_test.sql`
1. Run tests: `bin/test.sh`
1. Run app: `bin/local.sh`

## Decision Log

Short notes on decisions that were made so they can be discussed or revisted later. I expect some themes to emerge: simple, well-documented, low learning curve.

### Tech

* Selected [pipenv](https://pipenv.pypa.io/en/latest/) to manage dependencies and virtual environments. It popped up in [search results](https://packaging.python.org/tutorials/managing-dependencies/), was similar to tools I've used before (npm, bundler), and was easy to get started with.
* Selected [CherryPy](https://cherrypy.org/) because it's been around awhile, has lots of documentation, was easy to get running, and my webhost WebFaction ([affiliate link](https://www.webfaction.com/signup/?affiliate=cwk)) had an auto-installer for it.
* Selected [pytest](https://docs.pytest.org/en/latest/) as test framework because CherryPy already has a built-in test helper that uses it.
* Selected [black](https://github.com/psf/black) as a code auto-formatter because it's easy and avoids excessive time spent worrying about formatting and formatting rules.
* Selected [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/) as a template engine since it seems to be the most popular.
* Selected [MySQL](https://dev.mysql.com/) because it's [still the most popular DB](https://www.eversql.com/most-popular-databases-in-2020/) and my webhost supports it.
* Selected [SQLAlchemy](https://www.sqlalchemy.org/) because it's popular and [cwkingjr](https://github.com/cwkingjr) did some initial investigation ("loosened it")

### Infrastructure

* There's probably a "more correct" mechanism for managing environment variables, but stuffing them in shell scripts makes them explicit and easy to manage.

### Testing

* I decided to skip testing that the html rendered by a template exactly matched what I expected. This seemed excessive for now. I might revisit it later. If I do, I may aim for image-comparison tests.

### References

https://github.com/psf/black/tree/stable
https://pre-commit.com/
