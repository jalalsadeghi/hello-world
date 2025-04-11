pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS_ID = 'docker-hub-credentials'
        DOCKER_IMAGE = 'jalalsadeghi/hello-world'
        KUBE_CREDENTIALS_ID = 'kubeconfig'
    }
    stages {
        stage('Checkout') {
        steps {
            checkout scm
            echo "Checkout successfully validated."
        }
    }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:${env.BUILD_NUMBER}")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', DOCKER_CREDENTIALS_ID) {
                        docker.image("${DOCKER_IMAGE}:${env.BUILD_NUMBER}").push()
                        docker.image("${DOCKER_IMAGE}:${env.BUILD_NUMBER}").push('latest')
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                withKubeConfig([credentialsId: KUBE_CREDENTIALS_ID]) {
                    sh """
                    kubectl set image deployment/hallo-welt hallo-welt=${DOCKER_IMAGE}:${env.BUILD_NUMBER} -n websites
                    """
                }
            }
        }
        // stage('Deploy to Kubernetes') {
        //     steps {
        //         withKubeConfig([credentialsId: KUBE_CREDENTIALS_ID]) {
        //             sh """
        //             kubectl rollout restart deployment/hallo-welt -n websites
        //             """
        //         }
        //     }
        // }
    }
}