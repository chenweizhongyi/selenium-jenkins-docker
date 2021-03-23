import pytest
import yaml


def func(x):
    return x + 1

@pytest.mark.parametrize('a,b',yaml.safe_load(open('./test.yml')))
def test_answer(a,b):
    assert a == b
    print("测试完成")



if __name__ == '__main__':
    pytest.main(['-v'])