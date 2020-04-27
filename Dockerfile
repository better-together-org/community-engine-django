FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN apt-get update -qq && apt-get install -y gettext
RUN mkdir /btce/
WORKDIR /btce/
# COPY Pipfile /btce/
# COPY Pipfile.lock /btce/
# RUN pip install --quiet pipenv
# RUN pipenv install --dev --system --ignore-pipfile
COPY . /btce/

RUN pip install cookiecutter

# Port to expose
EXPOSE 8000

# Set the docker image command to use the entrypoint
CMD ["/btce/entrypoint.sh"]
