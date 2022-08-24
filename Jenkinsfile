pipeline 
{
  agent any
  stages 
  {
    stage('Credential Setup')
	{
      steps 
	  {
        withCredentials([usernamePassword(credentialsId: '1', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) 
		{
          bat """set DB_USERNAME="${USERNAME}" set DB_PASSWORD = "${PASSWORD}"""
        }
      }
    }
	 stage('build') 
	{
      steps {
          bat ""python test.py ""
        }
    }
  }
}
