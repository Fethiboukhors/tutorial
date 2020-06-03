import random
import udacity


def silly_string(nouns, verbs, templates):
    # Choose a random template.
    template = random.choice(templates)

    # We'll append strings into this list for output.
    output = []

    # Keep track of where in the template string we are.
    index = 0
    position = 0
    while position < len(template):
        if template[position:position + 8] == '{{noun}}':
            output.append(random.choice(nouns))
            position += 8
        elif template[position:position + 8] == '{{verb}}':
            output.append(random.choice(verbs))
            position += 8
        else:
            output.append(template[position])
            position +=1
    # Add a while loop here.

    # After the loop has finished, join the output and return it.


if __name__ == '__main__':
    print(silly_string(udacity.nouns, udacity.verbs,udacity.templates))