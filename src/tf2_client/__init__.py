from __future__ import absolute_import, division, print_function
import rospy
from tf2_ros import Buffer, TransformListener, BufferClient
from threading import Lock

__all__ = ['get_buffer']

_lock = Lock()
_buffer = None
_listener = None


def get_buffer():
    global _buffer, _listener, _lock
    with _lock:
        if _buffer is None:
            # remote
            ns = rospy.get_param('~tf2/ns', None)
            check_frequency = rospy.get_param('~tf2/check_frequency', None)
            timeout_padding = rospy.Duration(rospy.get_param('~tf2/timeout_padding', 2.0))
            # local
            cache_time = rospy.Duration(rospy.get_param('~tf2/cache_time', 10.0))
            queue_size = rospy.get_param('~tf2/queue_size', None)
            buff_size = rospy.get_param('~tf2/buff_size', 65536)
            if ns:
                _buffer = BufferClient(ns, check_frequency, timeout_padding)
            else:
                _buffer = Buffer(cache_time)
                _listener = TransformListener(_buffer, queue_size, buff_size)

        return _buffer
