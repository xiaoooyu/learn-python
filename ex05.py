name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_centimeter = height * 2.45
weight = 180 # lbs
weight_kilograms = 180 * 0.453592
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %r inches tall." % height
print "He's %d centimeter tall." % height_centimeter
print "He's %d pounds heavy." % weight
print "He's %d kilograms heavy." % weight_kilograms
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." %(
    age, height, weight, age + height + weight)
