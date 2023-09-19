from mininet.topo import Topo

class MyTopo( Topo ):
    def build( self ):
        pub1 = self.addSwitch('pub1')
        pub2 = self.addSwitch('pub2')

        s1 = self.addSwitch('s1')

        microtik = self.addHost('microtik', ip='192.168.1.1/24')
        h2 = self.addHost('h2', ip='192.168.1.10/24')
        h3 = self.addHost('h3', ip='192.168.1.20/24')

        self.addLink('microtik', 's1')
        self.addLink('h2', 's1')
        self.addLink('h3', 's1')

        s2 = self.addSwitch('s2')
        serverA = self.addHost('serverA', ip='100.64.10.10/23')
        serverB = self.addHost('serverB', ip='100.64.10.20/23')
        self.addLink('serverA', 'pub1')
        self.addLink('serverB', 'pub1')
        self.addLink('serverA', 's2', params1={'ip': '10.9.96.3/20'})
        self.addLink('serverB', 's2', params1={'ip': '10.9.96.4/20'})
        self.addLink('serverA', 'microtik', params1={'ip': '192.168.42.1/24'}, params2={'ip': '192.168.42.10/24'})

topos = { 'mytopo': ( lambda: MyTopo() ) }
