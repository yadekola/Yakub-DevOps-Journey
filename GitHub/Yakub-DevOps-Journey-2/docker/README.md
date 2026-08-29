# Docker

## Commands worth understanding, not memorising

```bash
docker compose up -d              # build if needed, start everything detached
docker compose ps                 # STATUS column: look for "healthy", not just "Up"
docker compose logs -f vproapp    # follow one service's logs - your first debugging step
docker compose exec vproapp bash  # get a shell INSIDE a running container
docker images                     # compare multi-stage vs naive image size
docker compose down               # remove containers - named-volume data SURVIVES
docker compose down -v            # ...and delete the volumes too. Data is gone.
```

## The persistence experiment (do this, do not skip it)

1. `docker compose up -d`, insert a row into the database.
2. `docker compose down` then `up -d`. The row is still there. Why?
3. `docker compose down -v` then `up -d`. The row is gone. Why?

Write the answer in your own words in `week-07/notes.md`.

## Disk hygiene

```bash
docker system df                  # see what is using space
docker system prune -a --volumes  # removes ALL unused images AND volumes - read first
```
