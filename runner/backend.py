'''
Autobahn examples using vanilla WAMP
'''

from os import environ
from twisted.internet.defer import inlineCallbacks
from twisted.internet import reactor

from autobahn.wamp.types import CallResult
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner


def callAdd(a, b):
    print 'Server called Add with ', a, b
    return a + b


def pub(a):
    print 'Server received a pub with ', a


def kill():
    print 'Quitting'
    reactor.stop()


class Component(ApplicationSession):

    """
    Application component that provides procedures which
    return complex results.
    """

    @inlineCallbacks
    def onJoin(self, details):
        print "session attached"

        yield self.register(callAdd, 'pd.damouse/add')
        yield self.register(kill, 'pd.damouse/kill')

        print 'Publishing to pd.pub'
        yield self.publish('pd/hello')

        yield self.subscribe(pub, 'pd.damouse/pub')

        print "procedures registered"


if __name__ == '__main__':
    runner = ApplicationRunner(
        "ws://127.0.0.1:8000/ws",
        # "ws://paradrop.io:9000/ws",
        u"pd.damouse",
        debug_wamp=False,  # optional; log many WAMP details
        debug=False,  # optional; log even more details
    )

    runner.run(Component)