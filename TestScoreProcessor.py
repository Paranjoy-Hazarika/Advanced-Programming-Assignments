import pytest
import os
from ScoreProcessor import ScoreProcessor

@pytest.fixture
def processor():
    """Provide a fresh ScoreProcessor instance for every test."""
    return ScoreProcessor()


@pytest.fixture
def valid_score_file(tmp_path):
    """Create a temporary file containing a valid integer score."""
    file = tmp_path / "score.txt"
    file.write_text("42")
    return str(file)


@pytest.fixture
def invalid_score_file(tmp_path):
    """Create a temporary file containing non-numeric data."""
    file = tmp_path / "bad_score.txt"
    file.write_text("abc")
    return str(file)

class TestSuccessfulCalculation:

    def test_score_is_multiplied_by_ten(self, processor, valid_score_file):
        result = processor.process_score_file(valid_score_file)
        assert result == 420

    def test_score_zero_returns_zero(self, processor, tmp_path):
        f = tmp_path / "zero.txt"
        f.write_text("0")
        assert processor.process_score_file(str(f)) == 0

    def test_score_with_whitespace_is_handled(self, processor, tmp_path):
        f = tmp_path / "padded.txt"
        f.write_text("  7  \n")
        assert processor.process_score_file(str(f)) == 70

class TestErrorHandling:

    def test_raises_file_not_found_for_missing_file(self, processor):
        with pytest.raises(FileNotFoundError):
            processor.process_score_file("nonexistent_file.txt")

    def test_raises_value_error_for_non_numeric_content(self, processor, invalid_score_file):
        with pytest.raises(ValueError):
            processor.process_score_file(invalid_score_file)

    def test_raises_value_error_for_float_string(self, processor, tmp_path):
        f = tmp_path / "float.txt"
        f.write_text("3.14")
        with pytest.raises(ValueError):
            processor.process_score_file(str(f))