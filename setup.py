from setuptools import find_packages, setup

with open('requirements.txt', encoding='utf-8') as f:
    requirements = f.read()

setup(
    name="systemq",
    version='5.5.0',
    author="baqis",
    author_email="baqis@baqis.ac.com",
    url="https://gitee.com/",
    license = "MIT",
    keywords="experiment laboratory",
    description="control, measure and visualization",
    long_description='long_description',
    long_description_content_type='text/markdown',
    packages = find_packages(),
    include_package_data = True,
    install_requires=requirements,
    python_requires='>=3.9.0',
    classifiers=[
        'Development Status :: 5 - Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering :: Physics',
    ],
    project_urls={
        'source': 'https://gitee.com',
    },
)
