FROM python:3

WORKDIR /app

COPY requirements.txt requirements.txt

ENV BUILD_DEPS="" \
    APP_DEPS="atomicparsley ffmpeg"

RUN apt-get update \
  && apt-get install -y ${BUILD_DEPS} ${APP_DEPS} --no-install-recommends \
  && pip install -r requirements.txt \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /usr/share/doc && rm -rf /usr/share/man \
  && apt-get purge -y --auto-remove ${BUILD_DEPS} \
  && apt-get clean

COPY ./flask-youtubeDL/. .

ENTRYPOINT [ "python" ]
CMD ["app.py"]
