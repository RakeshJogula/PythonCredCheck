pipeline {
  agent any
  stages {
    stage('Download tokens') {
        withCredentials([string(credentialsId: '2', variable: 'token')]) {

            sh "export token=${token}"

             sh """
                   export token="${token}"

                   python3 script.py
             """

        }
    }

  }
}
