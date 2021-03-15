# -*- coding: utf-8 -*-

"""
    credofasterpartnerapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from credofasterpartnerapi.decorators import lazy_property
from credofasterpartnerapi.configuration import Configuration
from credofasterpartnerapi.controllers.main_controller import MainController
from credofasterpartnerapi.controllers.events_controller import EventsController


class CredofasterpartnerapiClient(object):

    config = Configuration

    @lazy_property
    def main(self):
        return MainController()

    @lazy_property
    def events(self):
        return EventsController()


    def __init__(self,
                 api_key='XXXX-XXXX-XXXX-XXXX',
                 client_id='ABCDEDFG1234'):
        if api_key is not None:
            Configuration.api_key = api_key
        if client_id is not None:
            Configuration.client_id = client_id

