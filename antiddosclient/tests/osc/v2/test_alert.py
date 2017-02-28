#   Copyright 2016 Huawei, Inc. All rights reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#
import mock

from antiddosclient.osc.v2 import alert
from antiddosclient.tests import base
from antiddosclient.v2 import alert_mgr
from antiddosclient.v2 import resource


class TestAntiDDosAlertConfigShow(base.AntiDDosV2BaseTestCase):
    def setUp(self):
        super(TestAntiDDosAlertConfigShow, self).setUp()
        self.cmd = alert.ShowAntiDDosAlertConfig(self.app, None)

    @mock.patch.object(alert_mgr.AlertManager, "_get")
    def test_show_alert_config(self, mocked_get):
        parsed_args = self.check_parser(self.cmd, [], ())
        config = {
            "warn_config": {
                "antiDDoS": True,
                "bruce_force": False,
                "remote_login": False,
                "weak_password": False,
                "high_privilege": False,
                "back_doors": False,
                "waf": False
            },
            "topic_urn": ("urn:smn:eu-de:67641fe6886f43fcb78edbbf0ad0b99f:"
                          "test_soft"),
            "display_name": "group_1",
        }

        mocked_get.return_value = resource.AlertConfig(None, config)
        columns, data = self.cmd.take_action(parsed_args)
        mocked_get.assert_called_once_with(
            "/warnalert/alertconfig/query",
        )
        self.assertEqual(columns, resource.AlertConfig.show_column_names)
        expected = (
            'urn:smn:eu-de:67641fe6886f43fcb78edbbf0ad0b99f:test_soft',
            'group_1',
            ("antiDDoS='True', back_doors='False', bruce_force='False', "
             "high_privilege='False', remote_login='False', waf='False', "
             "weak_password='False'"),
        )
        self.assertEqual(expected, data)
