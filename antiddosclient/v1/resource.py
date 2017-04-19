#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
from osc_lib import utils as formatter

from antiddosclient.common import display
from antiddosclient.common import resource
from antiddosclient.common import utils
from antiddosclient.osc.v1.parser_builder import maximum_service_traffic
from antiddosclient.osc.v1.parser_builder import http_request_rate


class AntiDDos(resource.Resource, display.Display):
    """AntiDDos resource _antiddos."""

    status_list = [
        "normal",
        "configging",
        "notConfig",
        "packetcleaning",
        "packetdropping",
    ]

    list_column_names = (
        'floating IP id',
        'floating IP address',
        'network type',
        'status',
    )

    show_column_names = (
        'CC Defense',
        'maximum service traffic',
        'http request rate',
    )

    @property
    def cc_defense(self):
        return "Enabled" if self.enable_L7 else "Disabled"

    @property
    def maximum_service_traffic(self):
        return str(maximum_service_traffic[self.traffic_pos_id - 1]) + 'Mbit/s'

    @property
    def http_request_rate(self):
        return str(http_request_rate[self.http_request_pos_id - 1]) + '/s'


class AntiDDosTask(resource.Resource, display.Display):
    """AntiDDos task resource _antiddos."""

    show_column_names = (
        'Task Status',
        'Task Message',
    )

    list_column_names = (
        'Task Status',
        'Task Message',
    )

    @property
    def task_message(self):
        return self.task_msg


class AntiDDosStatus(resource.Resource, display.Display):
    """AntiDDos task resource _antiddos."""

    show_column_names = (
        'Status',
    )


class AntiDDosConfig(resource.Resource, display.Display):
    """AntiDDos configuration resource _antiddos."""

    show_column_names = [
        "Traffic limited list",
        "HTTP limited list",
        "Connection limited list"
    ]

    formatter = {
        "Traffic limited list": formatter.format_list_of_dicts,
        "HTTP limited list": formatter.format_list_of_dicts,
        "Connection limited list": formatter.format_list_of_dicts,
    }


class AntiDDosDailyReport(resource.Resource, display.Display):
    """AntiDDos report(every 5min) of past 24h"""

    list_column_names = (
        'Start Time',
        'BPS In',
        'BPS Attack',
        'BPS Total',
        'PPS In',
        'PPS Attack',
        'PPS Total',
    )

    @property
    def start_time(self):
        return utils.format_time(self.period_start / 1000)

    @property
    def bps_total(self):
        return self.total_bps

    @property
    def pps_total(self):
        return self.total_pps


class AntiDDosLog(resource.Resource, display.Display):
    """AntiDDos log for every five minutes."""

    list_column_names = (
        "Start Time",
        "End Time",
        "AntiDDos Status",
        "Trigger BPS",
        "Trigger PPS",
        "Trigger HTTP PPS",
    )

    formatter = {
        "Start Time": utils.format_time,
        "End Time": utils.format_time,
    }

    @property
    def antiddos_status(self):
        if self.status == 1:
            return 'Packet Cleaning'
        elif self.status == 2:
            return 'Packet Dropping'
        return ''


class AntiDDosWeeklyReport(resource.Resource, display.Display):
    """AntiDDos weekly summary report"""

    show_column_names = [
        "DDOS intercept times",
        "Weekly data",
        "top10"
    ]

    formatter = {
        # "weekdata": formatter.format_list_of_dicts,
        "top10": formatter.format_list_of_dicts,
    }

    @property
    def weekly_data(self):
        if self.weekdata:
            for data in self.weekdata:
                time_long = data["period_start_date"]
                data["period_start_date"] = utils.format_time(time_long)
        return formatter.format_list_of_dicts(self.weekdata)
