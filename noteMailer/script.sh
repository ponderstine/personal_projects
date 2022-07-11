pip install -r dependencies.txt # ensure that all dependencies are installed

# if builds and tests successfully then run
if [pip list | grep -F schedule] #TODO
then
    echo "Hello world"
    # python3 main.py & # Run python script in background
else
    echo "An error occurred.\n"