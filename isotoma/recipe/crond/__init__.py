# Copyright 2010 Isotoma Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

class Cron(object):

    def __init__(self, buildout, name, options):
        self.name = name
        self.options = options
        self.buildout = buildout

        self.options.setdefault("minute", "*")
        self.options.setdefault("hour", "*")
        self.options.setdefault("day-of-month", "*")
        self.options.setdefault("month", "*")
        self.options.setdefault("day-of-week", "*")

        if not self.options.get("user"):
            raise ValueError("You must specify a user to run the command as")

        if not self.options.get("location"):
            raise ValueError("You must specify where to write this cron rule to")

        flag = True
        for o in ("minute", "hour", "day-of-month", "month", "day-of-week"):
            if self.options.get(o) != "*":
                flag = False

        if flag:
            raise ValueError("You must set one of 'minute', 'hour', 'day-of-month', 'month' or 'day-of-week'")

    def install(self):
        dir, file = os.path.split(self.options['location'])
        if not os.path.isdir(dir):
            os.makedirs(dir)

        file = open(self.options['location'], 'w')

        # Can specify optional "comments" for any ops user looking in cron.d
        comments = self.options.get("comments", "").split("\n")
        if comments:
            for comment in comments:
                if not comment:
                    continue
                file.write("# %s\n" % comment)
            file.write("\n")

        # Users can specify environment variables
        vars = self.options.get("environment-vars", "").split("\n")
        if vars:
            for var in vars:
                if not var:
                    continue
                kv = var.split()
                file.write("%s=%s\n" % tuple(kv))
            file.write("\n")

        rule = "%(minute)s %(hour)s %(day-of-month)s %(month)s %(day-of-week)s %(user)s %(command)s\n"
        file.write(rule % self.options)

        file.close()

        return [self.options['location']]

    def update(self):
        pass

