# coding: utf-8

"""
    Trieve API

    Trieve OpenAPI Specification. This document describes all of the operations available through the Trieve API.

    The version of the OpenAPI document: 0.11.8
    Contact: developers@trieve.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from trieve_py_client.models.event_types_one_of2 import EventTypesOneOf2

class TestEventTypesOneOf2(unittest.TestCase):
    """EventTypesOneOf2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EventTypesOneOf2:
        """Test EventTypesOneOf2
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EventTypesOneOf2`
        """
        model = EventTypesOneOf2()
        if include_optional:
            return EventTypesOneOf2(
                clicked_items = trieve_py_client.models.chunks_with_positions.ChunksWithPositions(
                    chunk_id = '', 
                    position = 56, ),
                event_name = '',
                event_type = 'click',
                is_conversion = True,
                request_id = '',
                user_id = ''
            )
        else:
            return EventTypesOneOf2(
                clicked_items = trieve_py_client.models.chunks_with_positions.ChunksWithPositions(
                    chunk_id = '', 
                    position = 56, ),
                event_name = '',
                event_type = 'click',
        )
        """

    def testEventTypesOneOf2(self):
        """Test EventTypesOneOf2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()