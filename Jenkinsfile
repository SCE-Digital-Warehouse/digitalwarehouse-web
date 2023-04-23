pipeline{
    agent {
        dockerfile true
    }
    stages{
       stage('Build') {
             agent{
                docker{
                   image 'test'
                }
             }
             steps {
                sh 'python -m py compile hello.py'
             }

       }

    }

}
