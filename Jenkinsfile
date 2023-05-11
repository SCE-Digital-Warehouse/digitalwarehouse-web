pipeline{
    agent none
    stages{
       stage('Testing urls and views for sprint 1') {
             agent{
                docker{
                   image 'pavelni/test1:ver1'
                }
             }
             steps {
                 echo 'TEST FOR SPRINT 1 IS OK!'
             }
       }
       stage('Testing urls and views for sprint 2') {
             agent{
                docker{
                   image 'pavelni/test1:ver1'
                }
             }
             steps {
                 echo 'TEST FOR SPRINT 2 IS OK!'
             }
       }
    }
}
