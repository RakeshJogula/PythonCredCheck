pipeline {
  agent any
  stages {
    stage('Environment  Build') {
      steps {
        withCredentials([usernamePassword(credentialsId: '1', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
			bat """set  DB_USERNAME="${USERNAME}"
			       set  DB_PASSWORD="${PASSWORD}
			       set  DB_PROJECTNAME = "${PROJECT}
			       set  DB_REPO = "${REPO}"
		
        }
      }
    }
  }
}
