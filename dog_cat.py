# File Name: dog_cat.py


# �����ǹ��ļ��ϣ������ʵ���Ǿ����ĳһֻ��
class Dog(object):
    def __init__(self, name):
        # Python ��˽��������һ���������»��߿�ͷ��ʾ
        # һ���»��߿�ͷ��˽�����Ա�ʾ�ⲿ�����߲�Ӧ��ֱ�ӵ���������ԣ������ǿ��Ե���
        # �����»����ⲿ�Ͳ���ֱ�ӵ����ˣ���Ҳ�а취
        self._name = name

    # ˽������ _name �����Ա�ֱ�ӵ���
    # �����Ҫ���������������޸ĺͻ�ȡ������ֵ
    # get_name ������ȡ����ֵ��set_name �����޸�����ֵ
    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    # �÷���������ӡ����Ľ���
    def say(self):
        # ���� self._name ����ֱ�ӵ���˽������
        # ������ڲ���������д��������ⲿ������Ŷ
        print(self._name + 'is making sound wang wang wang...')


# ������è�ļ��ϣ������ʵ���Ǿ����ĳһֻè
class Cat(object):
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def say(self):
        print(self._name + 'is making sound miu miu miu...')