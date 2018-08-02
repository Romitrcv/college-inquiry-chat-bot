## greet
* greet
    - utter_greet
    - utter_welcome_gla

## thankyou
* thankyou
	- utter_ask_howcanhelp
## goodbye
* goodbye
    - utter_goodbye

## askhelp
* request_info
    - utter_ask_howcanhelp

## askstate
* request_info
    - utter_ask_States

## state_search
* findofficeByStates
    - action_search_state
    - slot{"States":"Bihar"}

## askname
* request_info
    - utter_ask_name

## add_student_name
* inform{"student_name":"sachin"}
	- action_add_name

## story1
* greet
	- utter_greet
	- utter_welcome_gla
* thankyou
	- utter_yourwelcome
	- utter_ask_name
* inform{"student_name":"sachin"}
	- action_add_name
	- slot{"student_name":"sachin"}
	- utter_ask_howcanhelp
* findofficeByStates{"States":"Bihar"}
	- action_search_state
	- slot{"States":"Bihar"}
	- utter_anything_else
* goodbye
    - utter_goodbye



## story2
* greet
	- utter_greet
	- utter_welcome_gla
* thankyou
	- utter_yourwelcome
	- utter_ask_name
* inform{"student_name":"sachin"}
	- action_add_name
	- slot{"student_name":"sachin"}
	- utter_ask_howcanhelp
* findFacultyByName{"faculty_name":"deepak"}
	- action_search_faculty
	- slot{"faculty_name":"deepak"}
	- utter_anything_else
* goodbye
    - utter_goodbye

## story3
* greet
	- utter_greet
	- utter_welcome_gla
	- utter_ask_name
* inform{"student_name":"sachin"}
	- action_add_name
	- utter_ask_howcanhelp
* findofficeByStates{"States":"Bihar"}
	- action_search_state
	- slot{"States":"Bihar"}
	- utter_anything_else
* findFacultyByName{"faculty_name":"deepak mangal"}
	- action_search_faculty
	- slot{"faculty_name":"deepak mangal"}
	- utter_anything_else
* goodbye
    - utter_goodbye    

## story4
* greet
	- utter_greet
	- utter_welcome_gla
	- utter_ask_name
* inform{"student_name":"sachin"}
	- action_add_name
	- utter_ask_degree

* inform{"degree":"b.tech"}
	- action_add_degree
	- slot{"student_name":"sachin"}
	- utter_ask_howcanhelp

* findofficeByStates{"States":"Bihar"}
	- action_search_state
	- utter_anything_else
* findFacultyByName{"faculty_name":"deepak mangal"}
	- action_search_faculty
	- utter_anything_else
* goodbye
    - utter_goodbye    

