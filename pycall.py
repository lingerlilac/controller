import ctypes
import subprocess
ll = ctypes.cdll.LoadLibrary
lib = ll("./receivea.so")
# a = lib.foo(1, 3)
# b = lib.print_cons()
# c = lib.arr()
# print '***finish***'
# print a, b
# print c

# child1 = subprocess.Popen(lib.print_cons0(), shell=True,
#                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# child2 = subprocess.Popen(lib.print_cons1(), shell=True,
#                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# child3 = subprocess.Popen(lib.print_cons2(), shell=True,
#                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# print child1
# print child2
# print child3
# c1 = subprocess.call(lib.print_cons0(),)
# print c1
# print ''
# c2 = subprocess.call(lib.print_cons2(),)
# print c2
# a = lib.abc()
b = lib.main()
# print a
