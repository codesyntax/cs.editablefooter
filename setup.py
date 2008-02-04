from setuptools import setup, find_packages

version = '0.2'

setup(name='cs.editablefooter',
      version=version,
      description="A simple package providing a editable footer for Plone",
      long_description="""\
""",
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone plone3 viewlet footer',
      author='Mikel Larreategi',
      author_email='mlarreategi@codesyntax.com',
      url='http://code.codesyntax.com/private/cs.editablefooter',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['cs'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'plone.browserlayer',
          'plone.app.form',
          'plone.app.controlpanel',
          'plone.app.layout',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
