pipeline {
   agent any
    stages {
        stage('Environment  Build') {
            steps {
                echo "Hello World!"
                sh "echo Hello from the shell"
                sh "hostname"
                sh "uptime"
                sh "python3 -m venv test_env"
                sh "source ./test_env/bin/activate"
                sh """echo the script is working"""
               withCredentials([[
                  $class: 'UsernamePasswordMultiBinding',
                   credentialsId: 98,
                   usernameVariable: 'user',
                   passwordVariable: 'pw',
                ]]) {
                sh """
                        export DB_USERNAME="${user}"
                        export DB_PASSWORD="${pw}"
                        python3 PythonCredCheck/test.py
                   """
                }
            }
        }
    }
}
