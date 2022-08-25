#!groovy

properties([
	parameters([
		string(defaultValue:"",description:"Project Name",name:'PROJECT_ID'),
		string(defaultValue:"",description:"Repo Name",name:'REPO_NAME'),
	])
])

bat 'echo "params: ${params}"'



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
			bat "echo ${params.PROJECT_ID.toLowerCase()}"
			bat "echo ${params.REPO_NAME.toLowerCase()}"

			
        }
      }
    }
  }
}
