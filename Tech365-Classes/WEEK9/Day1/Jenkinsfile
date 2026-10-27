pipeline{
    agent any 
    environment{
        DOCKERHUB_USERNAME = "tech365"
        IMAGE_NAME = "${DOCKERHUB_USERNAME}/nodejs-cicd-app"
        APP_SERVER = "ec2-54-82-61-48.compute-1.amazonaws.com"
        APP_PORT = "3000"
        APP_USER = "ec2-user"
        CONTAINER_NAME = "nodejs-apps"
    }
    stages{
        stage("Checkout source code"){
            steps{
                checkout scm
            }
        }

        stage("Install dependencies"){
            steps{
                sh "npm ci"
            }
        }

         stage("Build docker image"){
            steps{
                sh """
                docker build \
                -t ${IMAGE_NAME}:${BUILD_NUMBER} \
                -t ${IMAGE_NAME}:latest .
                """
            }
        }
        stage("Push to docker hub"){
            steps{
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-credentials',
                        usernameVariable: 'DOCKERHUB_USERNAME',
                        passwordVariable: 'DOCKER_TOKEN'
                    )
                ]){
                    sh """
                    echo "$DOCKER_TOKEN" | docker login -u "$DOCKERHUB_USERNAME" --password-stdin
                    docker push ${IMAGE_NAME}:${BUILD_NUMBER}
                    docker push ${IMAGE_NAME}:latest
                    docker logout
                    """
                }
            }
        }
    }
}
