pipeline {
  agent any
  stages {
    stage('Environment  Build') {
      steps {
        withCredentials([usernamePassword(credentialsId: '1', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
          sh """export DB_USERNAME="${USERNAME}"
          export DB_PASSWORD = "${PASSWORD}"
          python PythonCredCheck / test.py """
        }
      }
    }
  }
}
