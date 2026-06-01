AI Engineer


目的 : 在明年役期結束以前我可以熟悉AI的流程，以及程式能力可以大幅提升


什麼是pytest : 
        pytest是python的源生庫，是用來執行單元測試(Unit test) and 功能測試(Functional test)

安裝pytest : 
    commit : 
            pip install pytest

為何要做pytest : 
    確認我程式在任何情況下測試的參數是沒問題的不會報錯

    如何執行pytest : 
        先將資料夾分成以下格式：
        |src/
        | |__calculator.py 
        |
        |tests/
        | |__test_calculator.py


    def add(a, b):
        return a + b

    def test_add():
        print("---test---add---->>>>>")
        assert add(1, 2) == 3

