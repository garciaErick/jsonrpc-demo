#!/bin/bash

pkill python

python jserver.py &
python jclient.py

