FROM kdevarakonda/cdk-python

WORKDIR /app

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY . .


RUN ls

RUN cdk ls

USER root

CMD ["cdk", "ls"]