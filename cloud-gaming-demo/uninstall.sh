#!/bin/bash -e
#
# Copyright 2022 Canonical Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

if [ "$(id -u)" -ne 0 ]; then
  echo "ERROR: please run this script as root"
  exit 1
fi

snap remove --purge cloud-gaming-demo
rm "/var/snap/anbox-cloud-appliance/common/traefik/conf/cloud-gaming-demo.yaml"

games="bombsquad mindustry"
for game in $games; do
  echo "Uninstalling $game..."
  sudo -u ubuntu amc application delete $game -y
done
