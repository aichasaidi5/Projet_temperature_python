import serial

ser = serial.Serial('COM5', 9600)

myData= ser.readline().strip()
data2=myData.decode('utf-8')

data3= 9/5*(float(data2))+32
print ("temperature est:",+data3 )

if 80 <= float(data3) <= 90:
	print("Tepmperature est normale ,",+data3)

elif 20 <= data3 <= 25:
	print("La tepmperature est "+data3+"  deg C, le bebe peut avoir froid")

else:
	print("La température n'est pas acceptable pour le bebe")
