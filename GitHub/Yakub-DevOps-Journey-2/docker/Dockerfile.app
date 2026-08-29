# Lab 7 - multi-stage build for the Java app tier (vProfile).
# Stage 1 builds the .war with Maven. Stage 2 contains ONLY the artifact and a runtime.
# Measure both with `docker images` - the difference is the point of multi-stage.

# ---------- Stage 1: build ----------
FROM maven:3.9-eclipse-temurin-11 AS build
WORKDIR /src
# Copy the pom first so Maven's dependency layer caches separately from your code.
COPY pom.xml .
RUN mvn -B dependency:go-offline
COPY src ./src
RUN mvn -B clean package -DskipTests=false

# ---------- Stage 2: runtime ----------
FROM tomcat:9-jre11-temurin
LABEL maintainer="yacoub"
RUN rm -rf /usr/local/tomcat/webapps/ROOT
COPY --from=build /src/target/*.war /usr/local/tomcat/webapps/ROOT.war
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=5s --start-period=60s --retries=3 \
  CMD curl -fsS http://localhost:8080/ || exit 1
CMD ["catalina.sh", "run"]
