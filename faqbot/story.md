## Generated Story -3158646659815770510
* greet
    - utter_greet
    - utter_welcome_gla
* findFacultyByName{"faculty_name": "deepak"}
    - slot{"faculty_name": "deepak"}
    - action_search_faculty
    - slot{"faculty_name": "deepak"}
    - utter_ask_name
* request_info{"student_name": "romit"}
    - slot{"student_name": "romit"}
    - utter_anything_else
* findofficeByStates{"States": "bihar"}
    - slot{"States": "bihar"}
    - action_search_state
    - utter_anything_else
* request_info{"degree": "b.tech"}
    - slot{"degree": "b.tech"}
    - action_add_degree
    - slot{"degree": "b.tech"}
    - utter_ask_howcanhelp
* findofficeByStates{"States": "bihar"}
    - slot{"States": "bihar"}
    - action_search_state
    - utter_anything_else
* goodbye
    - export

