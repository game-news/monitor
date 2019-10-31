FROM python:3.7

USER root
ENV PYTHONUNBUFFERED=0
ENV PYTHONIOENCODING=utf-8

RUN pip3 install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip3 install scrapydweb -i https://pypi.tuna.tsinghua.edu.cn/simple

RUN mkdir /projects /data
COPY scrapydweb_settings_v10.py scrapydweb_settings_v10.py

VOLUME /projects /data

EXPOSE 5000

CMD ["scrapydweb"]