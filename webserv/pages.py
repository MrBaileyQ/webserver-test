"""
Page language
"""

def translate_line(line, context):
    print("Translating line: %s" % line)
    for key, value in context.items():
        line = line.replace('{{'+str(key)+'}}', str(value))
    return line