Name: Vraj Patel

UTA ID: 1001672822

Language used: Python

-------------------------------------------------------The structure of the code-------------------------------------------------------

Program will take 5 inputs 

1)source file
2)source
3)Destination
4)heuristic_file
5)algorithm type

I have three methods in my source code:

1) A_star:
	- A_star method have code for the informed search which uses 2 external file named input.txt and heuristic.txt. 
2) UCS:
	- UCS method have code for the uninformed search which uses 1 external file named input.txt.
3) Main:
	- Main method trigger one of the above method as per the user input. If user enters "inf" it will call A_star method and if user input is uninf it will trigger UCS method.


----------------------------------------------------------How to run the code-----------------------------------------------------------

The python file name is called route_algo.py. While running on omega using shell command, the following command must be typed.

$python find_route.py $input_file.txt $source $destination $heuristic_file.txt $algo_type

example 1: python route_algo.py input1.txt Bremen Frankfurt heuristic.txt inf    
(if it's informed search)

example 2: python route_algo.py input1.txt Bremen Frankfurt heuristic_file.txt uninf    
(if it's uninformed search)

Note : The source and destination is case sensitive. The name of the place must start with a captial letter or the place name input
must match with the name given in the input text file.

