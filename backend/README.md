Run `uv sync`, then `uv run ruff check` and `uvx ty check main.py` to test if everything works.

From here, you can choose your adventure of what backend Python framework you want to use. Some suggestions are:
- [FastAPI](https://fastapi.tiangolo.com/#without-standard-dependencies)
- [Django](https://docs.djangoproject.com/en/5.2/intro/install/) with [Django Ninja](https://django-ninja.dev/) for REST API
- [Strawberry](https://strawberry.rocks/) for GraphQL

For task queues and background worker libraries, my recommendations from most to least recommended are:
- [RQ](https://python-rq.org/)
- [Dramatiq](https://dramatiq.io/)
- [Huey](https://huey.readthedocs.io/en/latest/)
- [Kew](https://github.com/justrach/kew)
