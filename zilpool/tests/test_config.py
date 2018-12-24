# -*- coding: utf-8 -*-
# Zilliqa Mining Pool
# Copyright  @ 2018-2019 Gully Chen
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from zilpool.common.utils import merge_config

cur_dir = os.path.dirname(os.path.abspath(__file__))


def get_config(conf):
    conf_file = os.path.join(cur_dir, conf)
    return merge_config(conf_file)


def get_database_debug_config():
    return get_config("database/debug.conf")


def get_pool_config():
    return get_config("../../../pool.conf")


def get_default_config():
    return get_config("../default.conf")