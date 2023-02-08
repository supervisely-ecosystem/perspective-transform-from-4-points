FROM supervisely/base-py-sdk:6.68.26

COPY requirements.txt .
RUN apt-get update -y
RUN apt-get install -y libzbar0
RUN pip install -r requirements.txt
