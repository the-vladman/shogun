FROM mxabierto/python

RUN mkdir -p /root/shogun
COPY . /root/shogun
WORKDIR /root/shogun

RUN apk update && apk add git bash

RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["/root/shogun/start.sh"]