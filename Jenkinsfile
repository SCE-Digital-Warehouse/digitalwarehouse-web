pipeline{
    agent any
    stages{
       stage('Build') {
             agent{
                docker{
                     script {
                        withCredentials([DockerCred]) {
                            docker.withRegistry(pavelni/test:ver1, 'docker') {
                                image 'test:ver1'
                            }
                        }
                     }
                }
             }

             steps {
                sh 'python -m py compile hello.py'
             }

       }

    }

}
