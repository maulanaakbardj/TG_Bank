FROM python:3.7
RUN apt-get update && apt-get -y install cron vim
WORKDIR /app
RUN pip3 install numpy
RUN pip3 install pytigergraph
RUN pip3 install pytz
RUN pip3 install pandas
RUN pip3 install sqlalchemy
RUN pip3 install pymysql
RUN pip3 install python-dateutil
COPY crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab
RUN /usr/bin/crontab /etc/cron.d/crontab
COPY DataUploading_All_UC.py DataUploading_All_UC.py
COPY /data /app
RUN echo $PYTHONPATH
# run crond as main process of container
CMD ["cron", "-f"]
