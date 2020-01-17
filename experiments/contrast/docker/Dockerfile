FROM anapsix/alpine-java:jdk8

ENV APP /
RUN apk update && apk add ca-certificates && update-ca-certificates && apk add openssl
RUN apk update; apk add curl

RUN wget https://github.com/WebGoat/WebGoat/releases/download/7.1/webgoat-container-7.1-exec.jar
RUN curl -X GET https://eval.contrastsecurity.com/Contrast/api/ng/8983b8a4-d70b-41a9-8a53-f8c8e3e064d6/agents/default/JAVA -H 'Authorization: bXIubWFyY28uYS5tb3JhbGVzQGdtYWlsLmNvbTpVQUVSUU1QWTdVME8yNldQ' -H 'API-Key: FgtEu342x22HkR2nFe1aR65V9esgd1EU' -H 'Accept: application/json' -OJ

COPY target/contrast_security.yaml /etc/contrast/java/contrast_security.yaml

WORKDIR $APP
EXPOSE 8080
CMD ["java","-javaagent:contrast.jar","-Dcontrast.agent.java.standalone_app_name=WebGoatDocker","-Dcontrast.server.name=DockerServer","-jar","webgoat-container-7.1-exec.jar"]
