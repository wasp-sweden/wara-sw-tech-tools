FROM warasw/tep:latest
RUN bash -ic 'ove fetch depclean commons-numbers'
RUN sudo apt-get -y install maven openjdk-11-jdk
RUN bash -ic 'ove buildme depclean commons_numbers_examples'
