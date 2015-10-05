import unittest
import mru
import os
import appdirs
import tempfile
from unittest.mock import MagicMock


class TestMRU(unittest.TestCase):
    APP = 'testapp'
    ORG = 'testorg'

    @classmethod
    def setUpClass(cls):
        cls.temp_folder = tempfile.TemporaryDirectory()
        print("Testing in folder {.name}.".format(cls.temp_folder))
        appdirs.user_config_dir = MagicMock(return_value=cls.temp_folder.name)

    def tearDown(self):
        try:
            os.remove(os.path.join(self.temp_folder.name, mru.MRU.FILE_NAME))
        except FileNotFoundError:
            pass

    @classmethod
    def tearDownClass(cls):
        cls.temp_folder.cleanup()

    def test_add_one(self):
        m = mru.MRU(self.APP, self.ORG)
        m.add('a')
        self.assertEqual(m[0], 'a')

    def test_add_one_by_one(self):
        m = mru.MRU(self.APP, self.ORG)
        m.add('a')
        m.add('b')
        self.assertEqual(m[0], 'b')
        self.assertEqual(m[1], 'a')

    def test_add_multiple(self):
        m = mru.MRU(self.APP, self.ORG)
        m.add(['a', 'b'])
        self.assertEqual(m[0], 'b')
        self.assertEqual(m[1], 'a')

    def test_add_invalid(self):
        """Only pass str or iterable to m.add()"""
        m = mru.MRU(self.APP, self.ORG)
        with self.assertRaises(TypeError):
            m.add(object)

    def test_maxlen(self):
        m = mru.MRU(self.APP, self.ORG, maxlen=2)
        m.add(['a', 'b', 'c'])
        self.assertEqual(list(m), ['c', 'b'])

    def test_clear(self):
        m = mru.MRU(self.APP, self.ORG)
        m.add('a')
        m.clear()
        self.assertEqual(list(m), [])

    def test_persist(self):
        m = mru.MRU(self.APP, self.ORG)
        m.add('a')
        m2 = mru.MRU(self.APP, self.ORG)
        self.assertEqual(list(m2), ['a'])
