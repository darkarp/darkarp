from distutils.core import setup
setup(
    name='darkarp',
    packages=['darkarp', 'darkarp/malkit_modules'],
    version='2.1',
    license='MIT',
    description='Collection of modules by darkArp',
    author='Mario Nascimento',
    author_email='marionascimento@itsec.bz',
    url='https://github.com/darkarp',
    download_url='https://github.com/darkarp/darkarp/archive/v2.1.tar.gz',
    keywords=['darkarp', 'encryption', 'malkit'],
    install_requires=['pexe37'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
