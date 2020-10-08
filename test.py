import os
import unittest


class TestScript(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_file_1 = os.path.join('sample', 'test1.vtt')

    def test_input_file_exists(self):
        fake_filepath = os.path.join('sample', 'thisisnotarealfile.vtt')

        self.assertTrue(os.path.exists(self.test_file_1))
        self.assertFalse(os.path.exists(fake_filepath))
    
    def test_script_outputs_nothing_if_no_input_file(self):
        files_before_exec = [f for f in os.listdir('.') if os.path.isfile(f)]
        self.assertEqual(len(files_before_exec), 5)
        os.system('python clean_transcript.py {}'.format(self.test_file_1))
        self.assertEqual(len(files_before_exec), 5)


if __name__ == '__main__':
    unittest.main()
