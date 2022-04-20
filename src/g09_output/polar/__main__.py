import argparse
try:
    from . import Polar
except ImportError:
    from polar import Polar
    
def main():
    description = "Extract data from guassian09 polar file."
    parser = argparse.ArgumentParser(description=description)
    fname_help = "filename; assume file extension is '.out'; no '.' in filename."
    parser.add_argument("fname", type=str, help=fname_help)
    args = parser.parse_args()
    fname = args.fname
    f = Polar(fname)
    f.get_data()
    
if __name__ == "__main__":
    main()
