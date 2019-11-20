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

def execute(pl, commandLine='', line='{preContent}{output}{err}{postContent}', preContent='', postContent='🤖', successCodes=None, failureCodes=None, *args, **kwargs):
    """
        Return a segment with the info (as output and or error) from command line execution.
        Args:
            pl (object): The powerline logger. 
            commandLine (string): The command line to execute, it can be complex (with pipes).
            line (string): The string to format the content of segment.
                Default value: {preContent}{output}{err}{postContent}
            preContent (string): The string to show before the result.
            postContent (string): The string to show after the result.
                Default value: 🤖
            successCodes list(int) or None: The values are success code return (normally 0), the background
                change to critical success. 
            failureCodes list(int) or None:  The values are fail code return, the background
                change to critical failture. 
        Returns:
            segment (list(dict)): The formated line with output of execution command line as powerline segment.
    """
    result = subprocess.run(commandLine, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    returncode = result.returncode
    output = result.stdout.decode('utf8').strip()
    err = result.stderr.decode('utf8').strip()
    
    color = ['information:regular']
    if isinstance(successCodes, list):
        if returncode in successCodes:
            color = ['critical:success']
    elif isinstance(failureCodes, list):
        if returncode in failureCodes:
            color = ['critical:failure']
    
    return [{
        'contents': line.format(preContent=preContent, output=output, err=err, postContent=postContent),
        'highlight_groups': color,
        'divider_highlight_group': None}]  
    
