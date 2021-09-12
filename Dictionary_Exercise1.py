def main():
    #Create dictionaries 
    '''
    course_room = {'CS101':'3004',
                   'CS102':'4501',
                   'CS103':'6755',
                   'NT110':'1244',
                   'CM241':'1411'}
    
    course_instructor = {'CS101':'Haynes',
                         'CS102':'Alvarado',
                         'CS103':'Rich',
                         'NT110':'Burke',
                         'CM241':'Lee'}

    course_time = {'CS101':'8:00 am',
                   'CS102':'9:00 am',
                   'CS103':'10:00 am',
                   'NT110':'11:00 am',
                   'CM241':'1:00 pm'}
  '''  
  

    course_dictionary = {'CS101':{'room':'3004', 'isntructor':'Haynes', 'time':'8:00 am'},
                         'CS102':{'room':'4501', 'isntructor':'Alvarado', 'time':'9:00 am'},
                         'CS103':{'room':'6755', 'isntructor':'Rich', 'time':'10:00 am'},
                         'NT110':{'room':'1244', 'isntructor':'Burke', 'time':'11:00 am'},  
                         'CM241':{'room':'1411', 'isntructor':'Lee', 'time':'1:00 pm'}}
    
 #User selects course

    course_num = input('Enter a course number')
    print(course_dictionary[course_num])

main()