# Copyright (C) 2020  Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""Unit tests for the ansible_messages"""

import pytest

from jsonschema import ValidationError

from ..ansible_messages import AnsiblePlaybookStartV1, AnsiblePlaybookCompleteV1

DUMMY_ANSIBLE_START = {
    "playbook_checksum": "4b5eff15ef85a2424024fc963c25fde4809c1fa1",
    "extra_vars": {},
    "userid": "dudemcpants",
    "playbook": "playbooks/update_ticketkey.yml",
    "check": False,
    "inventory": ["/srv/web/infra/ansible/inventory"],
}

DUMMY_ANSIBLE_COMPLETE = {
    "userid": "dudemcpants",
    "playbook": "playbooks/update_ticketkey.yml",
    "results": {
        "proxy30.fedoraproject.org": {
            "ignored": 0,
            "skipped": 0,
            "ok": 2,
            "rescued": 0,
            "changed": 2,
            "unreachable": 0,
            "failures": 0,
        }
    },
}


def test_ansible_messages_properties():
    """Assert Ansible Messages properties are correct."""

    message = AnsiblePlaybookStartV1(body=DUMMY_ANSIBLE_START)

    assert message.app_name == "ansible"
    assert message.app_icon == "https://apps.fedoraproject.org/img/icons/ansible.png"
    assert message.agent == "dudemcpants"
    assert message.agent_avatar == (
        "https://seccdn.libravatar.org/avatar/"
        "caa750edf4a11206831a58713cf9231b5b3227765887cbc765d4f8c5c55576a5"
        "?s=64&d=retro"
    )
    assert message.usernames == ["dudemcpants"]


def test_playbook_start_v1():
    """
    Assert the message schema validates a message with the required fields.
    """
    message = AnsiblePlaybookStartV1(body=DUMMY_ANSIBLE_START)
    message.validate()


def test_playbook_start_v1_invalid():
    """
    Assert the message schema doenst validate with an incorrect body.
    """
    message = AnsiblePlaybookStartV1(body={})
    with pytest.raises(ValidationError):
        message.validate()


def test_playbook_start_v1_summary():
    """Assert the summary is correct."""
    expected_summary = (
        "dudemcpants started an ansible run of playbooks/update_ticketkey.yml"
    )
    message = AnsiblePlaybookStartV1(body=DUMMY_ANSIBLE_START)
    assert expected_summary == message.summary


def test_playbook_complete_v1():
    """
    Assert the message schema validates a message with the required fields.
    """
    message = AnsiblePlaybookCompleteV1(body=DUMMY_ANSIBLE_COMPLETE)
    message.validate()


def test_playbook_complete_v1_invalid():
    """
    Assert the message schema doenst validate with an incorrect body.
    """
    message = AnsiblePlaybookCompleteV1(body={})
    with pytest.raises(ValidationError):
        message.validate()


def test_playbook_complete_v1_summary():
    """Assert the summary is correct."""
    expected_summary = (
        "dudemcpants's playbooks/update_ticketkey.yml playbook run completed"
    )
    message = AnsiblePlaybookCompleteV1(body=DUMMY_ANSIBLE_COMPLETE)
    assert expected_summary == message.summary
