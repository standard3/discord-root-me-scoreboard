# First stage: install dependencies
FROM python:3-slim as requirements-stage

# Create a non-root user
RUN groupadd -r root_me_scoreboard_bot \
    && useradd --no-log-init -r -g root_me_scoreboard_bot root_me_scoreboard_bot

WORKDIR /code

# Copy everything
COPY . /code

# Install poetry and setup environment
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

RUN pip install poetry
RUN poetry install --without dev && rm -rf $POETRY_CACHE_DIR

# Execute the application as a non-root user
USER root_me_scoreboard_bot:root_me_scoreboard_bot

# Run the application
ENTRYPOINT ["poetry", "run", "python", "-m", "root_me_scoreboard_bot.main"]

