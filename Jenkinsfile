pipeline {
	agent any
	stages {
        stage('Linting') {
            steps {
                sh 'make lint'
            }
        }
        stage('Build image') {
            steps {
                sh '''
                    docker build -t misenli/devopscapstone .
                '''
            }
        }
        stage('Push image') {
            steps {
                withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD']]){
                sh '''
                    docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD
                    docker push misenli/devopscapstone
                '''
                }
            }
        }
    }
}
