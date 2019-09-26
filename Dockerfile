FROM raspbian/stretch:latest
# Enable systemd
ENV INITSYSTEM on
# Your code goes here
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev
WORKDIR /app
RUN echo "start"
RUN python -m pip install --upgrade pip
RUN pip install --upgrade pip
WORKDIR /app/tbot
RUN pip install python-telegram-bot --upgrade
RUN apt-get update
RUN apt-get install -y git
RUN useradd -m pi
ADD ./app /app/tbot
RUN chown -R pi /app
RUN sh install_dth.sh
#RUN pip install requests[socks]
RUN pip install pysocks
WORKDIR /app/tbot
CMD ["sudo","python","bot.py"]
