pipeline {
   agent any
    stages {
        stage('Environment  Build') {
            steps {
               withCredentials([[
                  $class: 'UsernamePasswordMultiBinding',
                   credentialsId: 98,
                   usernameVariable: 'user',
                   passwordVariable: 'pw',
                ]]) {
                bat """
                        export DB_USERNAME="${user}"
                        export DB_PASSWORD="${pw}"
                        python PythonCredCheck/test.py
                   """
                }
            }
        }
    }
}

