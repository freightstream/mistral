# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
from oslo_policy import policy

from mistral.policies import base

EXECUTIONS = 'executions:%s'

rules = [
    policy.DocumentedRuleDefault(
        name=EXECUTIONS % 'create',
        check_str=base.RULE_ADMIN_OR_OWNER,
        description='Create a new execution.',
        operations=[
            {
                'path': '/v2/executions',
                'method': 'POST'
            }
        ]
    ),
    policy.DocumentedRuleDefault(
        name=EXECUTIONS % 'delete',
        check_str=base.RULE_ADMIN_OR_OWNER,
        description='Delete the specified execution.',
        operations=[
            {
                'path': '/v2/executions/{execution_id}',
                'method': 'DELETE'
            }
        ]
    ),
    policy.DocumentedRuleDefault(
        name=EXECUTIONS % 'get',
        check_str=base.RULE_ADMIN_OR_OWNER,
        description='Return the specified execution.',
        operations=[
            {
                'path': '/v2/executions/{execution_id}',
                'method': 'GET'
            }
        ]
    ),
    policy.DocumentedRuleDefault(
        name=EXECUTIONS % 'list',
        check_str=base.RULE_ADMIN_OR_OWNER,
        description='Return all executions.',
        operations=[
            {
                'path': '/v2/executions',
                'method': 'GET'
            }
        ]
    ),
    policy.DocumentedRuleDefault(
        name=EXECUTIONS % 'list:all_projects',
        check_str=base.RULE_ADMIN_ONLY,
        description='Return all executions from all projects.',
        operations=[
            {
                'path': '/v2/executions',
                'method': 'GET'
            }
        ]
    ),
    policy.DocumentedRuleDefault(
        name=EXECUTIONS % 'update',
        check_str=base.RULE_ADMIN_OR_OWNER,
        description='Update an execution.',
        operations=[
            {
                'path': '/v2/executions',
                'method': 'PUT'
            }
        ]
    )
]


def list_rules():
    return rules
