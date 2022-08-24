pipeline {
  agent any
  stages {
    stage('Environment  Build') {
      steps {
		withCredentials([string(credentialsId: '2', variable: 'TOKEN')])
	      		bat """set  DB_TOKEN="${TOKEN}"
			       C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python39\\python.exe test.py"""
			echo "${TOKEN}"
        }
      }
    }
  }
}
