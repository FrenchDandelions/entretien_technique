FROM python:3.12

# Define the working directory in the container
WORKDIR /app

# Copy application files into container
COPY . .

# Install dependencies
# (Make sure you have a requirements.txt file at the root of the project containing Flask and any other dependencies)
RUN pip install -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Set the environment variable to run the application in production mode
ENV FLASK_ENV=production

# Commande pour démarrer l'application
CMD ["flask", "run", "--host=0.0.0.0"]