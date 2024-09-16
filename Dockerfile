FROM rezah65/djbase:5.1

# Installing all python dependencies
ADD requirements/ requirements/
RUN pip install -r requirements/development.txt


# Get the django project into the docker container
RUN mkdir /app
WORKDIR /app
ADD ./ /app/

