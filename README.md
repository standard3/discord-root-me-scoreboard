# Root-me Discord scoreboard

A discord bot that allows to make a private root-me scoreboard

## Features

To-do

## Deployment

Before deploying somewhere, please create a `.env` file with the filled variables :
- `DISCORD_TOKEN`: your discord bot token, get it [here](https://discord.com/developers/applications)
- `GUILD_ID`: your discord server unique identifier, you can get it through developer settings
- `ROOT_ME_API_KEY`: your personnal account API key, you can get it [here](https://www.root-me.org/?page=preferences)

Deployment is made with Docker. Build the image and run it :

```shell
$ docker build -t root_me_scoreboard_bot -f docker/Dockerfile .
$ docker run -d --name root_me_scoreboard_bot root_me_scoreboard_bot
```

Or with `docker compose` :

```shell
$ docker compose -f docker/docker-compose.yml -p root_me_scoreboard_bot up -d
```

## Usage

To-do
