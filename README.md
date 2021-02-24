# HomeInternetFilter
Redirect users of your computer away from selected sites and instead have the user land on other sites which you prefer.

#Explanation of hosts file
How this works is TYPE IN THE WEBSITE NAME THAT **YOU WANT BYPASSED**, and type in BEFORE it 
  the IP address of the desired "go to instead of" website (look it up with dnslookup or website)

 157.140.2.32 - This is the IP address for http://scratchpads.org
132.148.209.175  - This is really elithecomputerguy.com's Public IP Address. 

# Important technicality
Editting the host file while it is in its proper location RENDERS ANY CHANGES INEFFECTUAL.
The file needs to be changed in a different folder and THEN COPIED TO IT'S PROPER LOCATION.


#The following would be working entries in the host file 
#Desired dst      Undesired dst 
157.140.2.32 elithecomputerguy.com
132.148.209.175 nerleelef.com
68.183.248.146 nerleelef.com


This works for HTTP sites

Acknowledgements: 
      - Great site: https://charlesr.co.uk/how-to-get-the-hosts-file-to-work-in-windows-10/
