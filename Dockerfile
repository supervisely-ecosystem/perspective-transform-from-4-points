FROM supervisely/base-py-sdk:6.68.26

RUN apt-get update -y
RUN apt-get install -y libzbar0

COPY requirements.txt .
RUN pip install -r requirements.txt
