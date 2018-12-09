from invoke import task


@task
def install(runner):
    """
    this will pip install requirements.txt
    """
    runner.run('pip install -r requirements.txt')


@task
def upgrade(runner):
    """
    this will pip install and upgrade required packages from requirements.txt
    """
    runner.run('pip install -r requirements.txt --upgrade')


@task
def clean(runner):
    runner.run("rm -rf *.log*")
