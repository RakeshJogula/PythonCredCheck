pipeline {
  agent any
  stages {
    stage('Environment  Build') {
      steps {
        withCredentials([usernamePassword(credentialsId: '1', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
	echo "username is $USERNAME"
	echo "password is $PASSWORD"
        bat """python3 -u PythonCredCheck/test.py"""
        }
      }
    }
  }
}
