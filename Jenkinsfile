pipeline {
  agent any
  stages {
    stage('Environment  Build') {
      steps {
        withCredentials([usernamePassword(credentialsId: '1', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
			bat "set DB_USERNAME=${USERNAME}"
			bat "set DB_PASSWORD=${PASSWORD}" 
			bat "C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python39\\python.exe python test.py"
			echo "${USERNAME}"
        }
      }
    }
  }
}
