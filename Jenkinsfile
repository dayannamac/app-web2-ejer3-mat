node {
    stage ('Revisión') {
        checkout scm
    }

    stage ('Instalación de dependencias') {
        bat 'npm install'
    }

    stage ('Construir') {
        bat 'npm run ng build'
    }

    //Borrrar carpeta del html
    stage ('Eliminar contenido del servidor') {
        bat 'rd /s /q D:\\Servidor\\fire'
    }

    stage ('Mover al servidor') {
        bat 'xcopy C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\angular-pipeline\\dist\\app-03\\browser D:\\Servidor\\fire /E /I /Y'
    }
}