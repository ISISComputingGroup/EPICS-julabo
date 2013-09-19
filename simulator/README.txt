Running the simulator
---------------------

> python simulator.py -m FL300 -d -p 9999

-m = the julabo model (defaults to FL300)
-d = debug mode (prints out the input and output)
-p = port number (defaults to 9999)

Start the IOC
-------------

cd ..\iocs\julaboFL300\iocBoot\iocjulaboFL300
..\..\bin\windows-x64\julaboFL300.exe st_simulate.cmd