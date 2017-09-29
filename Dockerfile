FROM registry.centos.org/centos/centos:7
RUN yum update -y
RUN mkdir -p /opt/scripts
COPY . /app
WORKDIR /app
ADD ./fix-permissions.sh ./install.sh ./passwd.template ./run.sh /opt/scripts/
RUN chmod -R 777 /opt/scripts && . /opt/scripts/install.sh
EXPOSE 5000
USER python_user
ENTRYPOINT ["/opt/scripts/run.sh"]
CMD ["app"]
