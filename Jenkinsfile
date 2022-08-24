pipeline {
   agent any
    stages {
        stage('Environment  Build') {
            steps {
			withCredentials([usernamePassword(credentialsId: 'github', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) 
			{
			bat 'echo $PASSWORD'
			echo USERNAME
			echo "username is $USERNAME"             
            }
			}
		}
	}
}
