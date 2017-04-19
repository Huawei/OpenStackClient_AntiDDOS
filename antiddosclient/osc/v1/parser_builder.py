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
from antiddosclient.common.i18n import _


# traffic maximum
maximum_service_traffic = [10, 30, 50, 70, 100, 150, 200, 250, 300]

# http request rate
http_request_rate = [100, 150, 240, 350, 480, 550, 700, 850, 1000, 1500, 2000,
                     3000, 5000, 10000, 20000]


class AntiDDosParser(object):

    @staticmethod
    def add_floating_ip_arg(parser):
        parser.add_argument(
            'floating_ip',
            metavar='<floating ip>',
            help=_("For floating ip (UUID or IP)")
        )

    @staticmethod
    def add_enable_l7_arg(parser):
        enable_group = parser.add_mutually_exclusive_group()
        enable_group.add_argument(
            '--enable-CC',
            action="store_true",
            dest='enable_l7',
            default=True,
            help=_("Enable CC Defence protection (default)")
        )
        enable_group.add_argument(
            '--disable-CC',
            action="store_false",
            dest='enable_l7',
            help=_("Disable CC Defence protection")
        )

    @staticmethod
    def add_maximum_service_traffic_arg(parser):
        parser.add_argument(
            '--maximum-service-traffic',
            required=True,
            choices=maximum_service_traffic,
            type=int,
            help=_("Maximum service traffic (Mbit/s)")
        )

    @staticmethod
    def get_traffic_pos_id(traffic):
        if traffic:
            return maximum_service_traffic.index(int(traffic)) + 1
        else:
            return None

    @staticmethod
    def add_http_request_rate_arg(parser):
        parser.add_argument(
            '--http-request-rate',
            required=False,
            choices=http_request_rate,
            type=int,
            help=_("HTTP request rate (per second), "
                   "only effect when L7 is enabled")
        )

    @staticmethod
    def get_http_request_pos_id(rate):
        if rate:
            return http_request_rate.index(int(rate)) + 1
        else:
            return None

    # @staticmethod
    # def add_cleaning_access_pos_arg(parser):
    #     parser.add_argument(
    #         '--cleaning-access-pos',
    #         required=True,
    #         choices=utils.str_range(1, 9),
    #         help=_("cleaning access pos, integer between 1-8")
    #     )
    #
    # @staticmethod
    # def add_app_type_arg(parser):
    #     parser.add_argument(
    #         '--app-type',
    #         required=True,
    #         choices=('0', '1'),
    #         help=_("app type, 0 or 1")
    #     )
