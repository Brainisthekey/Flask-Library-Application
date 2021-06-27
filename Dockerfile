FROM python:3.8
EXPOSE 5000/tcp
WORKDIR /src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /src
CMD [ "python", "./app.py" ]