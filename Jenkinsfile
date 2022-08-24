pipeline {
   agent any
    stages {
        stage('Environment  Build') {
            steps {
		withCredentials([usernamePassword(credentialsId: 'amazon', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
 	       bat 'echo $PASSWORD'
	       bat  'echo USERNAME'
  	       bat "username is $USERNAME"
		}	
		{
                bat """export DB_USERNAME="${USERNAME}"
                        export DB_PASSWORD="${PASSWORD}"
                        python3 PythonCredCheck/test.py
                   """
                }
            }
        }
    }
}

