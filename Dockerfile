FROM supervisely/base-py-sdk:6.68.26

RUN pip install pyzbar 0.1.9
RUN pip install -r requirements.txt
