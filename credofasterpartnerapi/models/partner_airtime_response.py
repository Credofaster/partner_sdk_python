# -*- coding: utf-8 -*-

"""
    credofasterpartnerapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class PartnerAirtimeResponse(object):

    """Implementation of the 'PartnerAirtimeResponse' model.

    Response you get for A Request

    Attributes:
        error_code (int): Code for the Request API Generated. 0: Success, Any
            other Error Code, refer to ErrorCodes Page
        error_description (string): Text Description
        reference_id (uuid|string): a UUID Returned for the Transaction
        request_id (uuid|string): Return of the Clients Request ID

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "error_code":'ErrorCode',
        "error_description":'ErrorDescription',
        "reference_id":'ReferenceId',
        "request_id":'RequestId'
    }

    def __init__(self,
                 error_code=0,
                 error_description=None,
                 reference_id=None,
                 request_id=None):
        """Constructor for the PartnerAirtimeResponse class"""

        # Initialize members of the class
        self.error_code = error_code
        self.error_description = error_description
        self.reference_id = reference_id
        self.request_id = request_id


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
        error_code = dictionary.get("ErrorCode") if dictionary.get("ErrorCode") else 0
        error_description = dictionary.get('ErrorDescription')
        reference_id = dictionary.get('ReferenceId')
        request_id = dictionary.get('RequestId')

        # Return an object of this model
        return cls(error_code,
                   error_description,
                   reference_id,
                   request_id)


