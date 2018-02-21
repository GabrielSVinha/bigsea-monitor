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

import logging
import time


class Log:

    def __init__(self, name, output_file_path):
        self.logger = logging.getLogger(name)
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        self.logger.addHandler(handler)
        handler = logging.FileHandler(output_file_path)
        self.logger.addHandler(handler)

    def log(self, text):
        self.logger.info(text)

class TableLog:
    def __init__(self, name, output_file_path):
        self.logger = Log(name, output_file_path)
        self.table = texttable.Texttable()
        self.table.set_cols_align(["c", "c", "c", 'c', 'c', 'c'])
        self.table.set_cols_width([8, 24, 15, 15, 15, 26])
        
    def log(self, app_id, job_progress, time_progress, progress_error, action):
#       line = "%s %s %s %s %s %s %s" % (timestamp, app_id, job_progress, time_progress, previous_cap, current_cap, action)
        timestamp = time.strftime("%H:%M:%S")

        if job_progress != '--':
            job_progress_formatted = str(float("{0:.1f}".format(float(job_progress)))) + "%"
        else:
            job_progress_formatted = job_progress

        if time_progress != '--':
            time_progress_formatted = str(float("{0:.1}".format(float(time_progress)))) + "%"
        else:
            time_progress_formatted = time_progress

        if previous_cap != '--':
            previous_cap_formatted = str(previous_cap) + "%"
        else:
            previous_cap_formatted = previous_cap

        if current_cap != '--':
            current_cap_formatted = str(current_cap) + "%"
        else:
            current_cap_formatted = current_cap

        line = [timestamp, app_id, job_progress_formatted, time_progress_formatted, progress_error_formatted, action]
        self.table.add_row(line)
        last_line = self.table.draw().split('\n')[-2]
        self.logger.log(last_line)

    def header_log(self):
        header_row = [["Time", "Application ID", "Job Progress", "Time Progress", "Progress Error", 'Action']]
        self.table.add_rows(header_row)
        last_line = self.table.draw().split('\n')[:3]
        self.logger.log(last_line[0])
        self.logger.log(last_line[1])
        self.logger.log(last_line[2])

def configure_logging():
    logging.basicConfig(level=logging.DEBUG)
