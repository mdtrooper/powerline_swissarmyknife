#!/usr/bin/env python3
# 
# slotmachine_oneline.py
# Copyright (C) 2019  Miguel de Dios Matias
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import subprocess

def execute(pl, commandLine='', line='{preContent}{output}{err}{postContent}', successCodes=None, failureCode=None, preContent='', postContent='🧰', *args, **kwargs):
    result = subprocess.run(commandLine, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    returncode = result.returncode
    output = result.stdout.decode('utf8')
    err = result.stderr.decode('utf8')
    
    color = ['information:regular']
    if isinstance(successCodes, list):
        if returncode in successCodes:
            color = ['critical:success']
    elif isinstance(failureCode, list):
        if returncode in failureCode:
            color = ['critical:failure']
    
    return [{
        'contents': line.format(preContent=preContent, output=output, err=err, postContent=postContent),
        'highlight_groups': color,
        'divider_highlight_group': None}]  
    
