name = "Foo Bar"
age = 21
height = 74 #inches
weight = 180 #lbs
eyes = 'Orange'
teeth = 'White'
hair = 'Green'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually, that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the tea." % teeth

print "If I add %d, %d, and %d I get %d." % ( age, height, weight, age + height + weight)
