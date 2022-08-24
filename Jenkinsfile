pipeline {
  agent any
  stages {
    stage('Environment  Build') {
      steps {
        bat "pip install os"
        withCredentials([usernamePassword(credentialsId: '1', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
        bat """set DB_USERNAME="${USERNAME}" set DB_PASSWORD = "${PASSWORD}" python3 -u test.py """
        }
      }
    }
  }
}
