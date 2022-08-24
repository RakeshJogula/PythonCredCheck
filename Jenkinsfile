pipeline {
  agent any
  stages {
    stage('Download tokens') {
	  steps
      {
        withCredentials([string(credentialsId: '1', variable: 'token')])
        {
            sh "set token=${token}"
			
            sh """set token="${token}" python3 test.py"""
        }
	  }
    }
  }
}
