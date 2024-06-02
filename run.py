import sys
sys.path.append(".")

from berserkbjj import create_app

if __name__=='__main__':
    napp=create_app()
    napp.run(debug=True)
    