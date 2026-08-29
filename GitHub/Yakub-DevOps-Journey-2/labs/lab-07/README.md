# Lab 7: Full containerization of the multi-tier application

**Week 7 — Saturday 17 October 2026**

## Objective

Containerize every tier: a multi-stage Dockerfile for the Java app, a custom DB image with the schema pre-loaded, an Nginx web image, plus Memcached and RabbitMQ. Bring the whole thing up with one docker compose command and publish the images.

## Why this lab exists

'It works on my machine' finally dies here. Containers make the environment part of the artifact.

## Architecture

```
docker compose up -d
  nginx  ->  app (multi-stage build)  ->  mysql (custom image, schema baked in)
                        |-> memcached
                        |-> rabbitmq
Named volumes for DB persistence, custom bridge network for name resolution
```

Draw your own version of this diagram before you start building. Save it to
`../../architecture/lab-07.png`. If you cannot draw it, you do not understand it yet.

## Prerequisites

- Docker installed
- Docker Hub account
- Lectures 302-323 completed

## Acceptance criteria

- [ ] Multi-stage build with a measurably smaller final image
- [ ] docker-compose.yml with named volumes, a custom network and healthchecks
- [ ] Images pushed to Docker Hub under your own account
- [ ] A .dockerignore that actually excludes build junk

## Steps

1. **Write the app Dockerfile as a multi-stage build.** Stage one: Maven builds the war.
   Stage two: a slim Tomcat base, `COPY --from=build` only the artifact.
   *Why:* the final image should not contain Maven, the JDK, or your source code.
   *Expected:* the multi-stage image is dramatically smaller — measure it and record both numbers.

2. **Write the DB Dockerfile** with the schema pre-loaded via `/docker-entrypoint-initdb.d/`.

3. **Write the web Dockerfile** with your Nginx reverse-proxy config baked in.

4. **Write `docker-compose.yml`:** all five services, a custom network, named volumes for
   MySQL data, and healthchecks with `depends_on: condition: service_healthy`.

5. **`docker compose up -d`** and reach the app in a browser.

6. **Prove persistence:** insert data, `docker compose down`, `up` again, data is still there.
   Then `down -v` and watch it disappear. Understand why.

7. **Push all three images to Docker Hub** under your own namespace, tagged with a version,
   not just `latest`.

## Verification

- [ ] One command brings the whole stack up
- [ ] `docker images` shows the multi-stage image is smaller than a naive build
- [ ] Data survives `down` and `up`, and is destroyed by `down -v`
- [ ] Containers resolve each other by service name
- [ ] `docker compose ps` shows all services healthy, not just running

## Troubleshooting challenges

Work these out yourself before looking anything up. Hints only — no answers.

1. **The app container starts then exits immediately with code 0.**
   *Hint: Read the actual error, not the summary. Then ask: what changed?*
2. **The app cannot resolve the hostname 'mysql' even though both containers are running.**
   *Hint: Check the layer below the one you think is broken.*
3. **Data disappears every time you run `docker compose down`.**
   *Hint: Compare a working case with the broken one and list every difference.*

## Cleanup

```bash
docker compose down -v
docker system prune -a --volumes   # careful: removes ALL unused images
```
No cloud cost here, but Docker will quietly eat 20GB of your disk if you never prune.

## Interview questions

Answer these in writing in `answers.md` before you consider the lab finished.

1. What is the difference between an image and a container?
2. Why use a multi-stage build? What did it save you?
3. ENTRYPOINT vs CMD — when does the distinction matter?
4. Where does container data live, and what happens to it on `docker rm`?
5. How do containers find each other by name?
6. Your container starts and immediately exits with code 0. What does that tell you?
