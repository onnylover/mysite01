from board import models


def test_listcall():
    results = models.listcall(1,5)
    print(results)

def test_max():
    results = models.maxno()
    print(results)

#test_listcall()
#test_max()

def test_maxgno():
    results = models.maxgno()
    # data = {
    #     "results" : results
    # }
    #print(type(results.get("max")))
    print(results)
    #print(data.max)

#test_maxgno()

def test_insert():
    results = models.insert("modeltest", "modeltest,modeltest,modeltest,modeltest,",6)
    print(results)

#test_insert()

def test_contentscall():
    no = "10"
    results = models.contentscall(no)
    print(results)

#test_contentscall()

def test_update():
    results = models.update("업데이트 테스트용 구.test4","잘 변경 되었으면 좋겠습니다.",7)
    print(results)
#test_update()

def test_delete():
    results = models.delete(1)
    print(results)
#test_delete()

def test_hit():
    results = models.hit(32)
    print(results)
test_hit()