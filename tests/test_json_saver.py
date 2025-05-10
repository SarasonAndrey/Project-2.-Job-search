import json
import os
from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, mock_open, patch

from src.json_saver import BASEDIR, JsonSaver


def test_json_saver_init(json_saver_init: JsonSaver, file_path: str = "data") -> None:
    assert json_saver_init.file_path == Path(BASEDIR / "data" / file_path)


def test_json_saver_init_with_argument() -> None:
    file_path = "test"
    json_instance = JsonSaver(file_path)
    assert json_instance.file_path == Path(BASEDIR / "data" / file_path)


def test_get_data_from_file(json_saver_init: JsonSaver) -> None:
    mock_data = [{"name": "Python Developer"}]
    mock_json_data = json.dumps(mock_data)
    with patch("builtins.open", mock_open(read_data=mock_json_data)):
        result = json_saver_init.get_data_from_file()
        assert result == [{"name": "Python Developer"}]


def test_get_data_from_file_empty(json_saver_init: JsonSaver) -> None:
    mock_data = None
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = json_saver_init.get_data_from_file()
        assert result == []


@patch("builtins.open", side_effect=FileNotFoundError)
def test_get_data_from_file_found_error(
    mock_built: MagicMock, json_saver_init: JsonSaver
) -> None:
    result = json_saver_init.get_data_from_file()
    assert result == []


def test_add_data_to_file(vacancy_dict: dict) -> None:
    json_saver = JsonSaver("test")
    json_saver.add_data_to_file(vacancy_dict)
    assert json_saver.get_data_from_file() == [{"name": "Python Developer"}]
    f_path = f"{json_saver.file_path}.json"
    if os.path.exists(f_path):
        os.remove(f_path)


def test_add_data_to_file_copy(vacancy_dict: dict) -> None:
    json_saver = JsonSaver("test")
    json_saver.add_data_to_file(vacancy_dict)
    json_saver.add_data_to_file(vacancy_dict)
    assert json_saver.get_data_from_file() == [{"name": "Python Developer"}]
    f_path = f"{json_saver.file_path}.json"
    if os.path.exists(f_path):
        os.remove(f_path)
    else:
        os.truncate(f_path, 0)


def test_delete_data_from_file(vacancy_dict: dict) -> None:
    json_saver = JsonSaver("test")
    json_saver.add_data_to_file(vacancy_dict)
    json_saver.delete_data_from_file(vacancy_dict)
    assert json_saver.get_data_from_file() == []
    f_path = f"{json_saver.file_path}.json"
    if os.path.exists(f_path):
        os.remove(f_path)


def test_delete_data_from_file_value_error(capsys: Any, vacancy_dict: dict) -> None:
    vacancy_ins_del = {"name": "Python"}
    json_saver = JsonSaver("test")
    json_saver.add_data_to_file(vacancy_dict)
    json_saver.delete_data_from_file(vacancy_ins_del)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Данные не найдены"
    f_path = f"{json_saver.file_path}.json"
    if os.path.exists(f_path):
        os.remove(f_path)
