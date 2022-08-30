#FROM python:3.7.13
ARG PGUID=1000
ARG PUID=1000

FROM python:latest

RUN python -m pip install requests
RUN python -m pip install --upgrade pip
RUN pip install eth-tester 
RUN pip install web3
RUN pip install py-solc-x
#RUN pip install -U "web3[tester]"
COPY ./eth.py ./home/eth.py
RUN chmod +x ./home/eth.py
#RUN ./home/eth.py
WORKDIR ./home


