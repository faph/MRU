# -*- coding: utf-8 -*-

# The MIT License (MIT)
#
# Copyright (c) 2015 Florenz A. P. Hollebrandse
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
__all__ = ['MRU']

from collections import deque
from collections.abc import Iterable
import appdirs
import os
import os.path


class MRU(deque):
    """Most Recently Used (MRU) file paths collection"""

    FILE_NAME = 'mru'

    def __init__(self, app, org=None, maxlen=20):
        self.app = app
        self.org = org
        self.file_path = os.path.join(appdirs.user_config_dir(app, org), self.FILE_NAME)
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)  # create folder in advance
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = [line.rstrip('\n') for line in f]
        except OSError:
            data = []
        deque.__init__(self, data, maxlen=maxlen)

    def save(action):
        def saved_action(self, *args, **kwargs):
            action(self, *args, **kwargs)
            with open(self.file_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(self) + '\n')
        return saved_action

    @save
    def add(self, paths):
        if isinstance(paths, str):
            self.appendleft(paths)
        elif isinstance(paths, Iterable):
            self.extendleft(paths)
        else:
            raise TypeError("Argument `paths` must be string or iterable.")

    @save
    def clear(self):
        deque.clear(self)
