pipeline {
  agent any
  stages {
    stage('Environment  Build') {
      steps {
        withCredentials([gitUsernamePassword(credentialsId: '1', gitToolName: 'Default')])
				{
				bat 'echo $PASSWORD'
				echo USERNAME
				echo "username is $USERNAME"
				} 	
				{
                bat """
                        set DB_USERNAME="${USERNAME}"
                        set DB_PASSWORD="${PASSWORD}"
                        python3 test.py
                   """
                }
      }
    }
  }
}
