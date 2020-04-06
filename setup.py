from setuptools import setup

config = {
    'include_package_data': True,
    'description': 'Bot for doing initial avalon card assignments',
    'download_url': 'https://github.com/AvantiShri/avalon-bot',
    'version': '0.1.0.0',
    'packages': ['avalonbot'],
    'setup_requires': [],
    'install_requires': [], #I believe I only use the standard library
    'dependency_links': [],
    'scripts': ['run_avalon_bot'],
    'name': 'avalonbot'
}

if __name__== '__main__':
    setup(**config)