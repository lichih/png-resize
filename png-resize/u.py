import sys
import click

class AliasedGroup(click.Group):
    def get_command(self, ctx, cmd_name):
        rv = click.Group.get_command(self, ctx, cmd_name)
        if rv is not None:
            return rv
        matches = [x for x in self.list_commands(ctx)
                   if x.startswith(cmd_name)]
        if not matches:
            return None
        elif len(matches) == 1:
            return click.Group.get_command(self, ctx, matches[0])
        ctx.fail('Too many matches: %s' % ', '.join(sorted(matches)))

def pjson(d, *, err=False, **kwargs):
    import json
    # s = json.dumps(d, ensure_ascii=False, indent=2, cls=ComplexEncoder)
    s = json.dumps(d, ensure_ascii=False, indent=2)
    if err:
        kwargs['file'] = sys.stderr
    print(s, **kwargs)

def perr(*args, **kwargs):
    from inspect import getframeinfo, stack
    caller = getframeinfo(stack()[1][0])
    debug_str = f"{caller.filename}:{caller.lineno} -"
    if 'file' not in kwargs:
        kwargs['file'] = sys.stderr
    return print(debug_str, *args, **kwargs)
