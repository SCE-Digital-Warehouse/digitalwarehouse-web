pipeline{
    agent any
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
