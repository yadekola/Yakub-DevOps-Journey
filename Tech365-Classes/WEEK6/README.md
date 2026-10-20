# Java Inventory Application — DevOps Project

![Java](https://img.shields.io/badge/Java-17-orange)
![Spring Boot](https://img.shields.io/badge/Spring%20Boot-3.5.x-brightgreen)
![React](https://img.shields.io/badge/React-19-blue)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED)
![GitHub Actions](https://img.shields.io/badge/CI-GitHub%20Actions-2088FF)

## 1. Project Overview

The Java Inventory Application is a full-stack application for managing inventory products. It uses a Java Spring Boot backend, a React frontend, and a PostgreSQL database.

This repository also demonstrates practical DevOps workflows, including version control with Git and GitHub, containerization with Docker Compose, application testing, and Continuous Integration (CI) with GitHub Actions.

### Project objectives

* Run the application and its supporting services using Docker Compose.
* Configure communication between the frontend, backend, and database.
* Manage source code using Git and GitHub.
* Automate backend testing and frontend production builds.
* Document setup, verification, troubleshooting, and maintenance procedures.
* Build a foundation for future container image publishing and deployment automation.

## 2. Technologies Used

| Technology     | Purpose                                        |
| -------------- | ---------------------------------------------- |
| Java 17        | Backend programming language                   |
| Spring Boot    | Backend application framework                  |
| Maven          | Backend dependency management and testing      |
| React 19       | Frontend user interface                        |
| Vite           | Frontend development and production build tool |
| PostgreSQL 17  | Relational database                            |
| Docker         | Application containerization                   |
| Docker Compose | Running and connecting application services    |
| Git            | Version control                                |
| GitHub         | Source code hosting and collaboration          |
| GitHub Actions | Automated testing and build verification       |

## 3. Application Architecture

The application consists of three main services:

1. **Frontend:** React application served by Vite.
2. **Backend:** Spring Boot REST API.
3. **Database:** PostgreSQL database for persistent application data.

### How the services communicate

* The user opens the frontend in a web browser.
* The frontend sends API requests through the `/api` path.
* Vite forwards these requests to the backend API service.
* The backend communicates with PostgreSQL.
* The backend returns the response to the frontend.

Docker Compose manages the services and their internal network.

### Service and port reference

| Service     | Host access                                               | Container access |
| ----------- | --------------------------------------------------------- | ---------------- |
| Frontend    | `localhost:5173`                                          | Port `5173`      |
| Backend API | `localhost:8083`                                          | Port `8080`      |
| PostgreSQL  | Not published to the host in the documented configuration | Port `5432`      |

The frontend uses the `API_PROXY_TARGET` environment variable to identify the backend service. In Docker Compose, its value is `http://api:8080`.

## 4. Repository Structure

The important project files and directories include:

```text
java-inventory/
├── .github/
│   └── workflows/
│       └── ci.yml
├── backend/
│   ├── pom.xml
│   └── src/
│       ├── main/
│       └── test/
├── frontend/
│   ├── package.json
│   ├── package-lock.json
│   └── src/
├── .env.example
├── .gitignore
└── docker-compose.yml
```

Note: Additional files and directories may exist in the repository. Consult the actual repository tree for the complete structure.

### Important files

* `docker-compose.yml`: Defines the services, networking, ports, and configuration used to run the application.
* `backend/pom.xml`: Defines the backend dependencies and Maven build configuration.
* `frontend/package.json`: Defines frontend dependencies and npm scripts.
* `frontend/package-lock.json`: Locks frontend dependency versions for reproducible installation.
* `.env.example`: Provides a template for required environment variables.
* `.gitignore`: Excludes local secrets and generated files from version control.
* `.github/workflows/ci.yml`: Defines the GitHub Actions CI pipeline.

## 5. Prerequisites

Before starting, install the following:

* Git
* Docker Desktop with Docker Compose support
* A GitHub account
* A terminal such as Git Bash on Windows

Docker Desktop should be running before you execute Docker commands.

For running the backend directly on your computer, Java 17 and Maven are required. For running the frontend directly, Node.js 24 and npm are required.

The Docker-based setup is the recommended starting point because it runs the application's services in containers.

## 6. Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/yadekola/java-inventory.git
cd java-inventory
```

Confirm that you are in the project directory:

```bash
git status
```

Expected result: Git should report the current branch and working-tree status without errors.

## 7. Configure Environment Variables

The repository includes an `.env.example` file as a configuration template.

Create a local environment file:

```bash
cp .env.example .env
```

Open `.env` in a text editor and review the variables. Set the required values according to the template and the Docker Compose configuration.

Important security practices:

* Never commit `.env` when it contains secrets.
* Never publish database passwords, access tokens, or private credentials.
* Keep `.env.example` free of real secrets.
* Use strong, unique passwords for non-local environments.

If the application requires different environment variables, consult `.env.example`, `docker-compose.yml`, and the application configuration before proceeding.

## 8. Start the Application with Docker Compose

Build the images and start the services:

```bash
docker compose up --build -d
```

Check the service status:

```bash
docker compose ps
```

The database and API should become healthy when their health checks pass. The frontend should also be running.

Allow some time for the database initialization, migrations, and backend startup to complete.

### View application logs

View all service logs:

```bash
docker compose logs
```

Follow the logs in real time:

```bash
docker compose logs -f
```

View logs for an individual service:

```bash
docker compose logs -f api
docker compose logs -f frontend
docker compose logs -f db
```

Press `Ctrl+C` to stop following logs. This does not stop the containers.

## 9. Access and Verify the Application

### Frontend

Open this address in your browser:

http://localhost:5173

### Backend API

Test the product endpoint from your terminal:

```bash
curl http://localhost:5173/api/products
```

The request passes through the frontend's Vite proxy to the backend API.

A successful response should contain a JSON object with pagination information and a product data array. The exact records depend on the current database contents.

You can also check the frontend HTTP response:

```bash
curl -I http://localhost:5173
```

An HTTP `200` response indicates that the frontend server is responding successfully.

### Verify the database

Connect to the PostgreSQL service:

```bash
docker compose exec db psql -U inventory -d inventory
```

Inside the PostgreSQL prompt, list the tables:

```sql
\dt
```

Inspect product records:

```sql
SELECT * FROM products;
```

Exit PostgreSQL:

```sql
\q
```

If your database credentials or database name differ, use the values configured in your environment and Compose files.

## 10. Testing the Backend and Building the Frontend

### Backend tests

The backend uses Maven. Run the tests from the backend directory:

```bash
cd backend
mvn test
```

Return to the project root afterwards:

```bash
cd ..
```

The test configuration uses an in-memory H2 database in PostgreSQL compatibility mode. This allows the configured backend tests to run without relying on a local PostgreSQL instance.

### Frontend production build

Run the following commands:

```bash
cd frontend
npm ci
npm run build
```

The `npm ci` command installs dependencies according to the lockfile. The production build should complete without errors.

Return to the project root:

```bash
cd ..
```

## 11. Git and GitHub Workflow

Git is used to track changes, while GitHub hosts the repository and supports collaboration.

Check the current status:

```bash
git status
```

Review changed files:

```bash
git diff
```

Stage the intended changes:

```bash
git add README.md
```

Replace `README.md` with the appropriate file paths when staging other changes.

Review what is staged:

```bash
git diff --cached
```

Commit the changes:

```bash
git commit -m "Update project documentation"
```

Push to GitHub:

```bash
git push
```

Before committing, review staged files and confirm that no credentials, local `.env` files, or generated build artifacts have been included.

## 12. Continuous Integration with GitHub Actions

### Objective

The project uses GitHub Actions to automate backend testing and frontend build verification.

The workflow is located at:

```text
.github/workflows/ci.yml
```

### Workflow triggers

The workflow runs when:

* A commit is pushed to the `master` branch.
* A pull request targets the `master` branch.

### Job 1: Test Java Backend

The workflow:

1. Checks out the repository.
2. Sets up Java 17.
3. Configures Maven dependency caching.
4. Runs:

```bash
mvn -B test
```

The test job uses the H2 test configuration.

### Job 2: Build React Frontend

The workflow:

1. Checks out the repository.
2. Sets up Node.js 24.
3. Configures npm dependency caching.
4. Installs dependencies:

```bash
npm ci
```

5. Builds the frontend:

```bash
npm run build
```

### How to verify the CI pipeline

1. Push a commit to GitHub.
2. Open the repository's **Actions** tab.
3. Select the latest `Java Inventory CI` run.
4. Open the run details.
5. Confirm that both the backend test and frontend build jobs pass.

A successful workflow indicates that the configured automated checks passed. It does not, by itself, prove that the application has been deployed to production.

### Initial CI result

The initial GitHub Actions workflow completed successfully in 32 seconds. Both jobs passed.

Workflow:

https://github.com/yadekola/java-inventory/actions/workflows/ci.yml

## 13. Troubleshooting

### Docker services are not starting

Check their status:

```bash
docker compose ps
```

Inspect logs:

```bash
docker compose logs
```

Confirm that Docker Desktop is running and that the required ports are not already occupied by other applications.

### Frontend loads but API requests fail

Check the backend logs:

```bash
docker compose logs -f api
```

Verify that the API service is healthy and that the frontend's `API_PROXY_TARGET` points to `http://api:8080` inside Docker Compose.

### Database connection fails

Check the database logs:

```bash
docker compose logs -f db
```

Verify the configured database name, username, password, service name, and health status.

### GitHub Actions fails

Open the failed workflow run in the Actions tab. Select the failed job and inspect the step containing the error.

For backend failures, check the Maven test output. For frontend failures, inspect the npm installation and build logs.

Fix the underlying problem, run the relevant check locally when possible, and push the correction.

### Port already in use

If Docker reports that a port is already allocated, identify the application using that port or adjust the host-side port mapping in `docker-compose.yml`. Update the documented access URL if the host port changes.

## 14. Security and Operational Best Practices

* Keep credentials out of Git.
* Do not expose the PostgreSQL port publicly unless there is a specific, secured requirement.
* Use environment variables or a secret-management solution for sensitive configuration.
* Review Docker image versions and dependencies regularly.
* Use Git branches and pull requests when collaborating.
* Investigate failing tests rather than ignoring them.
* Keep the README aligned with the actual project configuration.
* Back up important persistent data before performing destructive maintenance.
* Avoid deleting Docker volumes unless you understand the effect on stored database data.

## 15. Stopping and Cleaning Up

Stop the running services:

```bash
docker compose down
```

This removes the Compose containers and network but normally preserves named volumes.

To remove volumes as well:

```bash
docker compose down -v
```

**Warning:** Removing volumes can permanently delete the database data stored in them. Do not run the second command unless you intentionally want to remove that data and have any required backups.

## 16. Current DevOps Scope and Future Improvements

### Implemented and verified

* Git repository hosted on GitHub.
* Docker Compose application environment.
* Frontend-to-backend API proxy configuration.
* Backend test configuration using H2.
* GitHub Actions CI workflow.
* Automated backend tests and frontend production build.
* Successful initial CI execution.

### Potential next improvements

* Build Docker images automatically in GitHub Actions.
* Publish versioned images to GitHub Container Registry.
* Add image vulnerability scanning and dependency checks.
* Add deployment automation to a suitable hosting environment.
* Introduce pull-request protection and required CI checks.
* Add monitoring, centralized logs, and operational health checks.
* Document backup and recovery procedures for persistent data.

These are future improvements, not claims that they have already been implemented.

## 17. Learning Outcomes

This project provides practical experience with:

* Version control and repository management.
* Containerizing a multi-service application.
* Configuring service networking and environment variables.
* Running automated backend tests and frontend builds.
* Creating and troubleshooting a GitHub Actions pipeline.
* Writing reproducible setup and operational documentation.

## 18. Author and Repository

**Repository:** https://github.com/yadekola/java-inventory

This project is part of a hands-on DevOps learning journey focused on applying software delivery, automation, and operational practices to a real application.
