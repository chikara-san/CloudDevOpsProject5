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
                    if [ $exist_service_info -eq 1 ]; then
                      kubectl delete secret service-info
                    fi
                    echo -n ${SERVICE_ID} > ./serviceid
                    echo -n ${API_KEY} > ./apikey
                    kubectl create secret generic service-info --from-file=./serviceid --from-file=./apikey
                    rm  ./serviceid ./apikey
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

        stage('Create service') {
            steps {
                sh '''
                    kubectl apply -f infra/app/service.yml
                '''
            }
        }
    }
}
