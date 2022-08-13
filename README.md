<!-- GETTING STARTED -->
## Getting Started

This is my first commited project. It is a two-function python script to execute commands on CLI

### Prerequisites

The two functions require settings on Siri and System preference

1. Siri
You must enable "Type to Siry" by going to 
```System Preferences >> Accesibility >> Siri```

2. Mic
You must have created an ```Aggregate device ``` microphone


### Installation


1. Clone the repo

2. Install keyboard and typer packages
   ```
   pip3 install typer
   pip3 install keyboard
   ```




<!-- USAGE EXAMPLES -->
## Usage

1. Siri

The Siri command, will allow you to ask any question to Siri by typing it.

You should execute:
main.py siri "your question"

2. Mic

The command will automatically set your "Aggregate device" as mic input. This is pretty useful when your mic is constantly changing due to bluetooth connection.

You should execute:
main.py mic

