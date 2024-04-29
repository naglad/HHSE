# settings.py
TEMPLATES = [
    {
        ...
        'OPTIONS': {
            'context_processors': [
                ...
                'your_app_name.sidebar_context_processor.sidebar_context',
            ],
        },
    },
]