pipeline{
    agent any
    stages{
       stage('Build') {
             agent{
                docker{
                   image 'test:ver1'
                }
             }
             steps {
                sh 'python -m py compile hello.py'
             }

       }

    }

}
