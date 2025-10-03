# front2back
A Docker template with a Node.js image on the frontend and a Python image on the backend for use as a starter for other apps.

See [frontend](./frontend/README.md) or [backend](./backend/README.md) documentation for more details on how to choose your adventure on those specific stacks.

You can run this entire app as a VS Code DevContainer, choosing a specific service that VS Code will mount into. Or to run all services at once, run `docker-compose up --build --abort-on-container-exit --remove-orphans`. To shutdown the app after you're done, run `docker-compose down --remove-orphans`.

If using this repo as a GitHub template, remember to rename all references to "front2back" or "f2b" to whatever your own app's name is.
