Postmortem

Issue Summary:

	On Monday, July 20th, cedi-mart was down for most of the Ghana working day. This affected transactions on the website as users could not make orders or track their orders. I have described the event in detail below.

	If you’re familiar with cedi-mart at all you know that we live and breathe ecommerce. For a long time I’ve had the stance that testing software before deployment is the right way to go. A an enginx file path was wrongly configured the extension was phpp instead of php. The problem caused a major outage of the hosted cedi-mart service earlier this week.

Timeline:
	On that faithful day of our SRE's shipped an update to production and after few minutes the web application went down. A customer complain later until then we were oblivious of the situation.
	Through minutes of debuging, we later found out the issue. Since it was a frontend issue we checked only the frontend. We initially thought it was a number of things turned out it was a bug in the front end application code. Though it took some sweat. The incident was quickly escalated to my team. We reconfigured the nginx to use the proper configs.

Root cause and resolution:
	Nginx was being used to serve the web frontend application and to achieve this it needed to be configured to tell it to do so since it can also be configured to do other stuff like load balancing and as proxy server just to mention few. The configuration to use it as a webserver went wrong. The server configuration has a portion were it request for the directory path of the files to serve and the path contained the wrong extension file name. After detecting the root cause we manage to fix it through a reconfiguration with the right file path.

Corrective and preventative measures:
	In order to avoid the future occurence of this we have put several measures in place. Some of these measures include reviews to ensure anything deployed has been verified and tested. Also, monitors will be added to check the nginx server.
