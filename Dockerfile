FROM tiangolo/uwsgi-nginx:python3.8
ENV UWSGI_INI uwsgi.ini
ENV TZ="Asia/Tehran"
ENV STATIC_URL /app/static_collected
ENV NGINX_MAX_UPLOAD 64m
ENV UWSGI_CHEAPER 8
ENV UWSGI_PROCESSES 256
ENV NGINX_WORKER_PROCESSES auto
ENV NGINX_WORKER_CONNECTIONS 2048
ENV NGINX_WORKER_OPEN_FILES 4096
WORKDIR /app
ADD . /app
# COPY /MEDIA /home/docker-compose/data/media/MEDIA
RUN chmod g+w /app
RUN apt-get update && \
    apt-get install -y libmariadb-dev && \
      rm -rf /var/lib/apt/lists/*
#RUN python3 -m pip install -i http://p.docker-registry.ir/PyPi/simple --trusted-host p.docker-registry.ir -r requirements.txt
RUN python3 -m pip install -r requirements.txt
#RUN python3 -m pip install -r requirements.txt
