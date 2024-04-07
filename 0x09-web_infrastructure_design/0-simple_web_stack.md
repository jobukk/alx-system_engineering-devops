## Simple web stack

# specifics about this infrastructure
+ What is a server
	- refers to a piece of computer hardware or software that offers services to other computers, often known as clients.

+ What is the role of the domain name?
	- To give text-based labels—rather to the numerical addresses used in Internet protocols—to identify Internet resources, such as computers, networks, and services.It helps to locate website addresses using internet protocol. Domain names are simpler to remember compared to a string of number that make up IP addresses.
+ What type of DNS record www is in www.foobar.com?
	- A record . An A record maps a domain to the physical IP address of the computer hosting that domain. Internet traffic uses the A record to find the computer hosting your domain's DNS settings. . A hostname and its matching IPv4 address are stored in an Address Mapping record (A Record), commonly referred to as a DNS host record.
+ What is the role of the web server?
	- These servers host websites and web applications, delivering content to users who request it through their web browsers.
+ What is the role of the application server?
	-Application servers host and execute applications or software programs, providing the necessary computing resources for them to run.
+ What is the role of the database?
	- These servers store and manage databases, providing access to stored data and handling queries from clients.
+ What is the server using to communicate with the computer of the user requesting the website?
	-  TCP/IP protocol suite


# ISSUES WITH INFRASTRUCTURE

+ SPOF
	- A single point of failure(SPOF)is likely to occur as the infrastructure contains several SPOF.
+ Downtime when maintenance needed (like deploying new code web server needs to be restarted)
	- The server must be shut down or any component shut down when we need to do maintenance checks on it. There is just one server, thus there would be a downtime on the website.
+ Cannot scale if too much incoming traffic.
	- All the necessary components are on a single server with no backup