pipeline {
    agent any

    stages {
        stage('Build and Deploy') {
            steps {
                script {
                    sh 'docker compose up -d --build'
                }
            }
        }
    }
}
