pipeline {
  agent any
  stages {
    stage('Environment  Build') {
      steps {
        withCredentials([usernamePassword(credentialsId: '1', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
			sh "set DB_USERNAME="${USERNAME}" 
			sh "set DB_PASSWORD="${PASSWORD}" 
			sh """set DB_USERNAME="${USERNAME} set DB_PASSWORD="${PASSWORD}" python test.py"""
        }
      }
    }
  }
}
