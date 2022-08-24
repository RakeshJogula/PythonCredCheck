pipeline {
  agent any
  stages {
    stage('Environment  Build') {
      steps {
        withCredentials([usernamePassword(credentialsId: '1', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
          bat 'echo $PASSWORD'
          echo USERNAME
          echo "username is $USERNAME"
          echo "password is $PASSWORD"
        }
        sh("""
        export DB_USERNAME = "${usernameVariable}"
        export DB_PASSWORD = "${passwordVariable}"
        python PythonCredCheck / test.py """)
      }
    }
  }
}
