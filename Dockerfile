FROM python:3.8-slim

COPY speedtest-cli.json /root/.config/ookla/
COPY *.py /srv/

RUN apt update && \
    apt install -y gnupg1 apt-transport-https dirmngr lsb-release curl && \
    curl -s https://install.speedtest.net/app/cli/install.deb.sh | bash && \
    apt install -y speedtest && \
    pip install /srv/

CMD python /srv/speedtest.py
