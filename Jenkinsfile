pipeline{
    agent none
    stages{
       stage('Build') {
             agent{
                docker{
                   image 'test:ver1'
                }
             }
             steps {
                sh 'python hello.py'
             }

       }

    }

}
