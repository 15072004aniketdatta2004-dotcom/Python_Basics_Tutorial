# In python , everything is encapsulated within a PyObject 
<code>struct _object{
    Py_ssize_t ob_refcnt;
    PyTypeObject *ob_type;
};</code><br/>
This struct _objectis the "common header for all objects" in CPython  . When you write a Python x = 42object s = "hello", a pointer to this structure (or an extension thereof) is created internally.<br/>
struct _objectIt is the base type for all Python objects .<br/>
In reality typedef struct _object PyObject;, an alias is defined for it, and PyObject *it is treated as such in the code.<br/>
Py_ssize_t ob_refcnt  

This is an integer field that holds   the reference count .
Py_ssize_tThis is a signed size type ( ssize_tor equivalent), and in a 64-bit environment, it is approximately 8 bytes.  
When this value becomes 0 , the object is determined to be "not referenced by anyone," and its memory is released.


PyTypeObject *ob_type  

This is a pointer to a type object .  
PyTypeObjectPyObjectIt is a structure that inherits from itself , and is an object that represents a "type" such as   int, str, etc.list
Through this pointer,
Object type name ( type(x).__name__)  
Method Table ( tp_methods)  
Attribute retrieval function ( tp_getattro)  
Destructors ( tp_dealloc) and similar methods are referenced.<br/>






2. The meaning of "Everything in Python is a PyObject"
In the world of Python,

integer42  
string"hello"  
list[1, 2, 3]  
functiondef f(): ...  
moduleimport sys  
The type itself type,intstr

Everything PyObject *is treated as such.
Specifically, each type is defined as a structure PyObjectthat begins with .
Example: Integer object (simplified)
  typedef struct {
    PyObject ob_base;      // Coomon Header
    long ob_ival;          // Actual Integer Value
} PyLongObject;
In memory, PyLongObjectthe beginning of the string is followed by ob_refcntand ob_typethen long ob_ival.
Therefore, casting to is safe because the leading fields will match PyLongObject *.PyObject *

Similarly,

PyUnicodeObject(string)  
PyListObject(list)  
PyDictObject(dictionary)  
PyFunctionObject(function)

PyObjectIt is defined as a structure that has all of these elements at the beginning.

3. How reference counting (ob_refcnt) works
3.1 Increasing and decreasing the reference count

When references increase (e.g., variable assignment, adding to a list)  
Py_INCREF(obj)The macro is called and ob_refcnt++executed.


When references decrease (e.g., end of variable scope del, removal from list)  
Py_DECREF(obj)The macro is called and ob_refcnt--executed.  
If ob_refcnt == 0this occurs, ob_type->tp_dealloc(obj)the method is called and the object is released.



3.2 The Problem of Circular References
Reference counting alone cannot recover circular references (e.g., ). Therefore, CPython runs additional circular reference detection garbage collection using the module ( ) .a.append(a)gcPython/gc.c

ob_refcntEven if the value is not 0, unreachable circular references will be collected by the garbage collector (GC).
However, the basic release logic is still ob_refcnt == 0triggered by [something].


4. The role of type objects (ob_type)
ob_typeThis is metadata that defines "what that object is . "
PyTypeObjectMain fields (excerpt):

const char *tp_name– Model name ( e.g. "int", "str",)
destructor tp_dealloc– Object release function
getattrfunc tp_getattro– Get attributes ( obj.attr)
setattrfunc tp_setattro– Attribute settings ( obj.attr = value)
PyNumberMethods *tp_as_number– Numerical calculation method table
PySequenceMethods *tp_as_sequence– Sequence operation method table
PyMappingMethods *tp_as_mapping– Mapping arithmetic method table

As a result,

x + yteethx->ob_type->tp_as_number->nb_add(x, y)  
len(x)teethx->ob_type->tp_as_sequence->sq_length(x)

As shown above, it is possible to dynamically call different implementations depending on the type .

5. Memory layout of PyObject (example)
In memory, integers, for example, 42are generally arranged as follows:
  +----------------+     +-----------------------+
| PyLongObject * | --> | ob_refcnt (8 bytes)   |
+----------------+     +-----------------------+
                       | ob_type* (8 bytes)     |
                       +-----------------------+
                       | long ob_ival (8 bytes) |  // 42
                       +-----------------------+
The first 16 bytes (in a 64-bit environment) are PyObjectpart ( ob_refcnt+ ob_type).  
This is followed by type-specific data (in this case long).

This layout allows

(PyObject *)long_objEven if you cast it as , ob_refcntyou ob_typecan still access it correctly.
Garbage collectors and debuggers ob_typecan determine that "this is an integer object" simply by looking at it.


6. Summary

struct _object( PyObject) is the core of the CPython object system .
ob_refcntMemory management is performed using reference counting, ob_typeand dynamic dispatch (polymorphism)  is achieved.
All Python objects are implemented as derived structures that have this structure at the top, supporting the "Everything in Python " design principle.PyObject

PyObject_*This design provides a consistent API (set of functions) at the C level while enabling flexible dynamic typing, metaprogramming, and garbage collection at the Python level.
