get_root = {
    'type': 'object',
    'required': [
        'name', 'version', 'license',
        'organization', 'headquater'
    ],
    'properties': {
        'name': {'type': 'string'},
        'version': {
            'type': 'string',
            'pattern': '^[0-9]+\.[0-9]+\.[0-9]+$'
        },
        'license': {'type': 'string'},
        'organization': {'type': 'string'},
        'headquater': {'type': 'string'}
    }
}
