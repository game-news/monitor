FROM python:3.6

USER root
ENV PYTHONUNBUFFERED=0
ENV PYTHONIOENCODING=utf-8

RUN pip3 install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip3 install scrapyd logparser -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY requirements.txt ./
RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY run.sh /run.sh
COPY scrapyd.conf /etc/scrapyd/

RUN mkdir /root/logs /root/items /root/eggs

RUN chmod 777 /run.sh

VOLUME /etc/scrapyd/ /var/lib/scrapyd/ /root/
EXPOSE 6800

CMD ["/run.sh"]