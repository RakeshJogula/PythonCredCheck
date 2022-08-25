#!groovy

properties([
	parameters([
		string(defaultValue:"",description:"Project Name",name:'PROJECT_ID'),
		string(defaultValue:"",description:"Repo Name",name:'REPO_NAME'),
	])
])

echo "params: ${params}"

def map = [
	PROJECT_ID : params.PROJECT_ID.trim()
	REPO_NAME : params.REPO_NAME.trim()
]


pipeline {
  agent any
  stages {
    stage('Environment  Build') {
      steps {
        withCredentials([usernamePassword(credentialsId: '1', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')])
		{
			bat """set  DB_USERNAME="${USERNAME}"
			       set  DB_PASSWORD="${PASSWORD}" 
			       C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python39\\python.exe test.py"""
			bat "echo ${DB_PROJECT%"
			bat "echo ${map.PROJECT_ID.toLowerCase()}"
			bat "echo ${map.REPO_NAME.toLowerCase()}"

			
        }
      }
    }
  }
}
