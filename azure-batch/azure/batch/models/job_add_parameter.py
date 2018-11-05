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


class JobAddParameter(Model):
    """An Azure Batch job to add.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. A string that uniquely identifies the job within the
     account. The ID can contain any combination of alphanumeric characters
     including hyphens and underscores, and cannot contain more than 64
     characters. The ID is case-preserving and case-insensitive (that is, you
     may not have two IDs within an account that differ only by case).
    :type id: str
    :param display_name: The display name for the job. The display name need
     not be unique and can contain any Unicode characters up to a maximum
     length of 1024.
    :type display_name: str
    :param priority: The priority of the job. Priority values can range from
     -1000 to 1000, with -1000 being the lowest priority and 1000 being the
     highest priority. The default value is 0.
    :type priority: int
    :param constraints: The execution constraints for the job.
    :type constraints: ~azure.batch.models.JobConstraints
    :param job_manager_task: Details of a Job Manager task to be launched when
     the job is started. If the job does not specify a Job Manager task, the
     user must explicitly add tasks to the job. If the job does specify a Job
     Manager task, the Batch service creates the Job Manager task when the job
     is created, and will try to schedule the Job Manager task before
     scheduling other tasks in the job. The Job Manager task's typical purpose
     is to control and/or monitor job execution, for example by deciding what
     additional tasks to run, determining when the work is complete, etc.
     (However, a Job Manager task is not restricted to these activities - it is
     a fully-fledged task in the system and perform whatever actions are
     required for the job.) For example, a Job Manager task might download a
     file specified as a parameter, analyze the contents of that file and
     submit additional tasks based on those contents.
    :type job_manager_task: ~azure.batch.models.JobManagerTask
    :param job_preparation_task: The Job Preparation task. If a job has a Job
     Preparation task, the Batch service will run the Job Preparation task on a
     compute node before starting any tasks of that job on that compute node.
    :type job_preparation_task: ~azure.batch.models.JobPreparationTask
    :param job_release_task: The Job Release task. A Job Release task cannot
     be specified without also specifying a Job Preparation task for the job.
     The Batch service runs the Job Release task on the compute nodes that have
     run the Job Preparation task. The primary purpose of the Job Release task
     is to undo changes to compute nodes made by the Job Preparation task.
     Example activities include deleting local files, or shutting down services
     that were started as part of job preparation.
    :type job_release_task: ~azure.batch.models.JobReleaseTask
    :param common_environment_settings: The list of common environment
     variable settings. These environment variables are set for all tasks in
     the job (including the Job Manager, Job Preparation and Job Release
     tasks). Individual tasks can override an environment setting specified
     here by specifying the same setting name with a different value.
    :type common_environment_settings:
     list[~azure.batch.models.EnvironmentSetting]
    :param pool_info: Required. The pool on which the Batch service runs the
     job's tasks.
    :type pool_info: ~azure.batch.models.PoolInformation
    :param on_all_tasks_complete: The action the Batch service should take
     when all tasks in the job are in the completed state. Note that if a job
     contains no tasks, then all tasks are considered complete. This option is
     therefore most commonly used with a Job Manager task; if you want to use
     automatic job termination without a Job Manager, you should initially set
     onAllTasksComplete to noaction and update the job properties to set
     onAllTasksComplete to terminatejob once you have finished adding tasks.
     The default is noaction. Possible values include: 'noAction',
     'terminateJob'
    :type on_all_tasks_complete: str or ~azure.batch.models.OnAllTasksComplete
    :param on_task_failure: The action the Batch service should take when any
     task in the job fails. A task is considered to have failed if has a
     failureInfo. A failureInfo is set if the task completes with a non-zero
     exit code after exhausting its retry count, or if there was an error
     starting the task, for example due to a resource file download error. The
     default is noaction. Possible values include: 'noAction',
     'performExitOptionsJobAction'
    :type on_task_failure: str or ~azure.batch.models.OnTaskFailure
    :param metadata: A list of name-value pairs associated with the job as
     metadata. The Batch service does not assign any meaning to metadata; it is
     solely for the use of user code.
    :type metadata: list[~azure.batch.models.MetadataItem]
    :param uses_task_dependencies: Whether tasks in the job can define
     dependencies on each other. The default is false.
    :type uses_task_dependencies: bool
    """

    _validation = {
        'id': {'required': True},
        'pool_info': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'priority': {'key': 'priority', 'type': 'int'},
        'constraints': {'key': 'constraints', 'type': 'JobConstraints'},
        'job_manager_task': {'key': 'jobManagerTask', 'type': 'JobManagerTask'},
        'job_preparation_task': {'key': 'jobPreparationTask', 'type': 'JobPreparationTask'},
        'job_release_task': {'key': 'jobReleaseTask', 'type': 'JobReleaseTask'},
        'common_environment_settings': {'key': 'commonEnvironmentSettings', 'type': '[EnvironmentSetting]'},
        'pool_info': {'key': 'poolInfo', 'type': 'PoolInformation'},
        'on_all_tasks_complete': {'key': 'onAllTasksComplete', 'type': 'OnAllTasksComplete'},
        'on_task_failure': {'key': 'onTaskFailure', 'type': 'OnTaskFailure'},
        'metadata': {'key': 'metadata', 'type': '[MetadataItem]'},
        'uses_task_dependencies': {'key': 'usesTaskDependencies', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(JobAddParameter, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.display_name = kwargs.get('display_name', None)
        self.priority = kwargs.get('priority', None)
        self.constraints = kwargs.get('constraints', None)
        self.job_manager_task = kwargs.get('job_manager_task', None)
        self.job_preparation_task = kwargs.get('job_preparation_task', None)
        self.job_release_task = kwargs.get('job_release_task', None)
        self.common_environment_settings = kwargs.get('common_environment_settings', None)
        self.pool_info = kwargs.get('pool_info', None)
        self.on_all_tasks_complete = kwargs.get('on_all_tasks_complete', None)
        self.on_task_failure = kwargs.get('on_task_failure', None)
        self.metadata = kwargs.get('metadata', None)
        self.uses_task_dependencies = kwargs.get('uses_task_dependencies', None)
