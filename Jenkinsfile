pipeline {
   agent any
    stages {
        stage('Environment  Build') {
            steps {
			withCredentials([usernamePassword(credentialsId: '1', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) 
			{
			bat 'echo $PASSWORD'
			echo USERNAME
			echo "username is $USERNAME"    
			echo "username is $PASSWORD" 
            }
			bat """
                        export DB_USERNAME="${user}"
                        export DB_PASSWORD="${pw}"
                        python PythonCredCheck/test.py
                  	 """
                }
			}
		}
	}
