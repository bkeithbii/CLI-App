# CLI-App

This project was designed to test my knowledge of Python and SQL along with their interaction together while building a command line application. 

My app replicates a note taker and is solely command line compatible. Currently the application allows users to create an account, design notes, view their note library in totality and will soon allow users to delete their accounts/notes as well. 

## How-To-Use

To run the application locally, please ensure you have pipenv installed on your machine and fork and clone the repository. Once the repo has been cloned locally, run pipenv install to install dependencies. 

Ensure that you are running Postgres on your machine and connect from the root level of this directory.

After initial set up please follow these commands sequentially: 
```
pipenv install
pipenv shell
python3 lib/main.py
```

## Example
**Upon running the "python3 lib/main.py" command you will be presented with the first menu**

![Example](./Screen&#32;Shot&#32;2020-03-29&#32;at&#32;10.33.41&#32;AM.png)


## Built With

- PeeWee
- Python
- PostgreSQL

## Future Updates

- Give users the ability to delete both notes and accounts as a whole.
- Build a UI for the application to give the notes life.
- Allow users to enter notes with special files such as images or links.

## Contributing

Please feel free to fork, clone and submit any potential new features that can be added or adjusted with the current code!

## Authors

- [Brian Brown II](https://github.com/bkeithbii)

