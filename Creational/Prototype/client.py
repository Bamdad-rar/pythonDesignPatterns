from prototype import Prototype
from expensive_object import Website



my_site = Website("main site","home","www.bamdad.com",test=False,debug=False,persistent=True)

print(my_site)
print(id(my_site))

test_site = Prototype().register("testSite", my_site).clone("testSite",name="test site",test=True,debug=True)

print(test_site)
print(id(test_site))

