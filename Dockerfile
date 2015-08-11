FROM mxabierto/python

RUN mkdir -p /root/api
COPY api/ /root/api
WORKDIR /root/api

RUN pip install -r requirements.txt

EXPOSE 80
CMD ["gunicorn", "--config=api/gunicorn.py", "api.app:app"]