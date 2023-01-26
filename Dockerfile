FROM nvidia/cuda:11.6.2-base-ubuntu20.04
#FROM nvidia/cuda:12.0.0-base-ubuntu20.04

# Disable Prompt During Packages Installation
ARG DEBIAN_FRONTEND=noninteractive


RUN apt update && apt --no-install-recommends -y install \
    python3 \
    python3-pip \
    ffmpeg \
    libsm6 \
    libxext6
    

RUN pip install \
    opencv-python \
    numpy \
    imutils

WORKDIR /app
COPY run.py .
CMD python3 run.py