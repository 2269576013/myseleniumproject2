import pytest
if __name__ == '__main__':
    pytest.main(args=["-v","../pytestpkg1/test_case1.py::TestCase1::test_case1","--html=report/report.html","--self-contained-html"])
    # 运行方式：
    # 1.修改Test_App/pytest.ini文件，添加报告参数，即：addopts = -s --html=./report.html
    #     # -s:输出程序运行信息
    #     # --html=./report.html 在当前目录下生成report.html文件
    #     ️ 若要生成xml文件，可将--html=./report.html 改成 --html=./report.xml
    # 2.命令行进入Test_App目录
    # 3.执行命令： pytest   
    # 执行结果：
    #     1.在当前目录会生成assets文件夹和report.html文件