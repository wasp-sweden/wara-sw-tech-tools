FROM ubuntu
ARG UID=1000
ARG GID=1000
ENV LANG C.UTF-8
RUN apt-get update
RUN apt-get install -y sudo bsdmainutils file git less tree binutils software-properties-common
RUN add-apt-repository -y ppa:cwchien/gradle
RUN apt-get update
RUN groupadd -g $GID ove
RUN useradd -m -s/bin/bash -u $UID -g $GID ove
RUN usermod -aG sudo ove
RUN mkdir /ove
RUN chown ove:ove /ove
RUN echo '%sudo ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers
USER $UID:$GID
COPY ove.bash /home/ove/.ove.bash
RUN echo '[ -f ~/.ove.bash ] && source ~/.ove.bash' >> /home/ove/.bashrc
WORKDIR /ove
ENTRYPOINT /bin/bash

