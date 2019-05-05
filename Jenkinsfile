
node {
    def image

    dockerRegistryUrl = "http://poc-nexus01.dc99:8123/repository/exl_docker"
    dockerRegistryCredentialsId = 'exl-docker-hub-credentials'

    stage('Clone repository') {
        /* Let's clone the repository into the JENKINS(!) workspace 
        */

        checkout scm
    }

    stage('Build image') {
        /* This builds the actual image. synonymous to
         * docker build on the commandline 
         */

        docker.withRegistry(dockerRegistryUrl, dockerRegistryCredentialId) {
            img = docker.build("exl_my_app:${env.BUILD_ID}", ". --build-arg GIT_TOKEN=${env.GIT_TOKEN} -f ./Dockerfile --rm --no-cache")
         }
    }

    stage('Test image') {
        /* we run a test framework against our image.
        */

        image.inside {
            // to fail run:
            sh 'echo "Tests passed"'
        }
    }

    stage('Push image') {
        /* Finally, we'll push the image with two tags:
         * First, the incremental build number from Jenkins
         * Second, the 'latest' tag.
         */
        docker.withRegistry(dockerRegistryUrl, dockerRegistryCredentialsId) {
            image.push()
            image.push("latest")
        }
    }
}