from exl_base import ExlConf
from exl_base import ExlLogger
from exl_base import ExlInitializer
from exl_base import ExlBaseApp
from exl_base import ExlCmdlineArgs
from exl_base import ExlSecrets

import traceback
import sys

from pkg_resources import Requirement, resource_filename


app = None


def app_init():
  # define command line arguments for this app
    ExlCmdlineArgs.instance().add_arg(
        '--times', 'number of times to print me...', '-t', int, 0, required=True)

    ExlCmdlineArgs.instance().add_group_arg(
        'person',
        '--name', 'name of person in one word', '-n', required=True
    )

    ExlCmdlineArgs.instance().add_group_arg(
        'person',
        '--job', 'job of person (default: generic)', '-j', default='Generic'
    )

    # will exit process if failes - look for logger messages
    app = ExlBaseApp(
        app_name='my_sample_app',
        app_desc="This is my sample app description..."
    )

    # you can do here whatever initialization you wish to do before the global initializer is being executed
    # to initialize app objects such as config, arg parser, logger etc
    app.initApp()


def main():
    try:

        app_init()

        logger = ExlBaseApp.theApp().logger   # same as ExlLogger.instance()

        logger.info("initial info msg")
        logger.debug("initial debug msg")
        logger.warning("initial warnning msg")
        logger.error("initial error msg")
        logger.critical("initial critical msg")

        test_user = ExlConf.instance().get('auth', 'test_user', 'no user!!')

        logger.info("test user is: {}".format(test_user))

        # secret = ExlSecrets.instance().get('secret/exl')
        # logger.critical("my best kept secret is: {} : {}".format(secret['db']['user'],
        #                                                          secret['db']['pass']))

        times = ExlCmdlineArgs.instance().get('times', 0)
        logger.info("going to print me {} times".format(times))
        for i in range(times):
            logger.info("me")

        personName = ExlCmdlineArgs.instance().get('name', None)
        logger.info("got person: {}".format(personName))

    except Exception as e:
        print(
            "Failed. ex: " + e.message)
        traceback.print_exc(file=sys.stdout)


if __name__ == '__main__':
    main()
