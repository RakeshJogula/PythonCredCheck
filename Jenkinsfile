pipeline {
  agent any
   environment {
     env.PATH = env.PATH + ";c:\\Windows\\System32"
 }
  stages {
    stage('Environment  Build') {
      steps {
        withCredentials([usernamePassword(credentialsId: '1', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
          bat """python test.py"""
        }
      }
    }
  }
}
