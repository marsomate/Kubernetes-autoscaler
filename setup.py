from setuptools import setup, find_packages

setup(
    name='my_package',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        # Ide írd a szükséges csomagokat
    ],
    author='A Neved',
    author_email='a.neved@example.com',
    description='Egy rövid leírás a csomagról',
    url='https://github.com/username/repository',  # GitHub repository URL
)
