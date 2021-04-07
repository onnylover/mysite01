from user import models


def test_models_insert():
    models.insert("JJ","JJ@korean.net","1234","male")

def test_model_findby_email_and_password():
    result = models.findbyemail_and_password("JJ@korean.net","1234")
    print(result)

# test_models_insert()
# test_model_findby_email_and_password()

def test_model_findbyno():
    result = models.findbyno("10")
    print(result)

#test_model_findbyno()

def test_update():
    results = models.update("CCC","1234","male","7")
    print(results)
test_update()