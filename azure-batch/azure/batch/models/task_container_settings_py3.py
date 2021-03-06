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


class TaskContainerSettings(Model):
    """The container settings for a task.

    All required parameters must be populated in order to send to Azure.

    :param container_run_options: Additional options to the container create
     command. These additional options are supplied as arguments to the "docker
     create" command, in addition to those controlled by the Batch Service.
    :type container_run_options: str
    :param image_name: Required. The image to use to create the container in
     which the task will run. This is the full image reference, as would be
     specified to "docker pull". If no tag is provided as part of the image
     name, the tag ":latest" is used as a default.
    :type image_name: str
    :param registry: The private registry which contains the container image.
     This setting can be omitted if was already provided at pool creation.
    :type registry: ~azure.batch.models.ContainerRegistry
    """

    _validation = {
        'image_name': {'required': True},
    }

    _attribute_map = {
        'container_run_options': {'key': 'containerRunOptions', 'type': 'str'},
        'image_name': {'key': 'imageName', 'type': 'str'},
        'registry': {'key': 'registry', 'type': 'ContainerRegistry'},
    }

    def __init__(self, *, image_name: str, container_run_options: str=None, registry=None, **kwargs) -> None:
        super(TaskContainerSettings, self).__init__(**kwargs)
        self.container_run_options = container_run_options
        self.image_name = image_name
        self.registry = registry
