#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author  : mystic
# @date    : 12/18/2018 20:26
import socket

# create socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# build connection
soc.connect(('www.qq.com', 80))
