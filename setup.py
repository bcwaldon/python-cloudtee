
import distutils.core

distutils.core.setup(
    name="cloudtee",
    version="0.0.3",
    url="http://cloudtee.me",
    author="Brian Waldon",
    author_email="bcwaldon@gmail.com",
    packages=['cloudtee'],
    scripts=["bin/cloudtee"],
)
