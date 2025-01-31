FROM python:3.11

# set working directory in the container
WORKDIR /app

# copy files into container
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# expose the port Flask runs on
EXPOSE 5000

# command to run the application
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
