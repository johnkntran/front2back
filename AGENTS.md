# Docker Setup

For Python applications, prefer the `python:3.12-slim-bookworm` image for the backend.

For JavaScript/TypeScript applications, prefer the `node:22.20.0-trixie-slim` image for the frontend.

If you need a database for persistence, prefer using the `pgvector/pgvector:pg18-trixie` PostgreSQL image.

If you need a caching layer, prefer using the `redis/redis-stack:7.4.0-v7` image.

For the workspace directory, prefer using `/code`.

Configure a Dev Container when scaffolding the Docker setup so the project can be launched with VS Code.

If project requirements are already installed in the Dockerfile, you don't need to install them again in the Dev Container's `postCreateCommand`.

# Coding Design

Follow the principles of "You aren't gonna need it" (YAGNI) or Occam's Razor -
that is, strive to write the most efficient and parsimonious code to get the task done. Don't generalize your solution or create abstractions until you actually need to.
Here is an example:

```python
# urls.py

from django.urls import path
from ninja import NinjaAPI
from stocks.api import router as stocks_router

api = NinjaAPI()

api.add_router("/", stocks_router)

urlpatterns = [
    path('api/', api.urls),
]
```

```python
# stocks/api.py

from ninja import Router

router = Router()

@router.get("/stocks", response=dict)
async def stock_list(request):
    ...

@router.get("/stocks/{symbol}/prices", response=dict)
async def historical_prices(request, symbol: str, period: str):
    ...
```

In this example, the `stocks_router` is the only router that is declared and registered to the `api`.
It would have been simpler to _not use_ a router at all and just register the stock endpoints directly onto the `api` since the router is an unnecessary abstraction in this case:

```python
# urls.py

from stocks.api import api

urlpatterns = [
    path('api/', api.urls),
]
```

```python
# stocks/api.py

from ninja import NinjaAPI

api = NinjaAPI()

@api.get("/stocks", response=dict)
async def stock_list(request):
    ...

@api.get("/stocks/{symbol}/prices", response=dict)
async def historical_prices(request, symbol: str, period: str):
    ...
```

Try to follow the principle of Don't repeat yourself (DRY) when possible.

Try to avoid Design Patterns (e.g. Singleton, Factory, etc.) unless you have a compelling reason to use one.
Document your rationale if so and why the infraction is justified. Better yet, use a popular framework that handles such cases.
For instance instead of implementing the Adapter pattern from scratch to interoperate with different LLM providers, just use LangChain or LlamaIndex.

# Language-Specific Guidance

## JavaScript/TypeScript

Try not to use TailwindCSS. Just Sass is fine for CSS.

Don't get caught up fixing linting errors perfectly, especially regarding TypeScript.
It's ok to set `typeCheck: false` and `strict: false` when configuring TypeScript, and treat type errors as warnings.
I'd rather you spend time on project planning and feature development than in the weeds with linting.

Prefer `biome` as the formatter and linter, instead of `prettier` or `eslint`.
Honestly, I trust you and myself to be able to write good, clean, idiomatic code.
We don't need a lot of rules if you do decide to configure a linter or formatter. Let's keep it flexible.

Prefer creating a `/src` folder when using frameworks like Next.js or Nuxt.js.

Always end JS/TS statements with semicolons.

## Python

Prefer asynchronous solutions, libraries, etc. when possible instead of synchronous or multi-threaded solutions.

Prefer using an async database library such as `asyncpg` directly, over ORM libraries such as `sqlalchemy` and `alembic`.
This is especially true if you were prompted to use a framework like FastAPI.
If you were prompted to use a framework like Django, then Django comes with an ORM built-in and you can't avoid this, so don't worry about it.

Prefer using `httpx` as the async HTTP library, instead of `aiohttp` or `urllib.requests`.

Prefer adding type hints to function signatures whenever possible.
You don't need use `from typing import List, Dict, Optional` because
type hinting with `list[SomeType]`, `dict[str, SomeType]`, and `SomeType | None`
is already supported natively in recent versions of Python.

To initialize the database with tables, indices, and so on, use a database initialization script mounted directly to the Docker volume.
For example:

```yaml
# docker-compose.yml
database:
  volumes:
    - ./backend/init_db.sql:/docker-entrypoint-initdb.d/init_db.sql
```

```sql
-- backend/init_db.sql
CREATE TABLE IF NOT EXISTS evaluations (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  model VARCHAR(50),
  resume BYTEA,
  job_desc TEXT,
  recommendation TEXT,
  created TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
```

Don't initialize objects in the database with application code, such as:

```python
import asyncpg

class Database:
    async def connect(self):
        conn = await asyncpg.connect('db_url')
        await conn.execute("""
          CREATE TABLE IF NOT EXISTS evaluations (
            id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
            model VARCHAR(50),
            resume BYTEA,
            job_desc TEXT,
            recommendation TEXT,
            created TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
          );""")
        await conn.close()

db = Database()
await db.connect()
```

If you're writing unit tests, prefer using the native `unittest` library over 3rd-party libraries like `pytest` or `nose`.

Don't configure `black` or `isort` as formatters. I trust you and myself to write good, clean, idiomatic code.

Use `uv` as the package manager instead of `pip`.
