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


@task
def build_image(runner):
  runner.run("docker build . -t exl_my_app --rm")

@task(build_image)
def run_image(runner):
  runner.run("docker run -i exl_my_app")

@task
def run_debug(runner, args=None):
  runner.run('docker run -i -v "$(pwd)/../exl_base":/exl_base -e PYTHONPATH=":/exl_base/" exl_my_app {}'.format(args))

@task
def run(runner, args=None):
  runner.run('docker run -i exl_my_app {}'.format(args))
