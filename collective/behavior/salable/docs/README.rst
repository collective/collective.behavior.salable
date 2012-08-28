===========================
collective.behavior.salable
===========================

collective.behavior.salable provides behavior to switch dexterity content types salable and not.

Currently tested with
---------------------

* Plone-4.2.1 [taito]

Behavior
--------

The behavior can be added through the web or directly through the file system to the dexterity content type xml file like::

  <property name="behaviors">
    ...
    <element value="collective.behavior.salable.interfaces.ISalable" />
    ...
  </property>


Farther Documentation URL
-------------------------

`http://packages.python.org/collective.behavior.salable/
<http://packages.python.org/collective.behavior.salable/>`_

Repository URL
--------------

`https://github.com/collective/collective.behavior.salable/
<https://github.com/collective/collective.behavior.salable/>`_
