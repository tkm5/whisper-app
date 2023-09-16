FROM ubuntu:latest

# Update the package list and install necessary packages
RUN apt -y update && apt install -y \
ffmpeg \
python3-pip

# Set the working directory in the container to /src
WORKDIR /src
COPY . /src

# Install OpenAI Whisper and other dependencies from requirements.txt
RUN pip install -U openai-whisper
RUN pip install -r requirements.txt

# Run the main Python script when the container launches
CMD ["python3", "main.py"]