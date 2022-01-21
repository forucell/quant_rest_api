FROM python

RUN mkdir /app
ADD . /app

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -e .

ENTRYPOINT ["gunicorn"]

CMD ["--bind", "0.0.0.0:80", "quant.wsgi:app"]

EXPOSE 80
