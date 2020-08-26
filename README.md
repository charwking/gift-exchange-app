# gift-exchange-app

## Development

1. Install [pipenv](https://pipenv.pypa.io/en/latest/)
1. Install dependencies: `pipenv install`
1. Run app: `pipenv run app`

## Decision Log

Short notes on decisions that were made so they can be discussed or revisted later. I expect some themes to emerge: simple, well-documented, low learning curve.

### Tech

* Selected [pipenv](https://pipenv.pypa.io/en/latest/) to manage dependencies and virtual environments. It popped up in [search results](https://packaging.python.org/tutorials/managing-dependencies/), was similar to tools I've used before (npm, bundler), and was easy to get started with.
* Selected [CherryPy](https://cherrypy.org/) because it's been around awhile, has lots of documentation, was easy to get running, and my webhost WebFaction ([affiliate link](https://www.webfaction.com/signup/?affiliate=cwk)) had an auto-installer for it.
