from setuptools import setup, find_packages


def get_requirements(file_path):
    """Reads the installation requirements from requirements.txt"""
    with open(file_path) as reqfile:
        reqs = filter(lambda line: not line.startswith(('#', '-')), reqfile.read().split("\n"))
        return list(reqs)

setup(
    name = 'twitter-news-bot',
    version = '0.1',
    author = 'Eric Connelly',
    description = 'A Twitter Bot to tweet about curated news content',
    url = 'https://github.com/econne01/twitter-news-bot',
    install_requires=get_requirements("requirements.txt"),
    packages = find_packages(),
)
