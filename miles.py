pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Automatically checks out code from your pipelinesmilestone repository
                git url: 'https://github.com/KonankiPranavi/pipelinesmilestone.git', branch: 'main'
            }
        }

        stage('Build') {
            steps {
                echo 'Compiling app.py...'
                // Waits for 20 seconds before proceeding
                sleep time: 20, unit: 'SECONDS'
                // First milestone check
                milestone(1)
            }
        }

        stage('Deploy') {
            steps {
                // Milestone 2 at the very start of deployment
                milestone(2)
                echo 'Deploying application to production environment...'
            }
        }
    }
}
