__author__ = "CSA"
__maintainer__ = "CSA"
__copyright__ = "Copyright 2019, Ex Libris"
__credits__ = ["CSA"]
__version__ = "0.0.1"
__email__ = "elie.ifrah@exlibrisgroup.com"
__status__ = "Development"

from invoke import task


@task
def install(runner):
    """
    this will pip install requirements.txt
    """
    runner.run("pip install -r requirements.txt")


@task
def upgrade(runner):
    """
    this will pip install and upgrade required packages from requirements.txt
    """
    runner.run("pip install -r requirements.txt --upgrade")


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
def run_debug(runner, env, args=None):
    runner.run(
        'docker run -i -v "$(pwd)/../exl_base":/src/exl_base -e EXL_ENV="{}" exl_my_app {}'.format(
            env, args
        )
    )


@task
def run_dev(runner, env, args=None):
    runner.run(
        'docker run -i -e EXL_ENV={} -v "$(pwd)":/src exl_my_app {}'.format(env, args)
    )


@task
def run(runner, env, args=None):
    runner.run("docker run -i -e EXL_ENV={} exl_my_app {}".format(env, args))
