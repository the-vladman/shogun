FROM mxabierto/python

RUN mkdir -p /root/shogun
COPY . /root/shogun
WORKDIR /root/shogun

RUN pip install -r api/requirements.txt

EXPOSE 80
CMD ["gunicorn", "--config=api/gunicorn.py", "api.app:app"]