# Filename: Dockerfile
FROM debian:stable-slim
# Drop all man pages, documentation, changelogs, Debian
RUN echo "path-exclude=/usr/share/man/*" > /etc/dpkg/dpkg.cfg.d/excludes
RUN echo "path-exclude=/usr/share/doc/*" >> /etc/dpkg/dpkg.cfg.d/excludes
RUN echo "path-include=/usr/share/doc/*/copyright" >> /etc/dpkg/dpkg.cfg.d/excludes
RUN echo "path-include=/usr/share/doc/*/changelog.Debian.*" >> /etc/dpkg/dpkg.cfg.d/excludes

RUN apt-get update && \
  apt-get install -y \
  python3 \
  python3-protobuf \
  python3-influxdb
WORKDIR /opt/jun-telemetry
COPY . .
EXPOSE 50000
ENTRYPOINT ["/opt/jun-telemetry/jun-telemetry.py"]