import os
import pytest


@pytest.fixture(scope='module')
def valid_output():
    valid_output_file = os.path.join('tests', 'data', 'valid_result.vtt')
    with open(valid_output_file, 'r') as valid_output:
        content = valid_output.read()
        return content


@pytest.fixture(scope='module')
def exec_clean_transcript():
    """
    creating test file by running test_clean_transcript.py with 'sample' and 'test1.vtt' args
    :return: whole file as string
    """
    input_file = os.path.join('sample', 'test1.vtt')
    output_file = os.path.join('tests', 'output', 'generated_test_file.vtt')
    os.system(f'python clean_transcript.py {input_file} {output_file}')
    with open(output_file, 'r') as output:
        content = output.read()
        yield content
    os.remove(output_file)


def test_compare_expected_script_output_vs_actual_script_output(valid_output, exec_clean_transcript):
    assert valid_output == exec_clean_transcript
