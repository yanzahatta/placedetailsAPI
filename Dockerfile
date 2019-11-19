FROM python:3.7.0-slim
EXPOSE 1234
WORKDIR /code
COPY . /code
RUN pip install requests
CMD [ "python", "-u", "/code/main.py" ]
