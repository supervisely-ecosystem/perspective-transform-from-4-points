FROM supervisely/base-py-sdk:6.72.56

RUN apt-get update -y
RUN apt-get install -y libzbar0

COPY dev_requirements.txt dev_requirements.txt
RUN pip install -r dev_requirements.txt
