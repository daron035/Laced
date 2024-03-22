pipeline {
    agent any

    stages {
        stage('Build and Deploy') {
            steps {
                script {
                    sh 'echo $USER'
                    sh 'chmod -R 777 backend/server/media'
                    sh 'docker compose up -d --build'
                }
            }
        }
    }
}
