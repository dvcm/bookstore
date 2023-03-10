#syntax=docker/dockerfile:1
FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

    COPY requirements.txt requirements.txt
# RUN apt update && apt install -y python3-pip
# RUN pip install --upgrade setuptools
# NOTE: the 2 RUN above are the 2 latest attempts to find a solution by using a RUN line.
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "django", "run", "--host=0.0.0.0"]