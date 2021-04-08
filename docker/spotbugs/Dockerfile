FROM warasw/tep:latest
RUN bash -ic 'ove fetch spotbugs cassandra'
RUN bash -ic 'ove patch spotbugs cassandra'
RUN sudo apt-get -y install ant maven openjdk-11-jdk python2.7
RUN bash -ic 'ove buildme spotbugs'