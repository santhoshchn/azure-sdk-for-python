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

try:
    from .provider_operation_py3 import ProviderOperation
    from .resource_type_py3 import ResourceType
    from .provider_operations_metadata_py3 import ProviderOperationsMetadata
    from .permission_py3 import Permission
    from .role_definition_filter_py3 import RoleDefinitionFilter
    from .role_definition_py3 import RoleDefinition
    from .role_assignment_filter_py3 import RoleAssignmentFilter
    from .role_assignment_py3 import RoleAssignment
    from .role_assignment_create_parameters_py3 import RoleAssignmentCreateParameters
except (SyntaxError, ImportError):
    from .provider_operation import ProviderOperation
    from .resource_type import ResourceType
    from .provider_operations_metadata import ProviderOperationsMetadata
    from .permission import Permission
    from .role_definition_filter import RoleDefinitionFilter
    from .role_definition import RoleDefinition
    from .role_assignment_filter import RoleAssignmentFilter
    from .role_assignment import RoleAssignment
    from .role_assignment_create_parameters import RoleAssignmentCreateParameters
from .provider_operations_metadata_paged import ProviderOperationsMetadataPaged
from .permission_paged import PermissionPaged
from .role_assignment_paged import RoleAssignmentPaged
from .role_definition_paged import RoleDefinitionPaged
from .authorization_management_client_enums import (
    PrincipalType,
)

__all__ = [
    'ProviderOperation',
    'ResourceType',
    'ProviderOperationsMetadata',
    'Permission',
    'RoleDefinitionFilter',
    'RoleDefinition',
    'RoleAssignmentFilter',
    'RoleAssignment',
    'RoleAssignmentCreateParameters',
    'ProviderOperationsMetadataPaged',
    'PermissionPaged',
    'RoleAssignmentPaged',
    'RoleDefinitionPaged',
    'PrincipalType',
]
