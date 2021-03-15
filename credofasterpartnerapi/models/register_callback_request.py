# -*- coding: utf-8 -*-

"""
    credofasterpartnerapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class RegisterCallbackRequest(object):

    """Implementation of the 'RegisterCallbackRequest' model.

    TODO: type model description here.

    Attributes:
        url (string): Define a reachable URL that accepts a JSON Payload as
            described below
        tps (string): Define the transactions per second we should use when
            pushing callbacks to your side
        retries (string): A comma separated value, containing the number of
            seconds to wait for any retries and the max number of retries to
            do, when the clients endpoint responds with an Error

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "url":'url',
        "tps":'tps',
        "retries":'retries'
    }

    def __init__(self,
                 url='https://posthere.io/partner_test',
                 tps='10',
                 retries='1,5'):
        """Constructor for the RegisterCallbackRequest class"""

        # Initialize members of the class
        self.url = url
        self.tps = tps
        self.retries = retries


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        url = dictionary.get("url") if dictionary.get("url") else 'https://posthere.io/partner_test'
        tps = dictionary.get("tps") if dictionary.get("tps") else '10'
        retries = dictionary.get("retries") if dictionary.get("retries") else '1,5'

        # Return an object of this model
        return cls(url,
                   tps,
                   retries)


