pipeline {
    agent any

    stages {
        stage('Build and Deploy') {
            steps {
                script {
                    sh '/usr/local/bin/docker-compose up --build'
                }
            }
        }
    }
}
