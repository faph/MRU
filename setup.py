from setuptools import setup
import versioneer

setup(
    name='mru',
    packages=['mru'],
    zip_safe=False,
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass()
)
