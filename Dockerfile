FROM python:3.7.13
RUN python -m pip install requests
RUN python -m pip install --upgrade pip
RUN pip install eth-tester 
RUN pip install web3

WORKDIR ./home


