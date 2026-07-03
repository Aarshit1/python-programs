student_data={
    "id1":{"name":"David", "class":"V", "subject_integration":"english, maths, science"},
    "id2":{"name":"Lucy", "class":"V","subject_integration":"english, maths, science"},
    "id3":{"name":"Falco", "class":"V","subject_integration":"english, maths, science"},
    "id4":{"name":"David", "class":"V", "subject_integration":"english, maths, scienece"}
}

result={}
seen_keys=[]

for student_id, details in student_data.items():
    unique_key=(details["name"], details["class"], details["subject_integration"])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id]=details

for k, v in result.items():
    print(k, ":", v)