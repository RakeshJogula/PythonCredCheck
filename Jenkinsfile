pipeline {
   agent any
    stages {
        stage('Environment  Build') {
            steps {
               withCredentials([[
                  $class: 'UsernamePassword',
                   credentialsId: github,
                   usernameVariable: 'username',
                   passwordVariable: 'password',
                ]]) {
                bat """
                        export DB_USERNAME="${username}"
                        export DB_PASSWORD="${password}"
                        python PythonCredCheck/test.py
                   """
                }
            }
        }
    }
}

