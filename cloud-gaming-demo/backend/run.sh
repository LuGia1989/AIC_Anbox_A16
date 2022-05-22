#!/bin/bash -ex
#
# Copyright 2021 Canonical Ltd.
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

if [ ! -e venv ] ; then
    virtualenv venv
fi

. ./venv/bin/activate
pip install -r requirements.txt

EXTRA_ARGS=

if [ -e "$PWD"/tls/app.crt ] && [ -e "$PWD"/tls/app.key ]; then
    EXTRA_ARGS="$EXTRA_ARGS --keyfile $PWD/tls/app.key --certfile $PWD/tls/app.crt"
    EXTRA_ARGS="$EXTRA_ARGS --ssl-version=TLSv1_2"
fi

exec talisker.gunicorn.gevent \
    --chdir "$PWD" \
    --bind "0.0.0.0:8002" \
    --worker-class gevent \
    $EXTRA_ARGS \
    service.service:app
