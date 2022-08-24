pipeline {
  agent any
  stages {
    stage('Environment  Build') {
      steps {
        withCredentials([usernamePassword(credentialsId: '1', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
			bat "export  DB_USERNAME=${USERNAME}"
			bat "export  DB_PASSWORD=${PASSWORD}" 
			bat ""C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python39\\python.exe test.py""
			echo "${USERNAME}"
        }
      }
    }
  }
}
