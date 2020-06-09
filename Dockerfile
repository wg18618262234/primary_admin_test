FROM python:3.7.6-slim-stretch
RUN echo "Asia/Chongqing" > /etc/timezone
RUN unlink /etc/localtime
RUN ln -s /usr/share/zoneinfo/Asia/Chongqing /etc/localtime
RUN apt update -y
RUN apt install gcc -y
RUN apt-get clean
RUN pip install virtualenv
RUN mkdir /opt/app
WORKDIR /opt/app
COPY dist/ /opt/app/
RUN virtualenv venv
RUN . venv/bin/activate
RUN pip install -r requirements.txt
CMD ["locust"]

