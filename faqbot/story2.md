## Generated Story -1900435358529277778
* greet
    - utter_greet
    - utter_welcome_gla
    - utter_ask_name
* request_info{"student_name": "sachin"}
    - slot{"student_name": "sachin"}
    - action_add_name
    - slot{"student_name": "sachin"}
    - utter_ask_degree
* request_info{"degree": "b.tech"}
    - slot{"degree": "b.tech"}
    - action_add_degree
    - slot{"degree": "b.tech"}
    - utter_ask_howcanhelp
* findofficeByStates{"States": "bihar"}
    - slot{"States": "bihar"}
    - action_search_state
    - slot{"States": "bihar"}
    - utter_anything_else
* findFacultyByName{"faculty_name": "deepak mangal"}
    - slot{"faculty_name": "deepak mangal"}
    - action_search_faculty
    - slot{"faculty_name": "deepak mangal"}
    - utter_anything_else
* request_info{"student_name": "whatsup"}
    - slot{"student_name": "whatsup"}
    - utter_goodbye
    - export

