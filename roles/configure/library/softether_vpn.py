#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import requests

def run_module():
    module_args = dict(
        command=dict(type='str', required=True),
        name=dict(type='str', required=False),
        hub=dict(type='str', required=False),
        users=dict(type='list', elements='str', required=False)
    )

    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    command = module.params['command']
    name = module.params.get('name')
    hub = module.params.get('hub')
    users = module.params.get('users')

    if command == 'CreateHub':
        if not name:
            module.fail_json(msg="name is required for CreateHub")
        # Implement CreateHub logic using requests to interact with the SoftEther API
        result['changed'] = True
        result['message'] = f"Hub {name} created"

    elif command == 'CreateUser':
        if not hub or not users:
            module.fail_json(msg="hub and users are required for CreateUser")
        # Implement CreateUser logic using requests to interact with the SoftEther API
        result['changed'] = True
        result['message'] = f"Users {', '.join(users)} created in hub {hub}"

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
