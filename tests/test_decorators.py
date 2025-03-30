from datetime import datetime

import pytest

from src.decorators import log


def test_log(capsys):
    @log()
    def my_sum(a, b):
        return a / b

    time_s = datetime.now()
    my_sum(1, 2)
    captured = capsys.readouterr()
    time_f = datetime.now()
    assert (
        captured.out
        == time_s.strftime("[%Y-%m-%d %H:%M:%S]")
        + " Function my_sum started with inputs: ((1, 2), {})\n"
        + time_f.strftime("[%Y-%m-%d %H:%M:%S]")
        + " Function my_sum finished successfully with result: 0.5\n"
    )

    with pytest.raises(Exception):
        my_sum(1, 0)


def test_log_arg(capsys):
    @log("log.txt")
    def my_sum(a, b):
        return a / b

    my_sum(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "Written in the log file\n"

    with pytest.raises(Exception):
        my_sum(1, 0)
