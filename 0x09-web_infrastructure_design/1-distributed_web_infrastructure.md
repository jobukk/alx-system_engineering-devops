## 1. Distributed web infrastructure

#specifics about this infrastructure

- Round Robin algorithm distribution. he queries requested are distributed to every server sequentially one after another.
  Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both - Active-Active set up.
  How a database Primary-Replica (Master-Slave) cluster works - A primary-replica (also known as master-slave) database cluster is a setup where multiple copies of a database exist, with one designated as the primary or master node and the others acting as replicas or slave nodes. This setup provides several benefits, including improved performance, high availability, and data redundancy.
  What is the difference between the Primary node and the Replica node in regard to the application? - Primary Node: The primary node is the main database server responsible for handling read and write operations. All write operations, such as INSERT, UPDATE, and DELETE queries, are directed to this primary node. It maintains the authoritative copy of the data .
  Replica Nodes: Replica nodes, also called slave nodes, are copies of the primary database. These nodes receive replicated copies of data from the primary node and are typically used for read operations, such as SELECT queries. They serve to distribute read queries, reducing the load on the primary node and improving performance.

# Issues are with this infrastructure<br/>

-Single Point of Failure (SPOF):<br/>

Without redundancy or failover mechanisms, any critical component that fails could potentially lead to system-wide downtime.<br/>
Potential SPOFs might include:<br/>
Single server hosting the database, web server, and application server.<br/>
Lack of redundancy in network infrastructure such as switches or routers.<br/>
Single internet connection without backup or failover.<br/>

-Security Issues:<br/>

- Lack of firewall: Without a firewall, the system is vulnerable to unauthorized access, malicious attacks, and data breaches. A firewall helps in controlling inbound and outbound traffic and provides an additional layer of security.<br/>
  No HTTPS: Transmitting sensitive data over HTTP exposes it to interception and manipulation by malicious actors. HTTPS encrypts data in transit, ensuring confidentiality and integrity.<br/>
  Absence of security measures increases the risk of various security threats such as unauthorized access, data breaches, DDoS attacks, and malware infections.<br/>

-No Monitoring:

Without monitoring, it's challenging to detect and respond to performance issues, security breaches, or infrastructure failures promptly.<br/>
Lack of monitoring means there's no insight into resource utilization, system health, or potential security incidents.<br/>
Monitoring is essential for proactive maintenance, capacity planning, and ensuring service availability and reliability.<br/>

-To address these issues, the infrastructure should be improved by implementing measures such as:<br/>
Introducing redundancy and failover mechanisms to eliminate SPOFs.<br/>
Deploying a firewall to control and secure network traffic.<br/>
Enabling HTTPS to encrypt data in transit and enhance security.<br/>
Implementing comprehensive monitoring solutions to track system performance, security events, and overall health.<br/>
Regularly updating and patching systems to address security vulnerabilities.<br/>
Implementing best practices for securing databases, web servers, and applications.<br/>
Establishing incident response procedures to address security breaches or system failures promptly.<br/>
