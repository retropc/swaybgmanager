import json

OUTPUTS = {}

def output(name):
  def decorator(fn):
    OUTPUTS[name] = fn
    return fn
  return decorator

def escape(fn):
  return json.dumps(fn)

def bg(fn, mode):
  return ("bg", escape(fn), mode)

def colour(colour):
  return ("bg", colour, "solid_color")
