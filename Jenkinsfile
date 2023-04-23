pipeline{
    agent none
    stages{
       stage('Testing urls and views') {
             agent{
                docker{
                   image 'pavelni/test1:ver1'
                }
             }
             steps {
                 echo 'TEST IS OK!'
             }

       }

    }

}
