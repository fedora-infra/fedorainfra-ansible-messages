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


class GitReceiveV1(message.Message):
    """
    Defines the message that is sent when an Ansible Playbook starts
    """

    @property
    def app_name(self):
        return "distgit"

    @property
    def app_icon(self):
        return "https://apps.fedoraproject.org/img/icons/git.png"

    @property
    def agent(self):
        try:
            return self.body["commit"]["agent"]
        except KeyError:
            return

    @property
    def agent_avatar(self):
        return user_avatar_url(self.agent)

    @property
    def usernames(self):
        return [self.agent]

    topic = "git.receive"

    body_schema = {
        "id": SCHEMA_URL + topic,
        "$schema": "http://json-schema.org/draft-04/schema#",
        "description": "Schema for messages sent when distgit gets a commit",
        "type": "object",
        "properties": {
            "commit": {
                "type": "object",
                "properties": {
                    "username": {"type": "string"},
                    "name": {"type": "string"},
                    "rev": {"type": "string"},
                    "namespace": {"type": "string"},
                    "agent": {"type": "string"},
                    "summary": {"type": "string"},
                    "repo": {"type": "string"},
                    "branch": {"type": "string"},
                    "seen": {"type": "boolean"},
                    "path": {"type": "string"},
                    "message": {"type": "string"},
                    "email": {"type": "string"},
                    "stats": {
                        "type": "object",
                        "properties": {
                            "files": {
                                "type": "object",
                                "patternProperties": {
                                    ".*": {
                                        "type": "object",
                                        "properties": {
                                            "additions": {"type": "integer"},
                                            "deletions": {"type": "integer"},
                                            "lines": {"type": "integer"},
                                        },
                                        "required": ["additions", "deletions", "lines"],
                                    }
                                },
                            },
                            "total": {
                                "type": "object",
                                "properties": {
                                    "additions": {"type": "integer"},
                                    "deletions": {"type": "integer"},
                                    "files": {"type": "integer"},
                                    "lines": {"type": "integer"},
                                },
                                "required": [
                                    "additions",
                                    "deletions",
                                    "files",
                                    "lines",
                                ],
                            },
                        },
                        "required": ["files", "total"],
                    },
                },
                "required": [
                    "branch",
                    "email",
                    "message",
                    "name",
                    "path",
                    "rev",
                    "stats",
                    "summary",
                    "username",
                    "agent",
                ],
            },
        },
        "required": ["commit"],
    }

    @property
    def summary(self):
        """Return a summary of the message."""
        commit = self.body["commit"]
        return (
            f"{commit['username']} pushed to {commit['repo']} ({commit['branch']}). "
            f"\"{commit['summary']}\""
        )
