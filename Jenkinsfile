pipeline {
  agent any
  stages {
    stage('Environment  Build') {
      steps {
        withCredentials([usernamePassword(credentialsId: '1', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
			bat """set  DB_USERNAME="${USERNAME}"
			       set  DB_PASSWORD="${PASSWORD}" 
			       C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python39\\python.exe test.py"""
			echo %DB_PROJECT%
			echo %DB_REPO%
        }
      }
    }
  }
}
