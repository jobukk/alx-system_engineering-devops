## Secured and monitored web infrastructure

# Specifics about this infrastructure:

- What are firewalls for:<br/> Firewalls are for securing the network by filtering and analysis the traffic and data packets that request entry to the network based on configured rules.

- Why is the traffic served over HTTPS:<br/> HTTPS has an SSL certificate which aid in encrypting personal information transferred between the private network and public network. <br/> Prevent hackers from accessing/modify any personal information in network traffic.

- What monitoring is used for:<br/> Monitoring clients monitors the servers and external network. They track, collect, analyze performance, alert incase of failure in network device and takes reports on variety of data from a network device (loadbalancer, servers):

- How the monitoring tool is collecting data:<br/>The monitoring tool observes the servers and loadbalancer and provides key metrics about the servers' operations and the loadbalancer operations to the administrators. It automatically tests the accessibility of the loadbalancer and servers, measures response time, and alerts for errors such as corrupt/missing files, security vulnerabilities/violations, and many other issues

- Explain what to do if you want to monitor your web server QPS:<br/> Select a monitoring tool, Install and configure the monitoring tool to the webserver, Setup the QPS metrics include; active connections, response times etc and setup notification and reports generation on the monitoring tool, Setup visualization metrics to display the QPS metrics in real-time then Analyze and optimize to identify the perfomance bottlenecks.

# Issues are with this infrastructure:

- Why terminating SSL at the load balancer level is an issue:<br/> Terminating SSL at Loadbalancer leads to unencryprion of traffic and information can be easily accessed and modified by anyone with access.

- Why having only one MySQL server capable of accepting writes is an issue:<br/> Because it acts as single point failure for the web infrastructure.

- Why having servers with all the same components (database, web server and application server) might be a problem:<br/>
  -They will be a difficult in scaling it up.<br/>
  -Single Point of Failure it there's a problem with one component or server it will affect the entire system.<br/>
  -Resource Imbalance.Example database server may need more disk I/O, memory, and CPU resources compared to a web server.<br/>-Having identical servers means resources might be underutilized for some components and overutilized for others.
