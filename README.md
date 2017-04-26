# An API Manager for all your APIs
A lean API that manages all your other APIs. Written in python using the Flask framework.

## Description
This app is an API that manages all your other APIs. The purpose is to easily store all your API credentials (keys and url) so that users need not worry about all the different connections and keys needed to access different APIs. 

## Setup
This app requires setting up:
* YAML file with your API keys
* Environment variable

### Create your YAML file 
Create a YAML file with your API keys. We store the API keys in a YAML file (and not in the .py file) because we do not want to expore the keys to others.

```yaml
census: &census
    key: 'fa264747f925262537dc391bdkahfjkgsdf89'
```

### Setup your environment variable
This variable stores the path where your YAML file is located. You will call the variable in your Flask app and load your YAML file. We set an environment variable so that we can move this app to different servers/computers without hardcoding the path of your YAML file.

Enter the environment variable in your ```.bash_profile``` or ```.bashrc``` in the home directory
```
export API_CONFIG=/User/username
```

### Running the app
In your terminal, run 

    python app.py
    
Now make an API request any way you normally would.
