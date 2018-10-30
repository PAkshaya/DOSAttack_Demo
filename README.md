# DOSAttack_Demo
DOS Attack and Mitigation using HoneyPot Demo in VMware Ubuntu

Network Setup
1. Install Wireshark at Victim  side and at Honeypot side
      Follow the instruction given:
          https://jlospinoso.github.io/software/wireshark/networks/ubuntu/2015/02/11/configuring-wireshark-on-ubuntu-14.html
2. Open the pdf of Configuration. 
  In Terminal of respective machine write: sudo nano /etc/network.interfaces
  Make the changes in this file according to Configuration file given and reboot the machine.
  Make sure the change in the ip address is reflected.

3. Code
  sniffAndReroute.py at Router Machine.
  SYN_Flood.py at Attacker Machine.
  In Terminal of respective machine write: sudo nano <file_name> and copy the code.
  
 4. Run
 Start wireshark at Victim side and at Honeypot side in Non promiscuous mode.
 at Router Run: python  sniffAndReroute.py
 at Attacker Run: python  SYN_Flood.py <victim's ip address>

Attack and Mitigation can be seen in wireshark.
