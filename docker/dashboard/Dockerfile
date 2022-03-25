FROM warasw/tep:latest
RUN bash -ic 'ove fetch wara-sw-tech-tools-dashboard'
RUN sudo apt-get -y install nodejs npm pkg-config python3-venv
RUN bash -ic 'ove buildme dashboard_components'
ENTRYPOINT ["/bin/bash", "-ic", "ove dashboard depclean"]