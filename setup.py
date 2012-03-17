
import distutils.core

import cloudtee


distutils.core.setup(
    name='cloudtee',
    version=cloudtee.__version__,
    url='http://cloudtee.me',
    author='Brian Waldon',
    author_email='bcwaldon@gmail.com',
    packages=['cloudtee'],
    scripts=['bin/cloudtee', 'bin/cloudtail'],
)
