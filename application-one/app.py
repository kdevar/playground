from aws_cdk import (
    aws_sqs as sqs,
    aws_ecs as ecs,
    aws_ecr as ecr,
    aws_s3 as s3,
    aws_iam as iam,
    aws_ecs_patterns as ecs_patterns,
    aws_autoscaling as asg,
    core
)


class MyStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        ecr.Repository(
            self, "customer-extractor-jobs-repo",
            repository_name="customer-extractor-job"
        )

        sqs.Queue(
            self, "customer-extractor-jobs-queue",
            visibility_timeout=core.Duration.seconds(300)
        )


app = core.App()

stack = MyStack(app, "test", env={'region': 'us-east-1'})
app.synth()
