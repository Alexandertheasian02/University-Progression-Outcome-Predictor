# University-Progression-Outcome-Predictor
Developed a Python program enabling students to predict academic progression outcomes. Implemented user-defined functions to prompt for credit details and determine progress. Enhancing academic planning and decision-making for students.
A University requires a program to predict progression outcomes at the end of each academic year. One student should take a total of 6 modules in an academic year and each module gives 20 marks when passed. Given below are the possible outcomes for the students.


  	
1st Column - Pass | 2nd Column - Defer | 3rd Column - Fail | 4th Column - Progression Outcome

120    0  	  0  	 Progress  
100  	 20  	  0  	 Progress (module trailer)  
100  	 0  	  20   Progress (module trailer)  
80  	 40  	  0  	 Do not Progress – module retriever  
80  	 20  	  20   Do not Progress – module retriever  
80  	 0  	  40   Do not Progress – module retriever  
60  	 60  	  0  	 Do not progress – module retriever  
60  	 40  	  20   Do not progress – module retriever  
60  	 20  	  40   Do not progress – module retriever  
60  	 0   	  60   Do not progress – module retriever  
40  	 80  	  0  	 Do not progress – module retriever  
40  	 60  	  20   Do not progress – module retriever  
40  	 40  	  40   Do not progress – module retriever  
40  	 20  	  60   Do not progress – module retriever  
40  	 0  	  80   Exclude  
20  	 100  	0  	 Do not progress – module retriever  
20  	 80  	  20   Do not progress – module retriever  
20  	 60  	  40   Do not progress – module retriever  
20  	 40  	  60   Do not progress – module retriever  
20  	 20  	  80   Exclude  
20  	 0  	  100  Exclude  
0  	   120  	0  	 Do not progress – module retriever  
0  	   100  	20   Do not progress – module retriever  
0  	   80  	  40   Do not progress – module retriever  
0  	   60  	  60   Do not progress – module retriever  
0  	   40  	  80   Exclude  
0  	   20  	  100  Exclude  
0  	   0  	  120  Exclude  


This project consists of:
Validations, Multiple Outcomes, Histogram, Lists, Dictionaries, User-defined functions

