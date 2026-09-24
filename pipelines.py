pipeline {
    agent any

    parameters {
        // Defines the boolean parameter for sending email
        booleanParam(name: 'SEND_EMAIL', defaultValue: true, description: 'Check to send email notification')
    }

    environment {
        // Custom environment block defining app details
        APP_NAME = 'InventoryManager'
        APP_VERSION = '2.4.1'
    }

    stages {
        stage('Checkout') {
            steps {
                // 1. REPLACE THE URL BELOW WITH YOUR GIT REPOSITORY URL
                git url: 'https://github.com/KonankiPranavi/jenkins_lab.git', branch: 'main'
            }
        }

        stage('Build') {
            steps {
                echo "Compiling app.py..."
                echo "Application Name: ${env.APP_NAME}"
                echo "Application Version: ${env.APP_VERSION}"
            }
        }

        stage('Send Notification') {
            when {
                // Controls execution based on the boolean parameter
                expression { params.SEND_EMAIL == true }
            }
            steps {
                // 2. REPLACE THE TO ADDRESS WITH YOUR ACTUAL EMAIL
                mail to: 'pranavikonamki@gmail.com',
                     subject: "${env.APP_NAME} v${env.APP_VERSION} Build Notification",
                     body: "The pipeline build for ${env.APP_NAME} version ${env.APP_VERSION} completed successfully."
            }
        }
    }
}
