# coding: utf8
## start by pulling the python image
FROM python:3.11-bullseye
#
## copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt
#FROM python:3.10

#RUN python3 -m venv /opt/venv

# switch working directory
WORKDIR /app


## install the dependencies and packages in the requirements file
#RUN pip install -r requirements.txt

#COPY requirements.txt .
RUN pip install gcc7 && pip install -r requirements.txt && pip install ibm_db

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py"]