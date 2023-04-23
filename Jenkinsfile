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
                sh 'python -m py_compile BS-PMC-2023-Team8/hello.py'
             }

       }

    }

}
