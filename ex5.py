name = 'Zed A. Shaw'
age = 35 #not a lie
height_in_inches = 74 #inches
height_in_centimeters = height_in_inches * 2.54
weight_in_pounds = 180 #pounds
weight_in_kilograms = weight_in_pounds * 0.453592
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d centimeters tall." % height_in_centimeters
print "He's %d kilograms heavy." % weight_in_kilograms
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (age, height_in_centimeters, weight_in_kilograms, age + height_in_centimeters + weight_in_kilograms)
