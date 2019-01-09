# Use Python latest image
FROM python

# install required packages
RUN apt-get -y install libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
RUN pip install Scrapy==1.5.1

# specify Work Directory
WORKDIR /usr/src/app
COPY . /usr/src/app/
