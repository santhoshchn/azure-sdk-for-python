# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SourceUploadDefinition(Model):
    """The properties of a response to source upload request.

    :param upload_url: The URL where the client can upload the source.
    :type upload_url: str
    :param relative_path: The relative path to the source. This is used to
     submit the subsequent queue build request.
    :type relative_path: str
    """

    _attribute_map = {
        'upload_url': {'key': 'uploadUrl', 'type': 'str'},
        'relative_path': {'key': 'relativePath', 'type': 'str'},
    }

    def __init__(self, *, upload_url: str=None, relative_path: str=None, **kwargs) -> None:
        super(SourceUploadDefinition, self).__init__(**kwargs)
        self.upload_url = upload_url
        self.relative_path = relative_path
