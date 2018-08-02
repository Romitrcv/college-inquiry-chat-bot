from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import logging
import warnings

from rasa_core import utils
from rasa_core.actions import Action
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.events import SlotSet
from rasa_core.featurizers import (
    MaxHistoryTrackerFeaturizer,
    BinarySingleStateFeaturizer)
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies.memoization import MemoizationPolicy

logger = logging.getLogger(__name__)




def train_nlu():
    from rasa_nlu.training_data import load_data
    from rasa_nlu import config
    from rasa_nlu.model import Trainer

    training_data = load_data('data/training_data.json')
    trainer = Trainer(config.load("nlu_model_config.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist('models/nlu/',
                                      fixed_model_name="current")

    return model_directory



if __name__ == '__main__':
    train_nlu()
