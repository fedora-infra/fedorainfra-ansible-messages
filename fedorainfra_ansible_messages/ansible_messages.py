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

from fedora_messaging import message
from fedora_messaging.schema_utils import user_avatar_url


SCHEMA_URL = "http://fedoraproject.org/message-schema/"


class ansibleMessage(message.Message):
    """
    A sub-class of a Fedora message that defines a message schema for messages
    published by the Fedora Infrastructure Ansible.
    """

    @property
    def app_name(self):
        return "ansible"

    @property
    def app_icon(self):
        return "https://apps.fedoraproject.org/img/icons/ansible.png"

    @property
    def agent(self):
        return self.body.get("userid")

    @property
    def agent_avatar(self):
        return user_avatar_url(self.agent)

    @property
    def usernames(self):
        return [self.agent]


class AnsiblePlaybookStartV1(ansibleMessage):
    """
    Defines the message that is sent when an Ansible Playbook starts
    """

    topic = "ansible.playbook.start"

    body_schema = {
        "id": SCHEMA_URL + topic,
        "$schema": "http://json-schema.org/draft-04/schema#",
        "description": "Schema for messages sent when an Ansible playbook starts",
        "type": "object",
        "properties": {
            "userid": {"type": "string"},
            "playbook_checksum": {"type": "string"},
            "extra_vars": {"type": "object"},
            "playbook": {"type": "string"},
            "check": {"type": "boolean"},
            "inventory": {"type": "array"},
        },
        "required": ["userid", "playbook_checksum", "playbook"],
    }

    @property
    def summary(self):
        """Return a summary of the message."""
        return (
            f"{self.body['userid']} started an ansible run of {self.body['playbook']}"
        )


class AnsiblePlaybookCompleteV1(ansibleMessage):
    """
    Defines the message that is sent when an Ansible Playbook completes
    """

    topic = "ansible.playbook.complete"

    body_schema = {
        "id": SCHEMA_URL + topic,
        "$schema": "http://json-schema.org/draft-04/schema#",
        "description": "Schema for messages sent when an Ansible playbook completes",
        "type": "object",
        "properties": {
            "userid": {"type": "string"},
            "playbook": {"type": "string"},
            "results": {"type": "object"},
        },
        "required": ["userid", "playbook"],
    }

    @property
    def summary(self):
        """Return a summary of the message."""
        return f"{self.body['userid']}'s {self.body['playbook']} playbook run completed"
