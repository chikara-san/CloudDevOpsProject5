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
                    docker build -t orikix/devopscapstone .
                '''
            }
        }
        stage('Push image') {
            steps {
                withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'docker', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD']]){
                sh '''
                    docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD
                    docker push orikix/devopscapstone
                '''
                }
            }
        }
        stage('Set secret from envvars') {
            steps {
                withCredentials([string(credentialsId: 'SERVICE_ID', variable: 'SERVICE_ID'), string(credentialsId: 'API_KEY', variable: 'API_KEY')]) {
                sh '''
                    exist_service_info=`kubectl get secret service-info | grep service-info | wc -l`
                    if [$exist_service_info -eq 0]; then
                      kubectl delete secret service-info
                    fi
                    echo -n ${SERVICE_ID} > ./SERVICE_ID
                    echo -n ${API_KEY} > ./API_KEY
                    kubectl create secret generic service-info --from-file=./SERVICE_ID --from-file=./API_KEY
                    rm  ./SERVICE_ID ./API_KEY
                '''
                }
            }
        }
        stage('Create deployment') {
            steps {
                sh '''
                    kubectl apply -f infra/app/deployment.yml
                '''
            }
        }

    }
}
