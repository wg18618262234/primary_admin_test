def remote = [:]
remote.name = 'master'
remote.host = 'test-1to6.yc345.tv'
remote.user = 'master'
remote.password = 'unitedmaster'
remote.allowAnyHosts = true
remote.pty = true

def running_dir = '/home/master/running'
pipeline {
    agent {
        docker {
            reuseNode false
            image 'docker.yc345.tv/1to6/primary-python-build:latest'
            registryUrl 'https://docker.yc345.tv'
            registryCredentialsId 'docker-credit'
            alwaysPull true
            args '--dns 10.8.8.12 -v /var/run/docker.sock:/var/run/docker.sock -v /usr/bin/docker:/usr/bin/docker -v /etc/docker:/etc/docker'
        }
    }

    environment {
        deploy_file = "deploy-${env.GIT_COMMIT}.tar.gz"
        project_name = "${env.GIT_URL.replaceFirst(/^.*\/([^\/]+?).git$/, '$1').toLowerCase()}"
    }

    stages {
        stage('build') {
            steps {
                sh 'rm -rf dist && mkdir -p dist && cp ./*.py dist/ && cp -R static dist/ && cp -R templates dist/ && cp -R tasksets dist/ && cp -R unit dist/ && cp ./*.txt dist/ && cp start.sh dist/'
                sh 'ls -al dist/'
                sh "tar zvcf ${env.deploy_file} dist"
            }
        }
        stage("build image") {
            when {
                anyOf {
                    branch "test"
                    branch "master"
                    tag "v*"
                }
            }
            steps {
                sshCommand remote:remote, command: "mkdir -p ${running_dir}/${env.project_name}/${env.GIT_COMMIT}"
                sshPut remote:remote, from: "${env.deploy_file}", into: "${running_dir}/${env.project_name}/${env.GIT_COMMIT}"
                sshPut remote:remote, from: "Dockerfile", into: "${running_dir}/${env.project_name}/${env.GIT_COMMIT}"
                sshCommand remote:remote, command: 'cp ~/.ssh/id_rsa ./'
                sshCommand remote:remote, command: "/home/master/bin/docker-build.sh ${env.project_name} ${env.GIT_COMMIT}"
            }
        }
        stage("deploy") {
            when {
                anyOf {
                    branch "test"
                    branch "master"
                }
            }
            steps {
                script {
                    sshCommand remote:remote, command: "/home/master/bin/docker-tag.sh ${env.project_name} ${env.GIT_COMMIT} ${env.BRANCH_NAME}"
                    if (env.BRANCH_NAME == 'master') {
                        sh "echo skip"
                    } else {
                        sshCommand remote:remote, command: "/home/master/bin/k8s-deploy.sh ${env.project_name} ${env.BRANCH_NAME} golang"
                    }
                }
            }
        }
        stage("publish tags") {
            when {
                tag "*"
            }
            steps {
                sshCommand remote:remote, command: "/home/master/bin/docker-tag.sh ${env.project_name} ${env.GIT_COMMIT} ${env.BRANCH_NAME}"
                echo "tag success"
            }
        }
    }
    post {
        always {
            sshCommand remote:remote, command: "rm -rf ${running_dir}/${env.project_name}/${env.GIT_COMMIT}"
            sh "rm -rf ${env.deploy_file}"
        }
    }
}
