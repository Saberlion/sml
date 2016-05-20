FROM ubuntu:14.04
MAINTAINER saberlion <admin@saberlion.info>

ENV DEBIAN_FRONTEND noninteractive
copy . /var/www/
RUN apt-get update
RUN apt-get -y install nginx  sed python-pip python-dev supervisor

RUN pip install -r /var/www/requirements.txt

ENV MODE DEVELOPMENT

RUN mkdir -p /var/log/nginx/app
RUN mkdir -p /data/db/

RUN rm /etc/nginx/sites-enabled/default
COPY flask.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/flask.conf /etc/nginx/sites-enabled/flask.conf

RUN echo "daemon off;" >> /etc/nginx/nginx.conf


RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 80
#CMD nohup "gunicorn -w 2 App:app -b 0.0.0.0:80 &"
#CMD ["nohup", "gunicorn -w 2 App:app -b 0.0.0.0:80 &"]
#CMD ["gunicorn","-w 2","run:app","-b 0.0.0.0:80"]
#CMD ["python","run.py"]
CMD ["/usr/bin/supervisord"]