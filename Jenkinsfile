pipeline {
    agent any

    stages {
        stage('Build and Deploy') {
            steps {
                script {
                    sh 'echo $USER'
                    sh 'docker compose up -d --build'
                }
            }
        }
    }
}
