pipeline {
  agent any
  stages {
    stage('Download tokens') {
	  steps
      {
        withCredentials([string(credentialsId: '11', variable: 'token')])
        {
            sh "export token=${token}"
            sh """export token="${token}" python3 script.py"""
        }
	  }
    }
  }
}
