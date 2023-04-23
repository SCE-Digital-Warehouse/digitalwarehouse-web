pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/BS-PMC-2023/BS-PMC-2023-Team8'
            }
        }
        stage('Build') {
            steps {
                sh 'python manage.py runserver'
            }
        }



}