pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'docker build -t shortscore-server .'
      }
    }
    stage('Test') {
      steps {
        sh 'echo "Test"'
      }
    }
  }
}
