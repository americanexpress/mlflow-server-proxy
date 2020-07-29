# Copyright 2020 American Express Travel Related Services Company, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and limitations under
# the License.

"""
Simple tests for validating mlflow configs
"""
import os
import mlflow_server_proxy


def test_valid_title():
    args = mlflow_server_proxy.setup_mlflow()
    launcher_entry = args.get("launcher_entry")
    assert "MLFlow" in launcher_entry.get("title")


def test_invalid_title():
    args = mlflow_server_proxy.setup_mlflow()
    launcher_entry = args.get("launcher_entry")
    assert launcher_entry.get('title') != 'abcd'


def test_valid_timeout():
    args = mlflow_server_proxy.setup_mlflow()
    timeout = args.get("timeout")
    assert str(timeout) == '10'


def test_invalid_timeout():
    args = mlflow_server_proxy.setup_mlflow()
    timeout = args.get("timeout")
    assert str(timeout) != 'aedae'


def test_valid_icon_path():
    args = mlflow_server_proxy.setup_mlflow()
    launcher_entry = args.get("launcher_entry")
    actual_icon_path = launcher_entry.get("icon_path")
    expected_icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)).strip("/tests"),
                                      "icons", "mlflow.svg")
    assert expected_icon_path in actual_icon_path


def test_invalid_icon_path():
    args = mlflow_server_proxy.setup_mlflow()
    launcher_entry = args.get("launcher_entry")
    actual_icon_path = launcher_entry.get("icon_path")
    expected_icon_path = "/a/b/c"
    assert expected_icon_path != actual_icon_path


def test_valid_absurl():
    args = mlflow_server_proxy.setup_mlflow()
    absolute_url = args.get("absolute_url")
    assert absolute_url is False


def test_invalid_absurl():
    args = mlflow_server_proxy.setup_mlflow()
    absolute_url = args.get("absolute_url")
    assert absolute_url != "aedfa"
