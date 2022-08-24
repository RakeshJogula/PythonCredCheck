pipeline {
   agent any
    stages {
        stage('Environment  Build') {
            steps {
                echo "Hello World!"
                bat "echo Hello from the batell"
                bat "hostname"
                bat "uptime"
                bat "python3 -m venv test_env"
                bat "source ./test_env/bin/activate"
                bat """echo the script is working"""
               withCredentials([[
                  $class: 'UsernamePasswordMultiBinding',
                   credentialsId: 98,
                   usernameVariable: 'user',
                   passwordVariable: 'pw',
                ]]) {
                bat """
                        export DB_USERNAME="${user}"
                        export DB_PASSWORD="${pw}"
                        python3 PythonCredCheck/test.py
                   """
                }
            }
        }
    }
}

