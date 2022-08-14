FROM python:3.8-slim

COPY speedtest-cli.json /root/.config/ookla/
COPY *.py /srv/

RUN apt update && \
    apt install -y gnupg1 apt-transport-https dirmngr lsb-release curl && \
    curl -s https://packagecloud.io/install/repositories/ookla/speedtest-cli/script.deb.sh | bash  && \
    apt install -y speedtest && \
    pip install /srv/

CMD python /srv/speedtest.py
