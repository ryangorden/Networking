FROM ubuntu
LABEL maintainer="ryanw.gorden@gmail.com"

RUN apt-get update -y && apt-get install -y python3-pip python3-dev



COPY ./requirements.txt /warren_easton/requirements.txt


WORKDIR /warren_easton

RUN pip3 install -r requirements.txt

COPY ./warren_easton /warren_easton



# Run the program by starting flask
ENTRYPOINT ["python3"]
CMD ["update_portAccess.py"]

