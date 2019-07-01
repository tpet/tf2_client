# tf2_client
Configurable tf2 client wrapper switching between local and remote buffer.

## Usage
```python
rospy.init_node('awesome_node')
buffer = tf2_client.get_buffer()
buffer.lookup_transform(target_frame, source_frame, time)
```

## Parameters 
- For remote buffer (parameters of `tf2_ros.BufferClient`):
    - `~tf2/ns`, defaults to `None`
    - `~tf2/check_frequency`, `None`
    - `~tf2/timeout_padding`, `2.0`
- For local buffer (parameters of `tf2_ros.Buffer` and `tf2_ros.TransformListener`):
    - `~tf2/cache_time`, `10.0`
    - `~tf2/queue_size`, `None`
    - `~tf2/buff_size`, `65536`

Remote buffer is used if parameter `~tf2/ns` is specified.
