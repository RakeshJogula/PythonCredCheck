pipeline {
   agent any
    stages {
        stage('Environment  Build') {
            steps {
			withCredentials([usernamePassword(credentialsId: 'amazon', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) 
			{
			bat 'echo $PASSWORD'
			echo USERNAME
			echo "username is $USERNAME"             
            }
			}
		}
	}
}
