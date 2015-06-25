===========================
collective.behavior.salable
===========================

collective.behavior.salable provides behavior to switch dexterity content types salable.

.. image:: https://secure.travis-ci.org/collective/collective.behavior.salable.png
    :target: http://travis-ci.org/collective/collective.behavior.salable

Currently tested with
---------------------

* Plone-4.3.6 with Python-2.7.x [taito]

Behavior
--------

The behavior can be added through the web or directly through the file system to the dexterity content type xml file like::

  <property name="behaviors">
    ...
    <element value="collective.behavior.salable.interfaces.ISalable" />
    ...
  </property>
