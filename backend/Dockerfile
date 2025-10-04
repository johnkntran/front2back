FROM python:3.13.7-slim-trixie

WORKDIR /code

RUN apt-get update \
    && apt-get install -y --no-install-recommends git curl vim \
    && apt-get install -y --reinstall procps

RUN --mount=type=secret,id=env,target=/code/.env \
    export $(cat /code/.env | xargs) \
    && git config --global user.name $GIT_USERNAME \
    && git config --global user.email $GIT_EMAIL

ENV NODE_VERSION=22.18.0
ENV NVM_DIR=/root/.nvm
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
RUN . "$NVM_DIR/nvm.sh" && nvm install ${NODE_VERSION}
RUN . "$NVM_DIR/nvm.sh" && nvm use v${NODE_VERSION}
RUN . "$NVM_DIR/nvm.sh" && nvm alias default v${NODE_VERSION}
ENV PATH="${PATH}:$NVM_DIR/versions/node/v${NODE_VERSION}/bin/"
RUN npm install -g @openai/codex
RUN codex --version
RUN npm install -g @anthropic-ai/claude-code
RUN claude --version
RUN echo 'alias cc="claude --permission-mode acceptEdits --allowedTools Tool Bash Edit Glob Grep LS MultiEdit NotebookEdit NotebookRead Read Task TodoWrite WebFetch WebSearch Write -p"' >> ~/.bashrc
RUN mkdir ~/.codex && echo 'preferred_auth_method = "apikey"' >> ~/.codex/config.toml

COPY ./backend/requirements.txt /code
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY .env /code

EXPOSE 8000

CMD ["sleep", "infinity"]
