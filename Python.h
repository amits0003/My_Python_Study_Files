static PyObject MyFunction( PyObject *self, PyObject *args);

static PyObject *MyFunctionWithKeywords(PyObject *self, PyObject *args, PyObject *kw)

static PyObject *MyFunctionWithNoArgs(PyObject *self)

static PyObject *module_func(PyObject *self, PyObject *args)
{
    Py_RETURN_NONE;
}

struct PyMethodDef
{
    char *ml_name;
    PyCFunction ml_meth;
    int ml_flags;
    char *ml_doc;
}
static PyMethodDef module_methods[] =
{
    { "func" = (PyCFunction) module_func, METH_NOARGS, NULL },
    {NULL, NULL, 0, NULL }
};

''' Initialization Function '''
PyMODINIT_FUNC initModule()
{
    Py_InitModule3(func, module_methods, "docstring...");
}
