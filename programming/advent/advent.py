
def get_input(day):
    fn = '2023.{0}.input'.format(day)
    with open(fn) as f:
        text = f.read()
        lines = [e.strip() for e in text.split('\n') if e.strip()]

    return lines
    
