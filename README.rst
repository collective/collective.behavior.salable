===========================
collective.behavior.salable
===========================

collective.behavior.salable provides behavior to switch dexterity content types salable.

Currently tested with
---------------------

* Plone-4.3.2 [taito]

Behavior
--------

The behavior can be added through the web or directly through the file system to the dexterity content type xml file like::

  <property name="behaviors">
    ...
    <element value="collective.behavior.salable.interfaces.ISalable" />
    ...
  </property>
