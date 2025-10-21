# front2back
A Docker template with a Node.js image on the frontend and a Python image on the backend for use as a starter for other apps.

# Getting Started

Create an `.env` file and copy the contents of `.env.example` into it. Fill out the placeholder values with your own data.

- To run all services, use `docker-compose up --build --abort-on-container-exit --remove-orphans`.
- To shutdown the app after you're done (and remove all volumes created), use `docker-compose down --remove-orphans --volumes`.

If using this repo as a GitHub template, remember to rename all references to "front2back" or "f2b" to whatever your own app's name is.

See [frontend](./frontend/README.md) or [backend](./backend/README.md) documentation for more details on how to choose your adventure on those specific stacks.

## Visual Studio Code (Optional)

[![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/johnkntran/front2back)

Instead of running `docker-compose up` in a separate process, you can run this project as a [VS Code Dev Container](https://code.visualstudio.com/docs/devcontainers/create-dev-container#_add-configuration-files-to-a-repository).

Install the [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension from the **Extensions** sidebar in VS Code.

Then open the Command Palette by typing `Command + P` on Mac (`Control + P` on Windows) and typing `> Dev Containers: Reopen in Container`, then choosing the first option. You can select whether to open the backend or frontend application first.

To switch between backend and frontend applications, open the Command Palette again and type `> Dev Containers: Switch Container` to switch to the other container.

## Using The LLM CLI Tools

### [Aider](https://aider.chat/docs/usage.html)

- Run `aider --model=claude-sonnet-4-5`, `aider --model=gpt-5`, `aider --model=gemini-2.5-pro`, `aider --model=xai/grok-4-0709` or `aider --model=perplexity/sonar-reasoning` to configure Aider.
- Run `aider <file1> <file2> <etc...>` to start using Aider.
- Use `CTRL + C` twice to quit.

### [Claude Code](https://www.anthropic.com/engineering/claude-code-best-practices)

- Run `cc "<question>"` to use Claude Code.
- Quits automatically after each statement.

### [Codex](https://developers.openai.com/codex/cli)

- Run `codex "<question>"` to use.
- Use `CTRL + C` to quit.

## Agentic IDEs

I personally find myself using [Windsurf](https://docs.windsurf.com/windsurf/getting-started) or [Void](https://voideditor.com/) as my primary IDE, with [VS Code](https://code.visualstudio.com/docs) as a fallback to run [Dev Containers](https://containers.dev/implementors/json_reference/). I've heard good things about [Zed](https://zed.dev/docs/) (by the same guy who created [Atom](https://github.blog/news-insights/product-news/sunsetting-atom/)) but haven't used it. There's also [Trae](https://traeide.com/docs/what-is-trae-ide), created by ByteDance (who makes TikTok) that I don't know much about. Lastly, there's [Kiro](kiro.dev/docs/) which might be promising.

Some other mentions are [Warp](https://docs.warp.dev/code/code-editor), [Amp](https://sourcegraph.com/amp), [OpenCode](https://opencode.ai/docs), [Factory](https://factory.ai/pricing), [Tabnine](https://docs.tabnine.com/main), [AugmentCode](https://docs.augmentcode.com/introduction), [Continue](https://docs.continue.dev/), [Forge Code](https://forgecode.dev/) , [Gemini CLI](https://geminicli.com/docs), [Jules](https://jules.google/) and many others.
