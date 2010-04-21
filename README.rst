cron.d buildout recipe
======================

This package provides buildout_ recipes for the configuration of cron jobs.
It creates files that are suitable for use in /etc/cron.d.

We use the system cron, so this recipe will not install cron for you.  If
you wish to install cron, use `zc.recipe.cmmi`_ perhaps.

.. _buildout: http://pypi.python.org/pypi/zc.buildout
.. _`zc.recipe.cmmi`: http://pypi.python.org/pypi/zc.recipe.cmmi


Mandatory Parameters
--------------------

command
    The command to run from cron. Cron can't handle multi-line commands, so \n will become ' '.
script
    Instead of command you can provide a script inline that will be saved to disk and run in the cronjob.
user
    The account to run the command under
location
    Where to write the cron entry to


Time Parameters
---------------

at
    One of 'reboot', 'yearly', 'monthly', 'weekly', 'daily', 'midnight' or 'hourly'
minute
    Any integer from 0 to 59
hour
    Any integer from 0 to 23
day
    Any integer from 1 to 31 (must be a valid day if a month is specified)
month
    Any integer from 1 to 12, or the short name of the month such as 'jan'
day-of-week
    Any integer from 0 to 7 (where 0 and 7 are Sunday), or a short name such as 'mon'

You must specify at least one of the above. You can use normal `cron`_ notation here too.

.. _`cron`: http://www.redhat.com/docs/manuals/linux/RHL-7.2-Manual/custom-guide/cron-task.html


Optional Parameters
-------------------

environment-vars
    Prepare the environment that your cron job will run under, for example setting PYTHONPATH
comments
    Any comments made will be prefixed with '#' and included in the generated files.


Repository
----------

This software is available from our `recipe repository`_ on github.

.. _`recipe repository`: http://github.com/isotoma/recipes


License
-------

Copyright 2010 Isotoma Limited

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


