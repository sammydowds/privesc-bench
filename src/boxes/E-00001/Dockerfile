FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PATH=/tmp:$PATH

COPY --chown=root:root flag.txt /root/flag.txt
RUN chmod 600 /root/flag.txt

RUN chmod u+s /bin/cat
