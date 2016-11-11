#!/usr/bin/env bash

python run.py --test &

sleep 1

py.test -v -s --driver PhantomJS tests/selenium
exit_code=$?

pkill -9 -f run.py && exit ${exit_code}
