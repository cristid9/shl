class TrafficRule:

    def __init__(self):
        self._cidr_block = None
        self._port_range_start = None
        self._port_range_end = None
        self._protocol = None

    @property
    def cidr_block(self):
        return self._cidr_block

    @cidr_block.setter
    def cidr_block(self, value):
        self._cidr_block = value

    @property
    def port_range_start(self):
        return self._port_range_start

    @port_range_start.setter
    def port_range_start(self, value):
        self._port_range_start = value
    
    @property
    def port_range_end(self):
        return self._port_range_end

    @port_range_end.setter
    def port_range_end(self, value):
        self._port_range_end = value

    @property
    def protocol(self):
        return self._protocol    
    
    @protocol.setter
    def protocol(self, value):
        self._protocol = value