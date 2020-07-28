FROM python:3.8-slim

ENV INSTALL_KEY=379CE192D401AB61

COPY speedtest-cli.json /root/.config/ookla/
COPY *.py /srv/

RUN apt update && \
    apt install -y gnupg1 apt-transport-https dirmngr lsb-release && \
    export DEB_DISTRO=$(lsb_release -sc) && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys $INSTALL_KEY && \
    echo "deb https://ookla.bintray.com/debian ${DEB_DISTRO} main" | tee  /etc/apt/sources.list.d/speedtest.list && \
    apt update && \
    apt install -y speedtest && \
    pip install /srv/

CMD python /srv/speedtest.py