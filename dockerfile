FROM python:3.7
EXPOSE 8000

COPY ./app /app

RUN pip3 install fastapi && \
    pip3 install uvicorn &&\
    pip3 install xmltodict &&\
    pip3 install requests

CMD [ "uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0" ]