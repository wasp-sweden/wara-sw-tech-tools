FROM ubuntu
ARG UID=1000
ARG GID=1000
ENV LANG C.UTF-8
ENV TZ=Etc/GMT-1
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update
RUN apt-get install -y sudo bsdmainutils file git less tree binutils software-properties-common python3 python3-pip
RUN pip3 install plotly dash pandas
RUN add-apt-repository -y ppa:cwchien/gradle
RUN apt-get update
RUN groupadd -g $GID ove
RUN useradd -m -s/bin/bash -u $UID -g $GID ove
RUN usermod -aG sudo ove
RUN mkdir /ove
RUN chown ove:ove /ove
RUN echo '%sudo ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers
USER $UID:$GID
COPY --chown=ove:ove docker/ove.bash /home/ove/.ove.bash
COPY --chown=ove:ove docker/ove /ove/.ove
RUN echo '[ -f ~/.ove.bash ] && source ~/.ove.bash' >> /home/ove/.bashrc
WORKDIR /ove
COPY --chown=ove:ove . /ove/wara-sw-tech-tools
RUN ln -s .ove/ove ove
RUN ln -s wara-sw-tech-tools .owel
ENTRYPOINT /bin/bash
