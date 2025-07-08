# Read a file and handle errors
try:
    a=input("Enter file name: ")
    file_1=open(a,'r')
    reading=file_1.read()
    print(reading)
    file_1.close()
except FileNotFoundError:
    print('Error:The file',"\'",a,"\'",'was not found')

# Write and append data to a file
b=input("Enter file name: ")
file_2=open(b,'r+')
line1=input('\nEnter text to write to the file:')
appending1=file_2.write(line1)
print('Data successfully written to',b)
line2=input('\nEnter additional text to append:')
append=file_2.write('\n')
appending2=file_2.write(line2)
print('Data successfully appended')
print('\nFinal content of',b,':')
print(line1)
print(line2)









