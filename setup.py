from setuptools import setup

config = {
    'include_package_data': True,
    'description': 'To help with playing Avalon over zoom. Requires owning board game.',
    'download_url': 'https://github.com/AvantiShri/avalonbot',
    'version': '0.1.0.0',
    'packages': ['avalonbot'],
    'package_data': {},
    'setup_requires': [],
    'install_requires': ['random', 'argparse', 'email', 'smtplib', 'json'],
    'dependency_links': [],
    'scripts': ['scripts/avalonbot'],
    'name': 'avalonbot'
}

if __name__== '__main__':
    setup(**config)
