pipeline {
    stages {
        stage('Environment  Build') {
            steps {
                echo "Hello World!"
                sh "echo Hello from the shell"
                sh "hostname"
                sh "uptime"
                sh "python3 -m venv test_env"
                sh "source ./test_env/bin/activate"
                sh "pip3 install pandas psycopg2"
                sh """echo the script is working"""
                withCredentials([[
                    $class: 'UsernamePasswordMultiBinding',
                    credentialsId: github,
                    usernameVariable: 'user',
                    passwordVariable: 'pw',
                ]])
                sh """python3 PythonCredCheck/test.py"""
            }
        }
    }
}
