#include "python.h" 

static PyObject*

spam_strlen(PyObject* self, PyObject* args)
{
    const char* str = NULL;
    int len;

    if (!PyArg_ParseTuple(args, "s", &str)) // �Ű����� ���� �м��ϰ� ���������� �Ҵ� ��ŵ�ϴ�.
        return NULL;

    len = strlen(str);

    return Py_BuildValue("i", len);
}

static PyObject*
spam_division(PyObject* self, PyObject* args)
{
    int quotient = 0;
    int dividend, divisor = 0;

    if (!PyArg_ParseTuple(args, "ii", &dividend, &divisor)) //�������� ���� �Ҵ�
        return NULL;

    if (divisor) {
        quotient = dividend / divisor;
    }
    else {  // ������ 0�� �� ���� ó���� �մϴ�.
      // ���� ó���� �� ���� �ݵ�� NULL�� ���� ���ݴϴ�. PyErr_SetString�Լ��� �׻� NULL�� �����մϴ�.
      //PyExc_ZeroDivisionError�� 0���� �������� �� �� ���� �����Դϴ�.
        PyErr_SetString(PyExc_ZeroDivisionError, "divisor must not be zero");
        return  NULL;
    }

    return Py_BuildValue("i", quotient);
}
static PyObject*
spam_getmail(PyObject* self)
{
    const char* ID = "zndtldy12@gmail.com";

    return Py_BuildValue("s", ID);
}
static PyObject*
spam_getAddr(PyObject* self)
{
    const char* Addr = "mirio4155@";

    return Py_BuildValue("s", Addr);

}

static PyMethodDef SpamMethods[] = {
    {"getmail", spam_getmail, METH_VARARGS,
    "Get E mail"},
    {"getAddr", spam_getAddr, METH_VARARGS,
    "Get Address"},
    {NULL, NULL, 0, NULL}    //�迭�� ���� ��Ÿ����.
};


static struct PyModuleDef spammodule = {
    PyModuleDef_HEAD_INIT,
    "spam",            // ��� �̸�
    "It is test module.", // ��� ������ ���� �κ�, ����� __doc__�� ����˴ϴ�.
    -1,SpamMethods
};

PyMODINIT_FUNC
PyInit_spam(void)
{
    return PyModule_Create(&spammodule);
}
