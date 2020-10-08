import re
import sys

DATETIME_REG_EX = r'\d{2}:\d{2}:\d{2}\.\d{3}'
NUMBERING_REG_EX = r'^[0-9]+'
SPEAKER_REG_EX = r'^[a-zA-Z].*[\s\.]*\: '
HEADER_LINE = r'WEBVTT'

def _clean_transcript_file(transcript_string):
        ZOOM_DATETIME_REG_EX = r'\d{2}:\d{2}:\d{2}\.\d{3}'
        ZOOM_NUMBERING_REG_EX = r'^(\d+|\s+)$'
        ZOOM_SPEAKER_REG_EX = r'^([a-zA-Z]).*[\s\.]*\:\s'
        ZOOM_HEADER_LINE = r'WEBVTT'

        formatted_lines = []

        last_speaker = None

        transcript_lines = transcript_string.split('\n')

        for line in transcript_lines:
            line = line.strip()
            current_speaker = last_speaker
            line_includes_speaker = re.match(ZOOM_SPEAKER_REG_EX, line)

            if line_includes_speaker:
                current_speaker = line_includes_speaker.group(0)

            line_is_number = re.match(ZOOM_NUMBERING_REG_EX, line)
            line_is_header = re.match(ZOOM_HEADER_LINE, line)
            line_is_timestamp = re.match(ZOOM_DATETIME_REG_EX, line)
            line_is_empty = re.match(r'^\s*$', line)

            if not (line_is_header or line_is_number or line_is_timestamp or line_is_empty):
                if line_is_number:
                    continue

                if (last_speaker is not None and current_speaker == last_speaker):
                    formatted_lines[-1] = (formatted_lines[-1] + line.strip().replace(current_speaker, ' '))
                else:
                    formatted_lines.append(line.strip())
                    last_speaker = current_speaker

            if last_speaker is None and current_speaker is not None:
                last_speaker = current_speaker

        return formatted_lines

def generate_plain_formatted_transcript(raw_transcript_content):
    clean_transcript = _clean_transcript_file(raw_transcript_content)
    return '\n\n'.join(clean_transcript)


'''
def clean_transcript_file(input_filename, output_filename):
    updated_transcript_contents = ''

    with open(input_filename, 'r') as transcript_file:
        last_speaker = None

        for line in transcript_file:
            current_speaker = last_speaker
            line_includes_speaker = re.match(SPEAKER_REG_EX, line)

            if line_includes_speaker:
                current_speaker = line_includes_speaker.group(0)

            line_is_number = re.match(NUMBERING_REG_EX, line)
            line_is_header = re.match(HEADER_LINE, line)
            line_is_timestamp = re.match(DATETIME_REG_EX, line)
            line_is_empty = re.match(r'\n', line)

            if not (line_is_header or line_is_number or line_is_timestamp or line_is_empty):
                if line_is_number:
                    continue

                if (last_speaker is not None and current_speaker == last_speaker):
                    updated_transcript_contents += line.replace(current_speaker, '')
                else:
                    updated_transcript_contents += '\n'
                    updated_transcript_contents += line
                    last_speaker = current_speaker

            if last_speaker is None and current_speaker is not None:
                last_speaker = current_speaker
    
        with open(output_filename, 'w') as output_file:
            output_file.write(updated_transcript_contents)
'''


args = sys.argv

if len(args) > 2:
    input_filename = args[1]
    output_filename = args[2]

    with open(input_filename, 'r') as transcript_input:
        result = generate_plain_formatted_transcript(transcript_input.read())

        with open(output_filename, 'w') as transcript_output:
            transcript_output.write(result)

