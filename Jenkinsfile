pipeline{
    agent any
    stages{
             stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
            }
             stage('version'){
                steps{
                    sh 'python3 --version'
                }
             }
             stage('hello'){
                steps{
                    sh 'python3 hello.py'
                }
             }

        }
}
