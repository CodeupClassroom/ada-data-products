## Project Structure

### Directories

- `env`: you won't find this folder on github, but this contains all the files
  necessary for our virtual environment
- `templates`: contains the `.html` files that we reference with flask's
  `render_template` function
- `static`: contains static assets, e.g. css or image files

### Files

- `model.py`: provides an interface to our trained model
- `server.py`: defines our flask web server code
- `requirements.txt`: defines the dependencies of our application
- `spam_clean.csv`: the data our model is trained on
- `.gitignore`: tells git which files to **exclude** from the repository
