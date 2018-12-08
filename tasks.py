from invoke import task


@task
def install(c):
    """
    this will pip install requirements.txt
    """
    c.run('pip install -r requirements.txt')


@task
def upgrade(c):
    """
    this will pip install and upgrade required packages from requirements.txt
    """
    c.run('pip install -r requirements.txt --upgrade')
