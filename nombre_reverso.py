Import serial as s
Puerto_serial=s.Serial('COM6',57600,TIMEOUT=0)

While(1):
{
	if(Puerto_serial.inwaiting>0):
	{
		nombre=Puerto_serial.readline()
	
		nombre = nombre[:-1]

			for i in range(0,LEN(DATA)): 
			{
				Puerto_serial.write(nombre(LEN(nombre)-1-i])
				Puerto_serial.write(str(i+1))
			}
	}

}

