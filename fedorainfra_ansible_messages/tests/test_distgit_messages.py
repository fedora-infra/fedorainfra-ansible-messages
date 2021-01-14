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

from ..distgit_messages import GitReceiveV1

DUMMY_GIT_RECEIVE = {
    "commit": {
        "username": "dudemcpants",
        "stats": {
            "files": {"kernel.spec": {"deletions": 1, "additions": 0, "lines": 1}},
            "total": {"deletions": 1, "files": 1, "additions": 0, "lines": 1},
        },
        "name": "Dude McPants",
        "rev": "7471f555f01eae34dcf5527f7fa1ad99f7f15ed4",
        "namespace": "rpms",
        "agent": "dudemcpants",
        "summary": "Add some Stuff",
        "repo": "kernel",
        "branch": "f35",
        "seen": False,
        "path": "/srv/git/repositories/rpms/kernel.git",
        "message": "Add some Stuff\n",
        "email": "dudemcpants@email.test",
    }
}


def test_distgit_messages_properties():
    """Assert DistGit Messages properties are correct."""

    message = GitReceiveV1(body=DUMMY_GIT_RECEIVE)

    assert message.app_name == "distgit"
    assert message.app_icon == "https://apps.fedoraproject.org/img/icons/git.png"
    assert message.agent == "dudemcpants"
    assert message.agent_avatar == (
        "https://seccdn.libravatar.org/avatar/"
        "caa750edf4a11206831a58713cf9231b5b3227765887cbc765d4f8c5c55576a5"
        "?s=64&d=retro"
    )
    assert message.usernames == ["dudemcpants"]


def test_git_receive_v1():
    """
    Assert the message schema validates a message with the required fields.
    """
    message = GitReceiveV1(body=DUMMY_GIT_RECEIVE)
    message.validate()


def test_git_receive_v1_invalid():
    """
    Assert the message schema doenst validate with an incorrect body.
    """
    message = GitReceiveV1(body={})
    with pytest.raises(ValidationError):
        message.validate()


def test_git_receive_v1_summary():
    """Assert the summary is correct."""
    expected_summary = 'dudemcpants pushed to kernel (f35). "Add some Stuff"'
    message = GitReceiveV1(body=DUMMY_GIT_RECEIVE)
    assert expected_summary == message.summary
