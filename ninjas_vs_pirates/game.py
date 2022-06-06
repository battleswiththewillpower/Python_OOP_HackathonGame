from classes.ninja import Ninja
from classes.pirate import Pirate
#michelango is the instance/ ninja is the class thats invoking the "michelanglo" class & attributes
michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

michelangelo.throw(jack_sparrow)
jack_sparrow.show_stats()

jack_sparrow.kick(michelangelo)
michelangelo.show_stats()
