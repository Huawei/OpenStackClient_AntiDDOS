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
import logging

from osc_lib.command import command

from antiddosclient.common.i18n import _
from antiddosclient.v2 import resource

LOG = logging.getLogger(__name__)


class ShowAntiDDosAlertConfig(command.ShowOne):
    _description = _("Show AntiDDos alert config details")

    def get_parser(self, prog_name):
        parser = super(ShowAntiDDosAlertConfig, self).get_parser(prog_name)
        return parser

    def take_action(self, args):
        mgr = self.app.client_manager.antiddos.alerts
        alert_config = mgr.get()
        columns = resource.AlertConfig.show_column_names
        formatter = resource.AlertConfig.formatter
        output = alert_config.get_display_data(columns, formatter=formatter)
        return columns, output
