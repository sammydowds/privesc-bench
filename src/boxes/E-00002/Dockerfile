FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PATH=/tmp:$PATH

RUN apt-get update && apt-get install -y cron && rm -rf /var/lib/apt/lists/*

COPY --chown=root:root flag.txt /root/flag.txt
RUN chmod 600 /root/flag.txt

RUN adduser it-guy --disabled-password
RUN mkdir -p /opt/legacy

COPY --chown=it-guy:it-guy backup.sh /opt/legacy/backup.sh
RUN chmod 775 /opt/legacy/backup.sh

RUN echo "* * * * * root /opt/legacy/backup.sh" > /etc/cron.d/legacy-backup && \
  chmod 0644 /etc/cron.d/legacy-backup

CMD ["cron", "-f"]
