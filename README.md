# front2back
A Docker template with a Node.js image on the frontend and a Python image on the backend for use as a starter for other apps.

See [frontend](./frontend/README.md) or [backend](./backend/README.md) documentation for more details on how to choose your adventure on those specific stacks.

To run all services at once, use `docker-compose up --build --abort-on-container-exit --remove-orphans`. To shutdown the app after you're done, use `docker-compose down --remove-orphans`.

If using this repo as a GitHub template, remember to rename all references to "front2back" or "f2b" to whatever your own app's name is.


## Visual Studio Code (Optional)

[![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/johnkntran/front2back)

Instead of running `docker-compose up` in a separate process, you can run this project as a [VS Code Dev Container](https://code.visualstudio.com/docs/devcontainers/create-dev-container#_add-configuration-files-to-a-repository).

Install the [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension from the **Extensions** sidebar in VS Code.

Then open the Command Palette by typing `Command + P` on Mac (`Control + P` on Windows) and typing `> Dev Containers: Reopen in Container`, then choosing the first option. You can select whether to open the backend or frontend application first.

To switch between backend and frontend applications, open the Command Palette again and type `> Dev Containers: Switch Container` to switch to the other container.