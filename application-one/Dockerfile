FROM kdevarakonda/cdk-python

COPY requirements.txt ./
RUN pip3 install -r rquirements.txt

COPY . .

CMD ["cdk", "ls"]