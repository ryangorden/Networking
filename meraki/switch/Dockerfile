FROM ubuntu
LABEL maintainer="ryangroden@gmail.co>

RUN apt-get update -y && apt-get inst>



COPY ./requirements.txt /src/requirem>


WORKDIR /warren_easton

RUN pip3 install -r requirements.txt

COPY ./warren_easton /warren_easton



# Run the program by starting flask
ENTRYPOINT ["python3"]
CMD ["update_portAccess.py"]

