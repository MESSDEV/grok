"""
We cannot register two skins under the same name::

  >>> grok.testing.grok(__name__)
  Traceback (most recent call last):
    ...
  ConfigurationConflictError: Conflicting configuration actions
    For: ('utility', <InterfaceClass zope.publisher.interfaces.browser.IBrowserSkinType>, 'foo')
"""

import grok

class Skin1(grok.Skin):
    grok.name('foo')

class Skin2(grok.Skin):
    grok.name('foo')
