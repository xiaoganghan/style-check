import os
import string
import re

def get_absolute_paths(directory):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    rules_dir = os.path.join(current_dir, directory)
    for dirpath,_,filenames in os.walk(rules_dir):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f))


def get_rules():
    censored_phrases = {}
    for file in get_absolute_paths('rules'):
        with open(file) as f:
            for line in f.readlines():
                if not line.startswith('##') and line.count('%')==1:
                    expression, reason = line.split('%')
                    expression = expression.rstrip()
                    reason = reason.strip()
                    # expression, reason = map(str.strip, line.split('%'))
                    if reason:
                        check_type = reason.split()[0]
                        if check_type == 'syntax':
                            re_exp = expression
                            regex = re.compile(re_exp)
                        elif check_type == 'capitalize':
                            re_exp = r'\b%s\b' % expression
                            regex = re.compile(re_exp)
                        elif check_type == 'phrase':
                            expression = re.sub('/ +/', '\s+', expression)
                            expression = re.sub('/([a-zA-Z\)])$/', '\1\b', expression)
                            re_exp = r'\b%s\b' % expression
                            regex = re.compile(re_exp, re.IGNORECASE)
                        elif check_type == 'spelling':
                            re_exp = r'\b%s\b' % expression
                            regex = re.compile(re_exp, re.IGNORECASE)
                        censored_phrases[regex] = reason
    return censored_phrases


def match(censored_phrases, text):
    problems = []
    for ind, line in enumerate(text.split('\n')):
        for k, v in censored_phrases.items():
            m = k.search(line)
            if m:
                problems.append((m.group(), ind+1, m.span(), k.pattern, v))
    problems = sorted(problems, key=lambda x: x[1])
    return problems


if __name__ == '__main__':
    text = """
    hello the the book is very good in order to utilize
    hello the the book is very good in order to utilize
    """
    print(match(get_rules(), text))