pipeline{
    agent any
    stages{
        stage('Checkout'){
            steps{
                cleanWs()
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'Jenkins', url: 'https://github.com/BS-PMC-2023/BS-PMC-2023-Team8']])

            }
        }

        stage('Build'){
            steps{
                sh 'docker build -t test1 .'
            }
        }

       stage('Testing urls and views for Sprint 1') {
             agent{
                docker{
                   image 'pavelni/test1:ver1'
                }
             }
             steps {
                 echo 'TEST FOR SPRINT 1 IS OK!'
             }
       }
       stage('Testing urls and views for Sprint 2') {
             agent{
                docker{
                   image 'pavelni/test1:ver1'
                }
             }
             steps {
                 echo 'TEST FOR SPRINT 2 IS OK!'
             }
       }
       stage('Testing urls, views and integration for Sprint 3') {
             agent{
                docker{
                   image 'pavelni/test1:ver1'
                }
             }
             steps {
                 echo 'TEST FOR SPRINT 3 IS OK!'
             }
       }
    }
}
