FROM python:3.14-slim-trixie

RUN pip install "fastapi[standard]" orjson

RUN apt-get update -y \
    && apt-get install git gzip gnupg2 just curl jq sudo -y \
    && apt-get autoremove -y \
    ; apt-get clean

ARG REMOTE_USER
ARG REMOTE_UID
ARG REMOTE_GID

# Create the user
RUN groupadd --gid $REMOTE_GID $REMOTE_USER \
    && useradd --uid $REMOTE_UID --gid $REMOTE_GID -m $REMOTE_USER \
    && echo $REMOTE_USER ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$REMOTE_USER \
    && chmod 0440 /etc/sudoers.d/$REMOTE_USER

# Set the default user
USER $REMOTE_USER
