from setuptools import setup, find_packages

package_name = "pip-project"
package_version = "1.0.0"

setup(
    name=package_name,
    version=package_version,
    author="some author",
    install_requires=["requests", "numpy", "Django==1.9.6", "sosreport", "Zope2==2.12.0"],
    entry_points={
        'console_scripts': [
            'pip-project=Main:main'
        ]
    }
)
