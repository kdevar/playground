FROM kdevarakonda/cdk-python

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY . .

CMD ["cdk", "ls"]