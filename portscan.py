import socket
import sys

#function for analyse ports in domain/ip
def analyse(ports, url, time):
    for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #tcp/ip
        client.settimeout(float(time))
        code = client.connect_ex((str(url), int(port))) #0 = true

        if code == 0:
            print(f' {port}/tcp - OPEN')

#variables default
ports = [21, 23, 80, 443, 8080]
error = 0
time = 0.5
url = '127.0.0.1'

#get args
arg = sys.argv

if arg.count('-h') == 0 or arg.count('--help') == 0:
    help = True

#argument -p (ports)
if arg.count('-p') != 0 and arg.count('-p') < 2:

    #explicit numbers
    if arg[arg.index('-p') + 1].count(',') != 0:
        ports = arg[arg.index('-p') + 1].split(',')

    #numbers in space
    elif arg[arg.index('-p') + 1].count('-') != 0 and arg[arg.index('-p') + 1].count('-') < 2:
        argPorts = arg[arg.index('-p') + 1].split('-')
        ports = []

        #trying convert two arguments for int
        try:
            argPorts = [int(argPorts[0]), int(argPorts[1])]

        except:
            print('\nError: invalid ports\n')
            error += 1

        #generate numbers missing
        while argPorts[0] <= argPorts[1]:
            ports.append(argPorts[0])
            argPorts[0] += 1

    else:
        print('\nError: ports invalid\n')
        error += 1

else:
    print('\nError: argument -p duplicated or not exist\n')
    error += 1


#arguments -u (url)
if arg.count('-u') != 0 and arg.count('-u') < 2:
    #get url
    url = str(arg[arg.index('-u') + 1])

else:
    print('\nError: no url info\n')
    error += 1


#arguments -t (time)
if arg.count('-t') < 2:
    try:
        time = arg[arg.index('-t') + 1]
    except:
        pass

else:
    print('\nError: argument -t duplicated\n')


#help
if arg.count('-h') > 0 or arg.count('--help') > 0:
    print("""
BASIC PORTSCAN
Commands:
            
    -h or --help: Is to see help 
            
    -p <80, 8080> or <80-8080>:	Is to indicate the ports that will be scanned (required)
    -u <url>: Is to indicate the domain or ip that will be scanned (required)
    -t <time in seconds>: is for setting a time in seconds for each scan (optional)
    """)

#call function
if error == 0:
    print('Config portscan:')
    print(f' URL - {url} \n Ports - {ports} \n Time - {time}')
    print('\nInfo:')

    analyse(ports, url, time)
