# Use Python latest image
FROM python

# install required packages
RUN apt-get -y install libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
