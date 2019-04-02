from exl_base import ExlConf
from exl_base import ExlLogger
from exl_base import ExlInitializer
from exl_base import ExlBaseApp
from exl_base import ExlCmdlineArgs
from exl_base import ExlSecrets
from exl_common import ExlSshUtils

import traceback
import sys
import os

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

        # Logging example
        logger = ExlBaseApp.theApp().logger   # same as ExlLogger.instance()
        logger.info("initial info msg")
        # logger.debug("initial debug msg")
        # logger.warning("initial warnning msg")
        # logger.error("initial error msg")
        # logger.critical("initial critical msg")

        #configuration management that is environment aware:
        conf_val_1 = ExlConf.instance().get('test', 'key1')
        conf_val_2 = ExlConf.instance().get('test', 'key2')
        conf_val_3 = ExlConf.instance().get('test', 'key3')

        logger.debug("env is {} and val1 => [{}] val2 => [{}] val3 => [{}]".format(os.environ['EXL_ENV'], conf_val_1, conf_val_2, conf_val_3))

        # Configuration Management example
        test_user = ExlConf.instance().get('auth', 'test_user', 'no user!!')
        logger.info("test user is: {}".format(test_user))

        # Secret Management example
        secret_log_mgmt = ExlSecrets.instance().get('secret/dev/log_mgmt')
        print("my best kept secret is: {} : {}".format(secret_log_mgmt['elkUsername'], secret_log_mgmt['elkPassword']))

        # Argument Parser example 1
        times = ExlCmdlineArgs.instance().get('times', 0)
        logger.info("going to print me {} times".format(times))
        for i in range(times):
            logger.info("me")

        # Argument Parser example 2
        # personName = ExlCmdlineArgs.instance().get('name', None)
        # logger.info("got person: {}".format(personName))

        # SSH usage example
        # ssh = ExlSshUtils("ssh-gr2.vpnjantit.com", 'kuku-vpnjantit.com', 'miaomiao123')
        # ssh.execute_command(['ls'])

    except Exception as e:
        print(
            "Failed. ex: {}".format(e))
        traceback.print_exc(file=sys.stdout)


if __name__ == '__main__':
    main()
