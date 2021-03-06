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

"""
Class that define a MonascaConnector simulation.
"""
class MockMonascaConnector():

    """ Constructor of the mock of a MonascaConnector object
    
    Returns:
        MockRedis: The simulation of a redis object
    """
    def __init__(self):

        self.metrics = {}

    """
    Simulate the behavior of send_metrics function
    Monasca Connector api.
    Args:
        metrics(Objects): Object that must be send to monasca.
    """
    def send_metrics(self, metrics):

        try:
            self.metrics[metrics[0]['name']].append(metrics)

        except Exception as ex:

            self.metrics[metrics[0]['name']] = []
            self.metrics[metrics[0]['name']].append(metrics)
