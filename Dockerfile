# use Python 3.7
FROM python:3.7

USER root

ENV WEBSITES_CONTAINER_START_TIME_LIMIT=60

WORKDIR /user_backend

# Add requirements.txt
COPY requirements.txt /user_backend/
 
# Install uwsgi Python web server
RUN pip install uwsgi
# Install app requirements
RUN pip install -r requirements.txt
 
# Create app directory
COPY . /user_backend
 
# Set the default directory for our environment
ENV HOME /user_backend
WORKDIR /user_backend
 
# Expose port 5000
EXPOSE 5000

RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["/bin/bash","-c","chmod +x ./entrypoint.sh && ./entrypoint.sh"]

#RUN chmod +x ./start_app.sh
#CMD ["/bin/bash","-c","chmod +x ./start_app.sh && ./start_app.sh"]


