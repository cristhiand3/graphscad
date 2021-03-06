# coding: utf8
from __future__ import unicode_literals

import core as cdc


class Node_vectordiv(cdc.Dagnode):

    def getcomment(self):
        return 'this node divide each component of a vector by a value'

    def getdisplaytype(self):
        return 'math'

    def getinputplugs(self):
        return [
            {'name': 'a', 'value': '[0,0,0]', 'type': 'vector'},
            {'name': 'b', 'value': '1', 'type': 'str'}
            ]

    def getoutputplugs(self):
        return [
            {'name': 'vector', 'value': '[0,0,0]', 'type': 'vector'}
            ]

    def evaluate(self):
        a=self.getinputplugvalue('a')
        b=self.getinputplugvalue('b')
        self.setoutputplugvalue('vector','vectordiv('+a+','+b+')')
        return
