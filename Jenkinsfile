pipeline {
  agent any
  stages {
    stage('Credential Setup') {
      steps {
        withCredentials([usernamePassword(credentialsId: '1', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
          bat """set DB_USERNAME="${USERNAME}" set DB_PASSWORD = "${PASSWORD}" python3 -u PythonCredCheck/test.py """
        }
      }
    }
	 stage('run') {
      steps {
          bat ""python3 -u PythonCredCheck/test.py ""
        }
      }
    }
  }

