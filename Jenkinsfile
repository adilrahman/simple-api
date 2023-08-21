pipeline {
  agent any
  stages {
    stage('error') {
      steps {
        git(url: 'https://github.com/adilrahman/simple-api.git', branch: 'main', changelog: true)
      }
    }

  }
}