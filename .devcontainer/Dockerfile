#######################################################################################
##     The Base image with usable tools
#######################################################################################

FROM registry.access.redhat.com/ubi8/ubi-minimal:latest as osbase

LABEL maintainer="Alejandro Medici <alejandro.medici@bnextiteration.com.ar>" \
      name="nit-python3-dev-container" \
      author="NiT Team" \
      vendor="NiT" \
      release="0.1.0" \
      summary="NiT Dev Environment containers" \
      description="Defined the proper setup to be used with Visual Studio Code for Python3"

RUN microdnf update && \
    microdnf -y install wget tar gzip git && \
    microdnf clean all && rm -rf /var/cache/microdnf

RUN microdnf install -y python311  && \
    python -m ensurepip --default-pip && \
    python -m pip install --upgrade pip

COPY ./ /scripts

WORKDIR /scripts

RUN pip install -r requirements.txt

CMD ["/bin/bash"]