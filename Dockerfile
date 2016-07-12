FROM mxabierto/python

RUN mkdir -p /root/shogun
COPY . /root/shogun
WORKDIR /root/shogun

RUN pip install -r requirements.txt

EXPOSE 80
CMD ["/root/shogun/start.sh"]
