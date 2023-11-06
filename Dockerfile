FROM python:3.11.5
RUN chmod 755 .
# RUN mkdir /app
WORKDIR .
COPY . .
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD ["python3", "main.py"]