pipeline {
  agent any
  stages {
    stage('checkout code') {
      steps {
        git(url: 'https://github.com/adilrahman/simple-api.git', branch: 'main', changelog: true)
      }
    }

    stage('Logs') {
      steps {
        sh 'ls -la'
      }
    }

    stage('Build docker image') {
      steps {
        sh 'sudo docker build . -t bitbyte007/simple_api:latest'
      }
    }

  }
}