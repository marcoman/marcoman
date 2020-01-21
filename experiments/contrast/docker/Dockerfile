FROM anapsix/alpine-java:jdk8

ENV APP /
RUN apk update && apk add ca-certificates && update-ca-certificates && apk add openssl
RUN apk update; apk add curl

RUN wget https://github.com/WebGoat/WebGoat/releases/download/7.1/webgoat-container-7.1-exec.jar
RUN curl -X GET https://eval.contrastsecurity.com/Contrast/api/ng/UID/agents/default/JAVA -H 'Authorization: AUTH' -H 'API-Key: KEY' -H 'Accept: application/json' -OJ

COPY target/contrast_security.yaml /etc/contrast/java/contrast_security.yaml

WORKDIR $APP
EXPOSE 8080
CMD ["java","-javaagent:contrast.jar", "-Dcontrast.inspect.allclasses=false", "-Dcontrast.process.codesources=false", "-Dcontrast.agent.java.standalone_app_name=WebGoatDocker", "-Dcontrast.server.name=DockerServer","-jar","webgoat-container-7.1-exec.jar"]
