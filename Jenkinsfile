pipeline {
    agent any
    stages {
        stage("DEV") {
            environment {
                HOME="."
            }
            agent {
                docker { image 'maven:3-alpine' }
            }
            steps {
                sh 'mvn --version'
            }
        }
        stage("QA") {
            steps {
                bat 'set'
            }
        }
        stage("UAT") {
            steps {
                bat 'set'
            }
        }
        stage("PERF") {
            steps {
                bat 'set'
            }
        }
        stage("PRE-PROD") {
            steps {
                bat 'set'
            }
        }
        stage("PROD") {
            steps {
                bat 'set'
            }
        }
    }
}