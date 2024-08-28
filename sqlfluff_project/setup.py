from setuptools import setup, find_packages

setup(
    name="sqlfluff_project",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[],
    entry_points={
        'console_scripts': [
            'lint-sql=module.script:main',
        ],
    },
)
