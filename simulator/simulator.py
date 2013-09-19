import SocketServer
import re
import argparse
from FL300 import JulaboFL300
from FP50_MH import JulaboFP50_MH

class SimulatorTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        global SIMULATOR, DEBUG
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        
        ans = SIMULATOR.check_command(self.data)
        
        if DEBUG :
            print self.data, "returned", ans
        
        if not ans is None:
            self.request.sendall(ans)
            
if __name__ == "__main__":
    #Argument parser - checks for debug mode and port
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', action='store_true', help='put into debug mode')
    parser.add_argument('-p', '--port', type=int, nargs=1, default=9999, help='server port')
    parser.add_argument('-m', '--model',  nargs=1, default=['FL300'], help='julabo model: FL300 (default)')
    args = parser.parse_args()
    DEBUG = args.debug
    model = args.model[0].upper().strip()
    
    #Define the type of simulator
    if model == 'FL300':
        print "Model: Julabo", model
        SIMULATOR = JulaboFL300()
    elif model == 'FP50_MH':
        print "Model: Julabo", model
        SIMULATOR = JulaboFP50_MH()
    else:
        #undefined
        raise Exception("Unrecognised Julabo model")
    
    # Create the server, binding to localhost on port 
    server = SocketServer.TCPServer(("localhost", args.port), SimulatorTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()