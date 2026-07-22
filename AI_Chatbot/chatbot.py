import random
import re

from patterns import patterns
from database import responses


def chatbot_response(user_input):

    user_input = user_input.lower()

    for category, keywords in patterns.items():

        for keyword in keywords:

            if re.search(r'\b' + keyword + r'\b', user_input):

                return random.choice(responses[category])


    return random.choice(responses["default"])