pipeline {
    agent {
        docker { image 'maven:3-alpine' }
    }
    stages {
        stage("DEV") {
            environment {
                HOME="."
            }
            steps {
                sh 'mvn --version'
            }
        }
        stage("QA") {
            steps {
                sh 'mvn --version'
            }
        }
        stage("UAT") {
            steps {
                sh 'mvn --version'
            }
        }
        stage("PERF") {
            steps {
                sh 'mvn --version'
            }
        }
        stage("PRE-PROD") {
            steps {
                sh 'mvn --version'
            }
        }
        stage("PROD") {
            steps {
                sh 'mvn --version'
            }
        }
    }
}