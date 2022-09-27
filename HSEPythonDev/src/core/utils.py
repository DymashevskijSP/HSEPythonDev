import datetime

from dateutil import parser
from django.core.exceptions import BadRequest


def parse_time(time_string):
    return parser.parse(time_string)


def check_meeting_times(start, end):
    if end <= start:
        raise BadRequest('meeting should begins earlier than ends')
    current_time = datetime.datetime.now()
    if end <= current_time:
        raise BadRequest('meeting can\'t be created in this time')