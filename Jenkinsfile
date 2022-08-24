pipeline {
   agent any
    stages {
        stage('Environment  Build') {
            steps {
                echo "Hello World!"
		withCredentials([usernamePassword(credentialsId: '1', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')])
		{
		bat 'echo $PASSWORD'
		echo USERNAME
		echo "username is $USERNAME"
		} 	
		{
                bat """export DB_USERNAME="${user}"
                        export DB_PASSWORD="${pw}"
                        python3 PythonCredCheck/test.py
                   """
                }
            }
        }
    }
}

