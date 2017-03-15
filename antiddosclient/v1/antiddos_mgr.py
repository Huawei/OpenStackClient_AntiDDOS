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
import re
import time

from antiddosclient.common import exceptions as execs
from antiddosclient.common import manager
from antiddosclient.common import utils
from antiddosclient.common.i18n import _
from antiddosclient.v1 import resource
from keystoneauth1 import exceptions

IP_PATTERN = re.compile(r'(\d{0,3}\.){1,3}(\d{0,3})$')


class AntiDDosManager(manager.Manager):
    resource_class = resource.AntiDDos

    def find(self, keyword):
        """find antiddos by keyword (UUID or IP)"""
        if not IP_PATTERN.match(keyword):
            try:
                # try keyword as UUID
                return self.get_antiddos(keyword)
            except exceptions.ClientException as e:
                pass
        else:
            # try keyword as IP
            results = self.list(ip=keyword)
            matched_number = len(results)
            if matched_number > 1:
                exactly_matched = [obj for obj in results
                                   if obj.floating_ip_address == keyword]
                if len(exactly_matched) == 1:
                    return exactly_matched[0]
                raise execs.NotUniqueMatch
            elif matched_number == 1:
                return results[0]

        message = _("AntiDDos with ID or IP '%s' not exists.") % keyword
        raise exceptions.NotFound(message)

    def query_config_list(self):
        """query antiddos config list"""
        return self._get("/antiddos/query_config_list",
                         resource_class=resource.AntiDDosConfig)

    def open_antiddos(
            self,
            floating_ip_id,
            enable_l7,
            traffic_pos_id,
            http_request_pos_id,
            cleaning_access_pos_id,
            app_type_id
    ):
        """Open AntiDDos"""
        data = utils.remove_empty_from_dict({
            "enable_L7": enable_l7,
            "traffic_pos_id": traffic_pos_id,
            "http_request_pos_id": http_request_pos_id if enable_l7 else None,
            "cleaning_access_pos_id": cleaning_access_pos_id,
            "app_type_id": app_type_id
        })
        return self._create("/antiddos/%s" % floating_ip_id,
                            data=data,
                            raw=True)

    def close_antiddos(self, floating_ip_id):
        """close AntiDDos"""
        return self._delete("/antiddos/%s" % floating_ip_id)

    def get_antiddos(self, floating_ip_id):
        """get anti DDos"""
        _antiddos = self._get("/antiddos/%s" % floating_ip_id)
        if isinstance(_antiddos, resource.AntiDDos):
            # server does not return floating ip id in response..
            _antiddos.floating_ip_id = floating_ip_id
        return _antiddos

    def update_antiddos(
            self,
            floating_ip_id,
            enable_l7,
            traffic_pos_id,
            http_request_pos_id,
            cleaning_access_pos_id,
            app_type_id
    ):
        """update anti DDos"""
        data = utils.remove_empty_from_dict({
            "enable_L7": enable_l7,
            "traffic_pos_id": traffic_pos_id,
            "http_request_pos_id": http_request_pos_id if enable_l7 else None,
            "cleaning_access_pos_id": cleaning_access_pos_id,
            "app_type_id": app_type_id
        })
        resource_url = "/antiddos/%s" % floating_ip_id
        return self._update_all(resource_url, data, raw=True)

    def list(self, status=None, ip=None, limit=None, offset=None):
        """list antiddos status of all EIP

        :param status:
            normal|configging|notConfig|packetcleaning|packetdropping
        :param ip: query for ip matches ".*ip.*"
        :param limit: max returned length
        :param offset: query offset
        :return:
        """
        params = utils.remove_empty_from_dict({
            "status": status,
            "ip": ip,
            "limit": limit,
            "offset": offset,
        })
        return self._list("/antiddos", params=params, key='ddosStatus')

    def get_task_status(self, task_id):
        """get anti-ddos task status"""
        url = "/query_task_status"
        return self._get(url,
                         params=dict(task_id=task_id),
                         resource_class=resource.AntiDDosTask)

    def get_antiddos_status(self, floating_ip_id):
        """get anti-ddos status of EIP"""
        url = "/antiddos/%s/status" % floating_ip_id
        return self._get(url, resource_class=resource.AntiDDosStatus)

    def get_antiddos_daily_report(self, floating_ip_id):
        """get past 24 hours antiddos protection report of the EIP

        report for every 5 minutes
        """
        url = "/antiddos/%s/daily" % floating_ip_id
        return self._list(url,
                          key="data",
                          resource_class=resource.AntiDDosDailyReport)

    def get_antiddos_daily_logs(self, floating_ip_id, sort_dir=None,
                                limit=None, offset=None):
        """get past 24 hours anti-ddos logs, delay is less than 5 minutes"""
        params = utils.remove_empty_from_dict({
            "sort_dir": sort_dir,
            "limit": limit,
            "offset": offset,
        })
        url = "/antiddos/%s/logs" % floating_ip_id
        return self._list(url,
                          key="logs",
                          params=params,
                          resource_class=resource.AntiDDosLog)

    def get_antiddos_weekly_report(self, period_start_date=None):
        """get weekly anti-ddos report for all EIP

        :param period_start_date: period start date (datetime)
        :return:
        """
        if period_start_date:
            epoch = time.mktime(period_start_date.timetuple())
            params = utils.remove_empty_from_dict({
                "period_start_date": int(epoch*1000)
            })
        else:
            params = {}
        url = "/antiddos/weekly"
        return self._get(url,
                         params=params,
                         resource_class=resource.AntiDDosWeeklyReport)
