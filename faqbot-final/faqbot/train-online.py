from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import warnings

from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

logger = logging.getLogger(__name__)


def run_faqbot_online(input_channel, interpreter,
                          domain_file="domain.yml",
                          training_data_file='data/stories.md'):
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=2), KerasPolicy()],
                  interpreter=interpreter)

    training_data = agent.load_data(training_data_file)
    agent.train_online(training_data,
                       input_channel=input_channel,
                       batch_size=50,
                       epochs=200,
                       max_training_samples=300)

    return agent


if __name__ == '__main__':
    warnings.filterwarnings(action='ignore', category=DeprecationWarning)
    utils.configure_colored_logging(loglevel="INFO")
    nlu_interpreter=RasaNLUInterpreter('./models/nlu/default/current')
    run_faqbot_online(ConsoleInputChannel(), nlu_interpreter)
