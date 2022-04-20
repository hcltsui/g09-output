import argparse
try:
    from . import Opt
except ImportError:
    from opt_output import Opt

def main():
    # TODO: add optional argument: output directory
    # TODO: add optional argument: plotting force and displacement values 
    # against optimization steps
    description = "Extract coordinates from guassian09 optimization file."
    parser = argparse.ArgumentParser(description=description)
    fname_help = "filename; assume file extension is '.out'; no '.' in filename."
    parser.add_argument("fname", type=str, help=fname_help)
    args = parser.parse_args()
    fname = args.fname
    f = Opt(fname)
    f.get_xyz()

if __name__ == "__main__":
    main()

