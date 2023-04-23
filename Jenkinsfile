pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/BS-PMC-2023/BS-PMC-2023-Team8'
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                sh 'python manage.py test'
            }
        }

        stage('Build and deploy') {
            steps {
                sh 'python manage.py collectstatic'
                sh 'docker build -t your-docker-image-name .'
                sh 'docker run -d -p 8000:8000 your-docker-image-name'
            }
        }
    }
}