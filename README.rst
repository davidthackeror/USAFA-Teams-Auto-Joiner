=============
Teams AutoJoin
=============

This repository seeks to create an AutoJoin Teams feature to facilitate the scheduling of classes during CoronaBreak.


.. image:: https://cdn.shopify.com/s/files/1/0246/4622/1903/products/itscoronatime-display_1200x1200.png?v=1583900078
  :align: right

=============
BEFORE RUNNING
=============

Users must edit the python script in any text editor and add their username and password underneath the comments at the beginning of the script. This is hardcoded so that the user can run the script without user input on launch. Edits should also be made to match the URL of the naviagted to classroom with their own, as it is currently unknown if class URL's are universal or distinct for each user.

Additionally users should follow the instructions at the following link to ensure they install Selenium

https://selenium-python.readthedocs.io/installation.html

=============
How It Works
=============

The software uses selenium to run the python script, which can generate a Firefox headless broweser and execute commands passed into it. Right now running the python script will launch a Firefox browser and navigate through the login screens usually presented to the user. Upon reaching the splash page of Teams, it can naviagte to A selected teams site to wait for a specified amount of time.

=============
Things Still To Do
=============


+----------------------------------------+
| Description                            |
+========================================+
| List and navigate to multiple classes  |
+----------------------------------------+
| Time triggered execution               |
+----------------------------------------+
| Password hiding                        |
+----------------------------------------+
| Text Support                           |
+----------------------------------------+
