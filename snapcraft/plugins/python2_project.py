# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
#
# Copyright (C) 2015 Canonical Ltd
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os

import snapcraft


class Python2ProjectPlugin(snapcraft.BasePlugin):

    # note that we don't need to setup env(), python figures it out
    # see python2.py for more details

    def pull(self):
        return self.handle_source_options()

    def build(self):
        env = os.environ.copy()
        env['PYTHONPATH'] = "{}/usr/lib/python2.7/dist-packages/".format(self.installdir)
        # Install will fail if PYTHONPATH does not exist
        os.makedirs(env['PYTHONPATH'])
        return self.run(
            ["python2", "setup.py", "install", "--install-layout=deb",
             "--prefix={}/usr".format(self.installdir)],
            env=env)
