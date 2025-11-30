FROM node:22.18.0-bookworm-slim

WORKDIR /code

RUN apt-get update \
    && apt-get install -y --no-install-recommends wget git curl vim \
    && apt-get install -y --reinstall procps

RUN --mount=type=secret,id=env,target=/code/.env \
    export $(cat /code/.env | xargs) \
    && git config --global user.name $GIT_USERNAME \
    && git config --global user.email $GIT_EMAIL

RUN npm install -g @openai/codex
RUN codex --version
RUN npm install -g @anthropic-ai/claude-code
RUN claude --version
RUN echo 'alias cc="claude --permission-mode acceptEdits --allowedTools Tool Bash Edit Glob Grep LS MultiEdit NotebookEdit NotebookRead Read Task TodoWrite WebFetch WebSearch Write -p"' >> ~/.bashrc
RUN mkdir ~/.codex && echo 'preferred_auth_method = "apikey"' >> ~/.codex/config.toml

COPY .env /code/.env

EXPOSE 3000

CMD ["sleep", "infinity"]
