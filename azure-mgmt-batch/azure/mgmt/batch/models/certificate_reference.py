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


class CertificateReference(Model):
    """A reference to a certificate to be installed on compute nodes in a pool.
    This must exist inside the same account as the pool.

    :param id: The fully qualified ID of the certificate to install on the
     pool. This must be inside the same batch account as the pool.
    :type id: str
    :param store_location: The location of the certificate store on the
     compute node into which to install the certificate. The default value is
     currentUser. This property is applicable only for pools configured with
     Windows nodes (that is, created with cloudServiceConfiguration, or with
     virtualMachineConfiguration using a Windows image reference). For Linux
     compute nodes, the certificates are stored in a directory inside the task
     working directory and an environment variable AZ_BATCH_CERTIFICATES_DIR is
     supplied to the task to query for this location. For certificates with
     visibility of 'remoteUser', a 'certs' directory is created in the user's
     home directory (e.g., /home/{user-name}/certs) and certificates are placed
     in that directory. Possible values include: 'CurrentUser', 'LocalMachine'
    :type store_location: str or
     ~azure.mgmt.batch.models.CertificateStoreLocation
    :param store_name: The name of the certificate store on the compute node
     into which to install the certificate. This property is applicable only
     for pools configured with Windows nodes (that is, created with
     cloudServiceConfiguration, or with virtualMachineConfiguration using a
     Windows image reference). Common store names include: My, Root, CA, Trust,
     Disallowed, TrustedPeople, TrustedPublisher, AuthRoot, AddressBook, but
     any custom store name can also be used. The default value is My.
    :type store_name: str
    :param visibility: Which user accounts on the compute node should have
     access to the private data of the certificate. Values are:
     starttask - The user account under which the start task is run.
     task - The accounts under which job tasks are run.
     remoteuser - The accounts under which users remotely access the node.
     You can specify more than one visibility in this collection. The default
     is all accounts.
    :type visibility: list[str or
     ~azure.mgmt.batch.models.CertificateVisibility]
    """

    _validation = {
        'id': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'store_location': {'key': 'storeLocation', 'type': 'CertificateStoreLocation'},
        'store_name': {'key': 'storeName', 'type': 'str'},
        'visibility': {'key': 'visibility', 'type': '[CertificateVisibility]'},
    }

    def __init__(self, id, store_location=None, store_name=None, visibility=None):
        self.id = id
        self.store_location = store_location
        self.store_name = store_name
        self.visibility = visibility
