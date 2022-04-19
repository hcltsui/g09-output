import argparse
try:
    from . import Opt
except ImportError:
    from g09_opt import Opt

def main():
    description = "Extract coordinates from guassian09 optimization file"
    parser = argparse.ArgumentParser(description=description)
    fname_help = "filename; assume file extension is '.out'; no '.' in filename."
    parser.add_argument("fname", type=str, help=fname_help)
    fname = parser.fname
    f = Opt(fname)
    f.get_xyz()

if __name__ == "__main__":
    main()

