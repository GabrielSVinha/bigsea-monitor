# Copyright (c) 2017 UFCG-LSD.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from monitor.service import api
from monitor.plugins.spark_sahara.plugin import SparkProgress
from monitor.plugins.spark_mesos.plugin import SparkProgressUPV
from monitor.plugins.web_app.plugin import WebAppMonitor
from monitor.plugins.openstack_generic.plugin import OSGeneric


class MonitorBuilder:
    def __init__(self):
        pass

    def get_monitor(self, plugin, app_id, plugin_info):
        executor = None
        if plugin == "spark_sahara":
            executor = SparkProgress(app_id, plugin_info, api.retries)

        elif plugin == "web_app":
            executor = WebAppMonitor(app_id, plugin_info, api.os_keypair,
                                     api.retries)

        elif plugin == "openstack_generic":
            executor = OSGeneric(app_id, plugin_info, api.os_keypair,
                                 api.retries)

        elif plugin == "spark_mesos":
            executor = SparkProgressUPV(app_id, plugin_info, api.retries)
       
        else:
            raise ex.BadRequestException()

        return executor
