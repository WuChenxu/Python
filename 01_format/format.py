#1. basic usage
print("{} world.".format("hello"))
#2. with arguments
print("{},{}".format("hello", "world"))
print("{0}, this is {1}. {1}, this is {0}.".format("Hellen", "Tom"))
print("{subject} {verb} {object}".format(object="the lazy dog", subject="the quick brown fox", verb="jumps over"))
#3. format
print("{0:d} - {0:x} -{0:X} - {0:o} - {0:b} ".format(42))
print("{0:#d} - {0:#x} -{0:#X} - {0:#o} - {0:#b} ".format(42))
pi = 3.1415926
# keep 2 digits fractional part
print("{:.2f}".format(pi))
# with sign
print("{:+.2f}".format(pi))
print("{:+.2f}".format(-1))
print("{:+.2f}".format(-1.0))

print("{:.0f}".format(2.71828))

print("{:02d}".format(5))
print("{:0>2d}".format(5))
print("{:x^10d}".format(5))
print("{:x<4d}".format(5))

print("{:,}".format(1000000))

print("{:.2%}".format(0.25))
print("e{:.2e}".format(10000000000))
print("E{:.2E}".format(10000000000))

print("{:04}".format(42))
print("{} of {:b} people know binary, the other haf don't".format(1,2))
